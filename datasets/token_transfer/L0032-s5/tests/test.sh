#!/bin/bash
mkdir -p /logs/verifier
answer="$(tr -d '[:space:]' < /app/answer.txt 2>/dev/null)"
if [ "$answer" = "Trent" ]; then echo 1 > /logs/verifier/reward.txt; else echo 0 > /logs/verifier/reward.txt; fi
