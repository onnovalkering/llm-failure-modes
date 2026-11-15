"""Plot the token-transfer (E3) results from results/token_transfer/token_transfer_trials.csv.

Usage: uv run --no-project --with matplotlib python ./experiments/token_transfer/plot.py
Writes results/token_transfer/token_transfer_accuracy.pdf and token_transfer_outcomes.pdf.
"""
import csv
from collections import defaultdict
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parents[2] / "results" / "token_transfer"
rows = list(csv.DictReader(open(OUT / "token_transfer_trials.csv")))

# Fixed categorical order (colour follows the model, never its rank).
# Qwen has no E3 runs; Gemini takes the fourth (amber) slot of the existing palette.
MODELS = ["google/gemini-3.1-flash-lite", "openai/gpt-oss-20b", "google/gemma-4-26b-a4b-it",
          "mistralai/ministral-8b-2512"]
LABEL = {"google/gemini-3.1-flash-lite": "Gemini 3.1 Flash Lite (ref.)", "openai/gpt-oss-20b": "gpt-oss-20b",
         "google/gemma-4-26b-a4b-it": "Gemma 4 26B-A4B", "mistralai/ministral-8b-2512": "Ministral 8B"}
COLOR = {"google/gemini-3.1-flash-lite": "#eda100", "openai/gpt-oss-20b": "#2a78d6",
         "google/gemma-4-26b-a4b-it": "#eb6834", "mistralai/ministral-8b-2512": "#1baf7a"}
MARKER = {"google/gemini-3.1-flash-lite": "D", "openai/gpt-oss-20b": "o",
          "google/gemma-4-26b-a4b-it": "s", "mistralai/ministral-8b-2512": "^"}
rows = [r for r in rows if r["model"] in MODELS]
MODELS = [m for m in MODELS if any(r["model"] == m for r in rows)]
INK, MUTED, GRID = "#0b0b0b", "#52514e", "#e4e3df"

plt.rcParams.update({"font.size": 9, "axes.edgecolor": MUTED, "axes.labelcolor": INK,
                     "xtick.color": MUTED, "ytick.color": MUTED, "axes.spines.top": False,
                     "axes.spines.right": False})

acc = defaultdict(list)
for r in rows:
    acc[(r["model"], int(r["L"]))].append(float(r["reward"]))
levels = sorted({int(r["L"]) for r in rows})

# Figure 1: accuracy against chain length.
fig, ax = plt.subplots(figsize=(4.6, 2.4))
offsets = dict(zip(MODELS, [-0.18, -0.06, 0.06, 0.18][:len(MODELS)]))  # small x-jitter so overlapping points stay visible
for m in MODELS:
    xs = [L * 2 ** offsets[m] for L in levels if acc.get((m, L))]
    ys = [sum(acc[(m, L)]) / len(acc[(m, L)]) for L in levels if acc.get((m, L))]
    ax.plot(xs, ys, color=COLOR[m], lw=1.5, marker=MARKER[m], ms=5, mec="white", mew=1, label=LABEL[m])
ax.set_xscale("log", base=2)
ax.set_xticks(levels, [str(L) for L in levels])
ax.minorticks_off()
ax.set_ylim(-0.05, 1.05)
ax.set_yticks([0, 0.5, 1], ["0", "0.5", "1"])
ax.set_xlabel("Transfers per token (L)")
ax.set_ylabel("Accuracy")
ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)
ax.legend(frameon=False, fontsize=7.5, loc="center left", bbox_to_anchor=(1.0, 0.5), labelcolor=INK)
fig.tight_layout()
fig.savefig(OUT / "token_transfer_accuracy.pdf", dpi=200)

# Figure 2: how each trial ended, per model (all levels pooled).
def outcome(r):
    if float(r["reward"]) == 1.0: return "Correct"
    if r["exception"]: return "Time-out"
    return "Wrong holder"
CATS = ["Correct", "Wrong holder", "Time-out"]
SHADE = {"Correct": "#3b3a37", "Wrong holder": "#8f8e88", "Time-out": "#d3d2cc"}
counts = {m: {c: 0 for c in CATS} for m in MODELS}
scripts = defaultdict(int)
for r in rows:
    counts[r["model"]][outcome(r)] += 1
    scripts[r["model"]] += r["used_script"] == "True"

fig, ax = plt.subplots(figsize=(4.6, 2.0))
for i, m in enumerate(reversed(MODELS)):
    left = 0
    for c in CATS:
        n = counts[m][c]
        if n:
            ax.barh(i, n, left=left, height=0.62, color=SHADE[c], edgecolor="white", linewidth=2 if n > 1 else 0.5)
        if n > 1:
            ax.text(left + n / 2, i, str(n), ha="center", va="center", fontsize=7.5,
                    color="white" if c != "Time-out" else INK)
        left += n
    ax.text(left + 0.4, i, (f"{scripts[m]} used a script" if scripts[m] == 1 else f"{scripts[m]} used scripts") if scripts[m] else "", va="center",
            fontsize=7, color=MUTED)
ax.set_yticks(range(len(MODELS)), [LABEL[m] for m in reversed(MODELS)])
ax.set_xlim(0, max(sum(v.values()) for v in counts.values()) + 12)
ax.set_xlabel("Trials (all levels)")
ax.tick_params(axis="y", length=0)
handles = [plt.Rectangle((0, 0), 1, 1, color=SHADE[c]) for c in CATS]
ax.legend(handles, CATS, frameon=False, fontsize=7, ncol=3, loc="lower center",
          bbox_to_anchor=(0.35, 1.0), handlelength=1, columnspacing=1)
fig.tight_layout()
fig.savefig(OUT / "token_transfer_outcomes.pdf", dpi=200)
print("wrote", OUT / "token_transfer_accuracy.pdf", OUT / "token_transfer_outcomes.pdf")
