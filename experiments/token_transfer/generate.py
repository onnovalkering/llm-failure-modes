"""Generate E3 token-transfer tasks for Harbor.

Each task lists the transfers of three tokens (one target, two distractors) as
step-numbered facts in shuffled order. The model must report who holds the
target token after the last step. Difficulty knob: L, the number of transfers
per token. A seed is a new task instance.

Usage: python ./experiments/token_transfer/generate.py --levels 4 16 32 64 128 256 --seeds 1 2 3 4 5
Writes datasets/token_transfer/L<L>-s<seed>/ and datasets/token_transfer/manifest.json
(ground truth and the answer of the 'last receiver of the target in the listing' heuristic).
The task names stay `ktai/e3-...` because the report calls this experiment E3.
"""
import argparse, json, random, shutil
from pathlib import Path

NAMES = ["Alice", "Bob", "Carol", "Dave", "Erin", "Frank", "Grace", "Heidi",
         "Ivan", "Judy", "Mallory", "Niaj", "Olivia", "Peggy", "Rupert", "Sybil",
         "Trent", "Uma", "Victor", "Wendy"]
TOKENS = ["red_token", "green_token", "blue_token"]  # first one is the target
HERE = Path(__file__).resolve().parent
TEMPLATE_PATH = HERE / "template"

def make_instance(L, seed):
    rng = random.Random(seed * 100_003 + L)
    facts, holders = [], {}
    for tok in TOKENS:
        holders[tok] = rng.choice(NAMES)
        facts.append((0, f"owns({holders[tok]}, {tok})"))
    events = [tok for tok in TOKENS for _ in range(L)]
    rng.shuffle(events)  # interleave the three chains in time
    for step, tok in enumerate(events, start=1):
        giver = holders[tok]
        receiver = rng.choice([n for n in NAMES if n != giver])
        holders[tok] = receiver
        facts.append((step, f"transfers({giver}, {tok}, {receiver})"))
    listing = facts[:]
    rng.shuffle(listing)  # listing order is not time order
    lines = [f"step {s}: {f}" for s, f in listing]
    target = TOKENS[0]
    last_listed = next(f for _, f in reversed(listing) if target in f and f.startswith("transfers"))
    heuristic = last_listed.rstrip(")").split(", ")[-1]
    return lines, holders[target], heuristic

INSTRUCTION = """Below are facts about three tokens. `owns(X, t)` means X holds token t at step 0.
`transfers(X, t, Y)` at step n means X gives token t to Y at step n. The facts are listed
in random order; the step number gives the time order.

Who holds `red_token` after the last step?

Work this out by reading the facts yourself. Do not write or run scripts or programs to
compute the answer. Write only the name to `/app/answer.txt`.

```
{facts}
```
"""

TEST = """#!/bin/bash
mkdir -p /logs/verifier
answer="$(tr -d '[:space:]' < /app/answer.txt 2>/dev/null)"
if [ "$answer" = "{answer}" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--levels", type=int, nargs="+", default=[4, 16, 64, 256])
    ap.add_argument("--seeds", type=int, nargs="+", default=[1, 2, 3])
    ap.add_argument("--out", type=Path, default=Path("datasets/token_transfer"))
    args = ap.parse_args()
    template = TEMPLATE_PATH
    out = args.out
    shutil.rmtree(out, ignore_errors=True)
    manifest = {}
    for L in args.levels:
        for s in args.seeds:
            name = f"L{L:04d}-s{s}"
            d = out / name
            shutil.copytree(template, d)
            lines, answer, heuristic = make_instance(L, s)
            (d / "instruction.md").write_text(INSTRUCTION.format(facts="\n".join(lines)))
            (d / "tests" / "test.sh").write_text(TEST.format(answer=answer))
            (d / "solution" / "solve.sh").write_text(f"#!/bin/bash\necho {answer} > /app/answer.txt\n")
            toml = (d / "task.toml").read_text()
            toml = toml.replace('name = "ktai/smoke-token-transfer"', f'name = "ktai/e3-{name}"')
            toml = toml.replace('description = "Smoke test: who holds the token after 5 transfers"',
                                f'description = "E3 token transfer, L={L}, seed={s}"')
            (d / "task.toml").write_text(toml)
            manifest[name] = {"L": L, "seed": s, "answer": answer, "heuristic_last_listed": heuristic}
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2))
    print(f"wrote {len(manifest)} tasks to {out}")

if __name__ == "__main__":
    main()
