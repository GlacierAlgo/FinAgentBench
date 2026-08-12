"""Bitemporal issuer dossiers for longitudinal A-share benchmarks.

The dossier is an authoring artifact: it may contain an issuer's complete known
history.  Agents must only receive :meth:`IssuerDossier.as_of_slice`, which uses
``info_date`` for public visibility and ``effective_date`` for state projection.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

from finagentbench.case import CaseValidationError

ISSUER_DOMAINS = frozenset(
    {
        "identity",
        "governance",
        "financing",
        "capital_allocation",
        "operations",
        "commercial",
        "working_capital",
        "cash_payment",
        "reporting",
        "regulatory",
        "listing",
        "market",
    }
)


@dataclass(frozen=True)
class IssuerIdentity:
    """Stable security identity; mutable names belong on the event timeline."""

    order_book_id: str
    ticker: str
    exchange: str

    @classmethod
    def from_dict(cls, payload: dict[str, Any], *, source: str) -> IssuerIdentity:
        _require_exact_fields(
            payload,
            {"order_book_id", "ticker", "exchange"},
            source=source,
        )
        order_book_id = _string(
            payload["order_book_id"], field="order_book_id", source=source
        )
        ticker = _string(payload["ticker"], field="ticker", source=source)
        exchange = _string(payload["exchange"], field="exchange", source=source)
        expected = f"{ticker}.{exchange}"
        if order_book_id != expected:
            raise CaseValidationError(
                f"{source}: order_book_id must equal ticker.exchange ({expected})"
            )
        if not re.fullmatch(r"\d{6}", ticker):
            raise CaseValidationError(f"{source}: ticker must contain six digits")
        if not re.fullmatch(r"[A-Z][A-Z0-9]{2,7}", exchange):
            raise CaseValidationError(
                f"{source}: exchange must be an uppercase market code"
            )
        return cls(order_book_id=order_book_id, ticker=ticker, exchange=exchange)

    def to_dict(self) -> dict[str, str]:
        return {
            "order_book_id": self.order_book_id,
            "ticker": self.ticker,
            "exchange": self.exchange,
        }


@dataclass(frozen=True)
class DossierSource:
    id: str
    published_at: date
    source_type: str
    title: str
    locator: str

    @classmethod
    def from_dict(cls, payload: dict[str, Any], *, source: str) -> DossierSource:
        _require_exact_fields(
            payload,
            {"id", "published_at", "source_type", "title", "locator"},
            source=source,
        )
        return cls(
            id=_identifier(payload["id"], field="id", source=source),
            published_at=_date(
                payload["published_at"], field="published_at", source=source
            ),
            source_type=_identifier(
                payload["source_type"], field="source_type", source=source
            ),
            title=_string(payload["title"], field="title", source=source),
            locator=_string(payload["locator"], field="locator", source=source),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "published_at": self.published_at.isoformat(),
            "source_type": self.source_type,
            "title": self.title,
            "locator": self.locator,
        }


@dataclass(frozen=True)
class DossierEvent:
    """One public-information event and its possibly different effective date."""

    id: str
    domain: str
    event_type: str
    info_date: date
    effective_date: date
    summary: str
    source_ids: tuple[str, ...]
    state_updates: dict[str, Any]
    details: dict[str, Any]

    @classmethod
    def from_dict(cls, payload: dict[str, Any], *, source: str) -> DossierEvent:
        _require_exact_fields(
            payload,
            {
                "id",
                "domain",
                "event_type",
                "info_date",
                "effective_date",
                "summary",
                "source_ids",
                "state_updates",
                "details",
            },
            source=source,
        )
        domain = _identifier(payload["domain"], field="domain", source=source)
        if domain not in ISSUER_DOMAINS:
            allowed = ", ".join(sorted(ISSUER_DOMAINS))
            raise CaseValidationError(
                f"{source}: unsupported issuer domain {domain!r}; expected {allowed}"
            )
        source_ids = _identifier_list(
            payload["source_ids"], field="source_ids", source=source
        )
        state_updates = _json_object(
            payload["state_updates"], field="state_updates", source=source
        )
        for key in state_updates:
            _identifier(key, field="state_updates key", source=source)
        details = _json_object(payload["details"], field="details", source=source)
        return cls(
            id=_identifier(payload["id"], field="id", source=source),
            domain=domain,
            event_type=_identifier(
                payload["event_type"], field="event_type", source=source
            ),
            info_date=_date(payload["info_date"], field="info_date", source=source),
            effective_date=_date(
                payload["effective_date"], field="effective_date", source=source
            ),
            summary=_string(payload["summary"], field="summary", source=source),
            source_ids=source_ids,
            state_updates=state_updates,
            details=details,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "domain": self.domain,
            "event_type": self.event_type,
            "info_date": self.info_date.isoformat(),
            "effective_date": self.effective_date.isoformat(),
            "summary": self.summary,
            "source_ids": list(self.source_ids),
            "state_updates": _json_copy(self.state_updates),
            "details": _json_copy(self.details),
        }


@dataclass(frozen=True)
class DossierSlice:
    """Leakage-safe public view of an issuer dossier at a specified date."""

    schema_version: int
    dossier_id: str
    issuer: IssuerIdentity
    as_of: date
    visible_events: tuple[DossierEvent, ...]
    effective_events: tuple[DossierEvent, ...]
    current_state: dict[str, Any]
    sources: tuple[DossierSource, ...]

    @property
    def planned_events(self) -> tuple[DossierEvent, ...]:
        """Events already public but not yet effective at ``as_of``."""
        effective_ids = {event.id for event in self.effective_events}
        return tuple(
            event for event in self.visible_events if event.id not in effective_ids
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "artifact_type": "finagentbench.issuer_dossier_slice.v1",
            "dossier_id": self.dossier_id,
            "issuer": self.issuer.to_dict(),
            "as_of": self.as_of.isoformat(),
            "visible_events": [event.to_dict() for event in self.visible_events],
            "effective_events": [event.to_dict() for event in self.effective_events],
            "current_state": _json_copy(self.current_state),
            "sources": [item.to_dict() for item in self.sources],
        }

    def digest(self) -> str:
        return _digest(self.to_dict())


@dataclass(frozen=True)
class IssuerDossier:
    """Complete longitudinal history keyed by a stable ``order_book_id``."""

    schema_version: int
    dossier_id: str
    issuer: IssuerIdentity
    events: tuple[DossierEvent, ...]
    sources: tuple[DossierSource, ...]

    @classmethod
    def from_dict(
        cls, payload: dict[str, Any], *, source: str = "<memory>"
    ) -> IssuerDossier:
        _require_exact_fields(
            payload,
            {"schema_version", "dossier_id", "issuer", "events", "sources"},
            source=source,
        )
        if payload["schema_version"] != 1:
            raise CaseValidationError(f"{source}: schema_version must be 1")
        dossier_id = _identifier(
            payload["dossier_id"], field="dossier_id", source=source
        )
        issuer = IssuerIdentity.from_dict(
            _object(payload["issuer"], field="issuer", source=source),
            source=f"{source}: issuer",
        )
        raw_sources = _non_empty_list(
            payload["sources"], field="sources", source=source
        )
        sources = tuple(
            DossierSource.from_dict(
                _object(raw, field="source", source=f"{source}: sources[{index}]"),
                source=f"{source}: sources[{index}]",
            )
            for index, raw in enumerate(raw_sources)
        )
        _unique((item.id for item in sources), field="source IDs", source=source)
        source_by_id = {item.id: item for item in sources}

        raw_events = _non_empty_list(payload["events"], field="events", source=source)
        events = tuple(
            DossierEvent.from_dict(
                _object(raw, field="event", source=f"{source}: events[{index}]"),
                source=f"{source}: events[{index}]",
            )
            for index, raw in enumerate(raw_events)
        )
        _unique((item.id for item in events), field="event IDs", source=source)
        referenced_sources: set[str] = set()
        for event in events:
            unknown = sorted(set(event.source_ids) - source_by_id.keys())
            if unknown:
                raise CaseValidationError(
                    f"{source}: event {event.id!r} references unknown sources: "
                    f"{', '.join(unknown)}"
                )
            event_sources = [source_by_id[item] for item in event.source_ids]
            latest_source_date = max(item.published_at for item in event_sources)
            if latest_source_date > event.info_date:
                raise CaseValidationError(
                    f"{source}: event {event.id!r} references a source published "
                    "after its info_date"
                )
            referenced_sources.update(event.source_ids)
        orphan_sources = sorted(source_by_id.keys() - referenced_sources)
        if orphan_sources:
            raise CaseValidationError(
                f"{source}: unreferenced sources: {', '.join(orphan_sources)}"
            )

        return cls(
            schema_version=1,
            dossier_id=dossier_id,
            issuer=issuer,
            events=tuple(sorted(events, key=_visible_event_key)),
            sources=tuple(
                sorted(sources, key=lambda item: (item.published_at, item.id))
            ),
        )

    def as_of_slice(self, as_of: date | str) -> DossierSlice:
        """Return public and effective timelines without post-``as_of`` facts.

        Visibility is governed exclusively by ``info_date``.  State projection
        additionally requires ``effective_date`` not to exceed ``as_of``.  This
        deliberately preserves announced future changes as planned events while
        preventing them from becoming current state too early.
        """
        cutoff = _coerce_date(as_of, field="as_of", source=self.dossier_id)
        visible = tuple(event for event in self.events if event.info_date <= cutoff)
        effective = tuple(
            sorted(
                (event for event in visible if event.effective_date <= cutoff),
                key=_effective_event_key,
            )
        )
        state: dict[str, Any] = {}
        for event in effective:
            for key, value in event.state_updates.items():
                state[key] = _json_copy(value)
        visible_source_ids = {
            source_id for event in visible for source_id in event.source_ids
        }
        sources = tuple(item for item in self.sources if item.id in visible_source_ids)
        return DossierSlice(
            schema_version=self.schema_version,
            dossier_id=self.dossier_id,
            issuer=self.issuer,
            as_of=cutoff,
            visible_events=visible,
            effective_events=effective,
            current_state=state,
            sources=sources,
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema_version": self.schema_version,
            "dossier_id": self.dossier_id,
            "issuer": self.issuer.to_dict(),
            "events": [event.to_dict() for event in self.events],
            "sources": [item.to_dict() for item in self.sources],
        }

    def digest(self) -> str:
        return _digest(self.to_dict())


def load_dossier(path: Path) -> IssuerDossier:
    """Load and validate one JSON issuer dossier."""
    return IssuerDossier.from_dict(_read_object(path), source=str(path))


def load_dossiers(directory: Path) -> tuple[IssuerDossier, ...]:
    """Load a directory of configuration-driven issuer dossiers."""
    if not directory.is_dir():
        raise CaseValidationError(f"dossier directory does not exist: {directory}")
    paths = sorted(directory.glob("*.json"))
    if not paths:
        raise CaseValidationError(f"dossier directory contains no JSON: {directory}")
    dossiers = tuple(load_dossier(path) for path in paths)
    _unique(
        (item.dossier_id for item in dossiers),
        field="dossier IDs",
        source=str(directory),
    )
    _unique(
        (item.issuer.order_book_id for item in dossiers),
        field="issuer order_book_ids",
        source=str(directory),
    )
    return dossiers


def dossier_digest(dossier: IssuerDossier | DossierSlice) -> str:
    """Return the canonical SHA-256 digest of a dossier artifact."""
    return dossier.digest()


def _visible_event_key(event: DossierEvent) -> tuple[date, date, str]:
    return (event.info_date, event.effective_date, event.id)


def _effective_event_key(event: DossierEvent) -> tuple[date, date, str]:
    return (event.effective_date, event.info_date, event.id)


def _read_object(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CaseValidationError(f"{path}: invalid JSON: {error}") from error
    return _object(payload, field="top-level value", source=str(path))


def _digest(payload: dict[str, Any]) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _require_exact_fields(
    payload: dict[str, Any], required: set[str], *, source: str
) -> None:
    missing = sorted(required - payload.keys())
    if missing:
        raise CaseValidationError(f"{source}: missing fields: {', '.join(missing)}")
    unknown = sorted(payload.keys() - required)
    if unknown:
        raise CaseValidationError(f"{source}: unknown fields: {', '.join(unknown)}")


def _object(value: Any, *, field: str, source: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CaseValidationError(f"{source}: {field} must be an object")
    return value


def _json_object(value: Any, *, field: str, source: str) -> dict[str, Any]:
    result = _object(value, field=field, source=source)
    try:
        return json.loads(json.dumps(result, ensure_ascii=False, allow_nan=False))
    except (TypeError, ValueError) as error:
        raise CaseValidationError(
            f"{source}: {field} must contain only finite JSON values"
        ) from error


def _json_copy(value: Any) -> Any:
    return json.loads(json.dumps(value, ensure_ascii=False, allow_nan=False))


def _non_empty_list(value: Any, *, field: str, source: str) -> list[Any]:
    if not isinstance(value, list) or not value:
        raise CaseValidationError(f"{source}: {field} must be a non-empty list")
    return value


def _string(value: Any, *, field: str, source: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CaseValidationError(f"{source}: {field} must be a non-empty string")
    return value.strip()


def _identifier(value: Any, *, field: str, source: str) -> str:
    result = _string(value, field=field, source=source)
    if not re.fullmatch(r"[a-z][a-z0-9_-]*", result):
        raise CaseValidationError(
            f"{source}: {field} must use lowercase ASCII identifier syntax"
        )
    return result


def _identifier_list(value: Any, *, field: str, source: str) -> tuple[str, ...]:
    raw = _non_empty_list(value, field=field, source=source)
    result = tuple(
        _identifier(item, field=f"{field} item", source=source) for item in raw
    )
    _unique(result, field=field, source=source)
    return result


def _coerce_date(value: date | str, *, field: str, source: str) -> date:
    if isinstance(value, date):
        return value
    return _date(value, field=field, source=source)


def _date(value: Any, *, field: str, source: str) -> date:
    raw = _string(value, field=field, source=source)
    try:
        return date.fromisoformat(raw)
    except ValueError as error:
        raise CaseValidationError(f"{source}: {field} must be YYYY-MM-DD") from error


def _unique(values: Any, *, field: str, source: str) -> None:
    items = list(values)
    if len(items) != len(set(items)):
        raise CaseValidationError(f"{source}: {field} must be unique")
