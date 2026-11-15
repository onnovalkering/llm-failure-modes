# LLM failure modes experiments


## Instruction count
```
python ./experiments/instruction_count/generate.py \
  --counts 32 64 128 256 512 768 1024 \ 
  --seeds 0 1 2
```

### Experiment validation
```
PYTHONPATH=. harbor run \
  --agent opencode \
  --model openrouter/anthropic/claude-haiku-5.5 \
  --path datasets/instruction_count \
  --n-concurrent 4  \
  --plugin plugins.reward_matrix:RewardMatrixPlugin \
  --ak 'opencode_config={"snapshot": false}'
```

### Experiment 
```
PYTHONPATH=. harbor run \
  --agent opencode \
  --model openrouter/google/gemma-4-26b-a4b-it \
  --model openrouter/openai/gpt-oss-20b \
  --model openrouter/qwen/qwen3.5-35b-a3b \
  --model openrouter/mistralai/ministral-8b-2512 \
  --path datasets/instruction_count \
  --n-concurrent 4 \
  --plugin plugins.reward_matrix:RewardMatrixPlugin \
  --ak 'opencode_config={"snapshot": false}'
```

### Reference
```
PYTHONPATH=. harbor run \
  --agent opencode \
  --model openrouter/google/gemini-3.1-flash-lite \
  --path datasets/instruction_count \
  --n-concurrent 4  \
  --plugin plugins.reward_matrix:RewardMatrixPlugin \
  --ak 'opencode_config={"snapshot": false}'
```

## Maze navigation
```
python ./experiments/maze_navigation/generate.py \
  --steps 4 8 12 16 24 32 64 \
  --seeds 0 1 2
```

### Experiment validation
```
PYTHONPATH=. harbor run \
  --agent opencode \
  --model openrouter/anthropic/claude-haiku-5.5 \
  --path datasets/maze_navigation \
  --n-concurrent 4 \
  --plugin plugins.reward_matrix:RewardMatrixPlugin \
  --plugin plugins.maze_plot:MazePlotPlugin \
  --ak 'opencode_config={"snapshot": false}'
```

### Experiment 
```
PYTHONPATH=. harbor run \
  --agent opencode \
  --model openrouter/google/gemma-4-26b-a4b-it \
  --model openrouter/openai/gpt-oss-20b \
  --model openrouter/qwen/qwen3.5-35b-a3b \
  --model openrouter/mistralai/ministral-8b-2512 \
  --path datasets/maze_navigation \
  --n-concurrent 4 \
  --plugin plugins.reward_matrix:RewardMatrixPlugin \
  --plugin plugins.maze_plot:MazePlotPlugin \
  --ak 'opencode_config={"snapshot": false}'
```

### Reference
```
PYTHONPATH=. harbor run \
  --agent opencode \
  --model openrouter/google/gemini-3.1-flash-lite \
  --path datasets/maze_navigation \
  --n-concurrent 4 \
  --plugin plugins.reward_matrix:RewardMatrixPlugin \
  --plugin plugins.maze_plot:MazePlotPlugin \
  --ak 'opencode_config={"snapshot": false}'
```

## Token transfer
Three tokens change hands through step-numbered `transfers(X, t, Y)` facts listed in shuffled order; the
model must report who holds `red_token` after the last step. `L` is the number of transfers per token.
Task names stay `ktai/e3-...` (E3 in the report); `manifest.json` holds the ground truth per task.

```
python ./experiments/token_transfer/generate.py \
  --levels 4 16 32 64 128 256 \
  --seeds 1 2 3 4 5
```

### Experiment validation
```
harbor run --path datasets/token_transfer --agent oracle
```

### Experiment
```
PYTHONPATH=. harbor run \
  --agent opencode \
  --model openrouter/google/gemma-4-26b-a4b-it \
  --model openrouter/openai/gpt-oss-20b \
  --model openrouter/mistralai/ministral-8b-2512 \
  --path datasets/token_transfer \
  --plugin plugins.reward_matrix:RewardMatrixPlugin \
  --ak version=1.19.5 \
  --ak disable_web_search=true
```

### Reference
```
PYTHONPATH=. harbor run \
  --agent opencode \
  --model openrouter/google/gemini-3.1-flash-lite \
  --path datasets/token_transfer \
  --plugin plugins.reward_matrix:RewardMatrixPlugin \
  --ak version=1.19.5 \
  --ak disable_web_search=true
```

### Results
One valid trial per model per task (120 in total); trials that failed outside the model (credit, rate
limit, provider errors) were re-run. Qwen3.5 35B-A3B was not run on this experiment. Per-trial data is in
`results/token_transfer/token_transfer_trials.csv`; the figures are rebuilt with:
```
uv run --no-project --with matplotlib python ./experiments/token_transfer/plot.py
```
