#!/bin/bash
# Reward 1 if /app/answer.txt names the correct final holder, else 0.
mkdir -p /logs/verifier
answer="$(tr -d '[:space:]' < /app/answer.txt 2>/dev/null)"
if [ "$answer" = "Frank" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
