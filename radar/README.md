# Public radar

This directory is a dependency-free, offline-capable static site. Its checked-in
`data.js` is generated only from committed historical result artifacts and
self-contained A-share Markdown points; it does not fetch scores from a client
or external API.

```bash
uv run pitfall radar build
python3 -m http.server 4173 --directory radar
```

Open `http://127.0.0.1:4173`. Opening `index.html` directly also works because
the payload is a JavaScript assignment rather than a runtime `fetch()`.

The site deliberately labels current historical replays as development
diagnostics. It will not show a formal leaderboard until a pre-registered sealed
hard-case suite has matured and passed verifier-owned resolution.
