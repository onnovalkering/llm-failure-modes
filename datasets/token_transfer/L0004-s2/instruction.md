Below are facts about three tokens. `owns(X, t)` means X holds token t at step 0.
`transfers(X, t, Y)` at step n means X gives token t to Y at step n. The facts are listed
in random order; the step number gives the time order.

Who holds `red_token` after the last step?

Work this out by reading the facts yourself. Do not write or run scripts or programs to
compute the answer. Write only the name to `/app/answer.txt`.

```
step 10: transfers(Judy, blue_token, Bob)
step 5: transfers(Ivan, red_token, Sybil)
step 4: transfers(Mallory, blue_token, Alice)
step 3: transfers(Rupert, green_token, Heidi)
step 1: transfers(Carol, red_token, Ivan)
step 2: transfers(Ivan, green_token, Rupert)
step 7: transfers(Sybil, red_token, Dave)
step 0: owns(Ivan, green_token)
step 9: transfers(Dave, red_token, Bob)
step 6: transfers(Heidi, green_token, Carol)
step 0: owns(Carol, red_token)
step 0: owns(Mallory, blue_token)
step 8: transfers(Alice, blue_token, Judy)
step 12: transfers(Bob, blue_token, Alice)
step 11: transfers(Carol, green_token, Sybil)
```
