Below are facts about three tokens. `owns(X, t)` means X holds token t at step 0.
`transfers(X, t, Y)` at step n means X gives token t to Y at step n. The facts are listed
in random order; the step number gives the time order.

Who holds `red_token` after the last step?

Work this out by reading the facts yourself. Do not write or run scripts or programs to
compute the answer. Write only the name to `/app/answer.txt`.

```
step 2: transfers(Dave, blue_token, Judy)
step 1: transfers(Grace, blue_token, Dave)
step 7: transfers(Sybil, blue_token, Rupert)
step 10: transfers(Trent, red_token, Dave)
step 12: transfers(Wendy, red_token, Mallory)
step 3: transfers(Judy, blue_token, Sybil)
step 0: owns(Grace, blue_token)
step 8: transfers(Olivia, green_token, Judy)
step 0: owns(Trent, green_token)
step 5: transfers(Trent, green_token, Wendy)
step 0: owns(Victor, red_token)
step 11: transfers(Dave, red_token, Wendy)
step 6: transfers(Wendy, green_token, Olivia)
step 4: transfers(Victor, red_token, Trent)
step 9: transfers(Judy, green_token, Wendy)
```
