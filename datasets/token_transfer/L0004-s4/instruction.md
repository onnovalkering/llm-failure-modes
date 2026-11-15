Below are facts about three tokens. `owns(X, t)` means X holds token t at step 0.
`transfers(X, t, Y)` at step n means X gives token t to Y at step n. The facts are listed
in random order; the step number gives the time order.

Who holds `red_token` after the last step?

Work this out by reading the facts yourself. Do not write or run scripts or programs to
compute the answer. Write only the name to `/app/answer.txt`.

```
step 0: owns(Dave, red_token)
step 3: transfers(Dave, red_token, Heidi)
step 1: transfers(Sybil, blue_token, Ivan)
step 0: owns(Alice, green_token)
step 2: transfers(Ivan, blue_token, Alice)
step 8: transfers(Olivia, green_token, Alice)
step 5: transfers(Alice, blue_token, Rupert)
step 12: transfers(Trent, red_token, Peggy)
step 9: transfers(Rupert, blue_token, Ivan)
step 0: owns(Sybil, blue_token)
step 11: transfers(Alice, green_token, Grace)
step 6: transfers(Niaj, green_token, Olivia)
step 4: transfers(Alice, green_token, Niaj)
step 7: transfers(Heidi, red_token, Grace)
step 10: transfers(Grace, red_token, Trent)
```
