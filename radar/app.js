(function () {
  "use strict";

  const data = window.PITFALL_RADAR_DATA;
  if (!data) {
    document.body.textContent = "Radar data is missing. Run pitfall radar build.";
    return;
  }

  const modelColors = ["#147d73", "#6854a6", "#c2702d", "#2f6690", "#a83f36"];
  const colorByModel = new Map(data.models.map((model, index) => [model, modelColors[index % modelColors.length]]));
  const state = { family: "all", model: "all", query: "", sort: "difficulty" };
  let lastInfoTrigger = null;

  const $ = (selector) => document.querySelector(selector);
  const node = (tag, className, text) => {
    const element = document.createElement(tag);
    if (className) element.className = className;
    if (text !== undefined) element.textContent = text;
    return element;
  };
  const format = (value, digits = 3) => value === null ? "—" : Number(value).toFixed(digits);
  const percent = (value, digits = 0) => value === null ? "—" : `${(Number(value) * 100).toFixed(digits)}%`;
  const shortModel = (model) => model.replace("gpt-5.6-", "");
  const colorStyle = (model) => `--model-color:${colorByModel.get(model)}`;

  function renderHeader() {
    $("#development-count").textContent = `${data.coverage.case_count} cases · ${data.coverage.attempt_count} runs`;
    $("#sealed-count").textContent = `${data.leaderboard.eligible_suite_count} eligible suites`;
    $("#data-version").textContent = `Data ${data.source_completed_at.slice(0, 10)} · ${data.data_sha256.slice(0, 10)}`;
  }

  function renderLegend() {
    const legend = $("#model-legend");
    data.models.forEach((model) => {
      const item = node("span", "legend-item");
      const mark = node("span", "legend-mark");
      mark.setAttribute("style", colorStyle(model));
      item.append(mark, document.createTextNode(model));
      legend.append(item);
    });
  }

  function renderSuiteChart() {
    const rows = data.experiment_suites.map((suite) => ({
      suite,
      summaries: data.suite_summaries.filter((item) => item.suite_id === suite.id),
    }));
    const allValues = rows.flatMap((row) => row.summaries.map((item) => item.mean_brier_loss));
    const maxValue = Math.max(0.1, ...allValues);
    const axisMax = Math.ceil(maxValue / 0.05) * 0.05;
    const width = 920;
    const left = 142;
    const right = 52;
    const top = 42;
    const groupHeight = 82;
    const height = top + rows.length * groupHeight + 46;
    const plotWidth = width - left - right;
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", "三个模型在纳入雷达的实验套件上的平均 Brier loss；越低越好。");

    for (let index = 0; index <= 5; index += 1) {
      const value = axisMax * index / 5;
      const x = left + plotWidth * index / 5;
      const line = document.createElementNS(svg.namespaceURI, "line");
      line.setAttribute("x1", x); line.setAttribute("x2", x);
      line.setAttribute("y1", top - 14); line.setAttribute("y2", height - 32);
      line.setAttribute("class", index === 0 ? "chart-axis" : "chart-grid");
      svg.append(line);
      const label = document.createElementNS(svg.namespaceURI, "text");
      label.setAttribute("x", x); label.setAttribute("y", 17);
      label.setAttribute("class", "chart-tick"); label.setAttribute("text-anchor", index === 0 ? "start" : "middle");
      label.textContent = value.toFixed(2);
      svg.append(label);
    }

    rows.forEach((row, rowIndex) => {
      const yBase = top + rowIndex * groupHeight;
      const label = document.createElementNS(svg.namespaceURI, "text");
      label.setAttribute("x", 0); label.setAttribute("y", yBase + 28);
      label.setAttribute("class", "chart-label");
      label.textContent = `${row.suite.title}  ·  ${row.suite.case_count}`;
      svg.append(label);
      row.summaries.forEach((summary, modelIndex) => {
        const y = yBase + 8 + modelIndex * 15;
        const rect = document.createElementNS(svg.namespaceURI, "rect");
        rect.setAttribute("x", left); rect.setAttribute("y", y);
        rect.setAttribute("width", Math.max(1, plotWidth * summary.mean_brier_loss / axisMax));
        rect.setAttribute("height", 7);
        rect.setAttribute("fill", colorByModel.get(summary.model));
        rect.setAttribute("opacity", "0.78");
        svg.append(rect);
        const value = document.createElementNS(svg.namespaceURI, "text");
        value.setAttribute("x", Math.min(width - 34, left + plotWidth * summary.mean_brier_loss / axisMax + 7));
        value.setAttribute("y", y + 7); value.setAttribute("class", "chart-value");
        value.textContent = format(summary.mean_brier_loss);
        svg.append(value);
      });
    });
    $("#suite-chart").append(svg);
  }

  function renderFamilyMatrix() {
    const wrap = $("#family-matrix");
    const table = node("table", "family-table");
    const head = node("thead");
    const headRow = node("tr");
    headRow.append(node("th", "", "逻辑族"));
    data.models.forEach((model) => headRow.append(node("th", "", model)));
    head.append(headRow);
    table.append(head);
    const body = node("tbody");
    const families = [...new Map(data.family_summaries.map((item) => [item.family, item.family_label])).entries()];
    families.forEach(([family, label]) => {
      const row = node("tr");
      row.append(node("td", "", label));
      data.models.forEach((model) => {
        const summary = data.family_summaries.find((item) => item.family === family && item.model === model);
        const cell = node("td");
        const value = node("span", "matrix-value");
        const bar = node("span", "matrix-bar");
        bar.setAttribute("style", `${colorStyle(model)};--bar-width:${Math.min(44, Math.max(2, summary.mean_brier_loss * 120))}px`);
        value.append(bar, document.createTextNode(format(summary.mean_brier_loss)));
        cell.append(value);
        cell.title = `${label} · ${model} · accuracy ${percent(summary.accuracy)} · n=${summary.completed_count}`;
        row.append(cell);
      });
      body.append(row);
    });
    table.append(body);
    wrap.append(table);
  }

  function renderCoverage() {
    const coverage = $("#coverage-metrics");
    const metrics = [
      ["A-share cases", data.coverage.case_count],
      ["Event / no event", `${data.coverage.event_count} / ${data.coverage.no_event_count}`],
      ["Models", data.coverage.model_count],
      ["Completed attempts", data.model_summaries.reduce((sum, item) => sum + item.completed_count, 0)],
      ["Search coverage", percent(Math.min(...data.model_summaries.map((item) => item.search_coverage)))],
      ["Repeats / case", Math.max(...data.experiment_suites.map((item) => item.repeats))],
    ];
    metrics.forEach(([label, value]) => {
      const row = node("div"); row.append(node("dt", "", label), node("dd", "", String(value))); coverage.append(row);
    });
  }

  function renderModelSummary() {
    const target = $("#model-summary");
    [...data.model_summaries].sort((a, b) => a.mean_brier_loss - b.mean_brier_loss).forEach((summary) => {
      const item = node("div", "model-summary-item");
      const name = node("div", "model-name");
      const dot = node("span", "model-dot"); dot.setAttribute("style", colorStyle(summary.model));
      name.append(dot, document.createTextNode(summary.model));
      const score = node("div", "summary-row");
      score.append(node("span", "summary-label", "Mean Brier"));
      const scoreValue = node("span", "summary-value"); scoreValue.innerHTML = `<strong>${format(summary.mean_brier_loss)}</strong> ↓`;
      score.append(scoreValue);
      const accuracy = node("div", "summary-row");
      accuracy.append(node("span", "summary-label", "Accuracy"), node("span", "summary-value", percent(summary.accuracy)));
      item.append(name, score, accuracy); target.append(item);
    });
  }

  function renderIdentity() {
    const target = $("#experiment-identity");
    data.experiment_suites.forEach((suite) => {
      const item = node("div", "identity-item");
      item.append(node("div", "identity-title", suite.title));
      const meta = node("p", "identity-meta");
      meta.append(document.createTextNode(`${suite.harness.version} · ${suite.reasoning_effort} · `));
      const hash = node("span", "identity-hash", suite.case_suite_sha256.slice(0, 12));
      hash.title = suite.case_suite_sha256;
      meta.append(hash);
      item.append(meta); target.append(item);
    });
  }

  function populateFilters() {
    const familySelect = $("#family-filter");
    [...new Map(data.cases.map((item) => [item.family, item.family_label])).entries()].forEach(([value, label]) => {
      const option = node("option", "", label); option.value = value; familySelect.append(option);
    });
    const modelSelect = $("#model-filter");
    data.models.forEach((model) => { const option = node("option", "", model); option.value = model; modelSelect.append(option); });
  }

  function caseDifficulty(item) {
    const losses = item.runs.filter((run) => run.status === "completed").map((run) => run.brier_loss);
    return losses.reduce((sum, value) => sum + value, 0) / losses.length;
  }

  function renderCases() {
    const query = state.query.trim().toLocaleLowerCase("zh-CN");
    const filtered = data.cases.filter((item) => {
      const matchesFamily = state.family === "all" || item.family === state.family;
      const haystack = `${item.company} ${item.ticker} ${item.family_label} ${item.id}`.toLocaleLowerCase("zh-CN");
      return matchesFamily && (!query || haystack.includes(query));
    });
    filtered.sort((a, b) => {
      if (state.sort === "as-of-desc") return b.as_of.localeCompare(a.as_of);
      if (state.sort === "as-of-asc") return a.as_of.localeCompare(b.as_of);
      return caseDifficulty(b) - caseDifficulty(a);
    });
    $("#case-result-count").textContent = `${filtered.length} / ${data.cases.length} cases`;
    const list = $("#case-list"); list.replaceChildren();
    if (!filtered.length) { list.append(node("p", "empty-list", "没有符合当前筛选的样例。")); return; }
    filtered.forEach((item) => {
      const row = node("article", "case-row");
      const identity = node("div");
      const company = node("div", "case-company", item.company);
      company.append(node("span", "case-ticker", item.ticker));
      const meta = node("p", "case-meta", `${item.family_label} · as-of ${item.as_of}`);
      const outcome = node("span", `case-outcome${item.outcome ? "" : " no-event"}`, item.outcome ? "EVENT" : "NO EVENT");
      outcome.title = item.target_definition;
      identity.append(company, meta, outcome);
      const runs = node("div", "case-runs");
      item.runs.filter((run) => state.model === "all" || run.model === state.model).forEach((run) => {
        const line = node("div", "case-run");
        line.append(node("span", "run-label", shortModel(run.model)));
        if (run.status === "completed") {
          const track = node("span", "probability-track");
          const marker = node("span", "probability-marker");
          marker.setAttribute("style", `${colorStyle(run.model)};--probability:${run.event_probability}`);
          marker.title = `${run.model}: P(event) ${percent(run.event_probability, 0)}`;
          track.append(marker); line.append(track);
          const value = node("span", "run-value");
          value.innerHTML = `<strong>${percent(run.event_probability)}</strong> · B ${format(run.brier_loss)}`;
          line.append(value);
        } else {
          line.append(node("span", "run-label", "failed"), node("span", "run-value", "—"));
        }
        runs.append(line);
      });
      row.append(identity, runs); list.append(row);
    });
  }

  function bindTabs() {
    const tabs = [$("#development-tab"), $("#sealed-tab")];
    tabs.forEach((tab) => tab.addEventListener("click", () => {
      tabs.forEach((item) => item.setAttribute("aria-selected", String(item === tab)));
      $("#development-view").hidden = tab.id !== "development-tab";
      $("#sealed-view").hidden = tab.id !== "sealed-tab";
    }));
  }

  const infoCopy = {
    brier: ["为什么用 Brier loss", [
      "Brier loss 是预测概率与实际二元结果之间的平方误差，0 最好、1 最差。它会同时惩罚判断方向错误和不恰当的过度自信。",
      "图中按公开历史任务切片展示平均值。现有结果每题只有一次运行，因此只能诊断，不能估计随机波动。",
    ]],
    families: ["如何阅读逻辑族", [
      "每个逻辑族至少包含一组具体预测合同，例如商誉减值阈值、ST 触发规则、业绩承诺缺口或研发商业兑现。",
      "同一模型跨列比较可以定位失分面；不同模型同列比较可以观察同类任务的相对差异。悬停单元格可查看 accuracy 与样本数。",
    ]],
    identity: ["实验身份与边界", [
      "每个结果文件记录模型、reasoning effort、harness 版本、只读 sandbox、语料边界和 case-suite SHA-256。页面数据还绑定原始 result 文件 SHA-256。",
      "历史 replay 使用截至 as-of 的冻结官方披露；结果对 agent 不可见。正式排名仍需未来题预注册、外部时间戳、重复运行和 verifier-owned resolution。",
    ]],
  };

  function bindInfo() {
    const layer = $("#info-layer"); const title = $("#info-title"); const content = $("#info-content"); const close = $("#info-close");
    const hide = () => {
      layer.hidden = true;
      if (lastInfoTrigger) {
        lastInfoTrigger.setAttribute("aria-expanded", "false");
        lastInfoTrigger.setAttribute("data-tooltip-suppressed", "");
        lastInfoTrigger.addEventListener(
          "blur",
          () => lastInfoTrigger?.removeAttribute("data-tooltip-suppressed"),
          { once: true },
        );
        lastInfoTrigger.focus();
      }
    };
    document.querySelectorAll("[data-info]").forEach((button) => button.addEventListener("click", () => {
      lastInfoTrigger = button; button.setAttribute("aria-expanded", "true");
      const [heading, paragraphs] = infoCopy[button.dataset.info]; title.textContent = heading; content.replaceChildren();
      paragraphs.forEach((copy) => content.append(node("p", "", copy)));
      const list = node("ul"); data.methodology.forEach((item) => list.append(node("li", "", item))); content.append(list);
      layer.hidden = false; close.focus();
    }));
    close.addEventListener("click", hide);
    layer.addEventListener("click", (event) => { if (event.target === layer) hide(); });
    document.addEventListener("keydown", (event) => { if (event.key === "Escape" && !layer.hidden) hide(); });
  }

  function bindControls() {
    $("#case-search").addEventListener("input", (event) => { state.query = event.target.value; renderCases(); });
    $("#family-filter").addEventListener("change", (event) => { state.family = event.target.value; renderCases(); });
    $("#model-filter").addEventListener("change", (event) => { state.model = event.target.value; renderCases(); });
    $("#case-sort").addEventListener("change", (event) => { state.sort = event.target.value; renderCases(); });
  }

  renderHeader();
  renderLegend();
  renderSuiteChart();
  renderFamilyMatrix();
  renderCoverage();
  renderModelSummary();
  renderIdentity();
  populateFilters();
  renderCases();
  bindTabs();
  bindInfo();
  bindControls();
}());
