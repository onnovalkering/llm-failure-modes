Below are facts about three tokens. `owns(X, t)` means X holds token t at step 0.
`transfers(X, t, Y)` at step n means X gives token t to Y at step n. The facts are listed
in random order; the step number gives the time order.

Who holds `red_token` after the last step?

Work this out by reading the facts yourself. Do not write or run scripts or programs to
compute the answer. Write only the name to `/app/answer.txt`.

```
step 0: owns(Dave, red_token)
step 7: transfers(Peggy, red_token, Bob)
step 3: transfers(Dave, red_token, Peggy)
step 0: owns(Judy, green_token)
step 2: transfers(Judy, green_token, Frank)
step 11: transfers(Niaj, green_token, Victor)
step 12: transfers(Mallory, red_token, Victor)
step 4: transfers(Frank, green_token, Carol)
step 9: transfers(Heidi, blue_token, Grace)
step 6: transfers(Carol, green_token, Niaj)
step 10: transfers(Grace, blue_token, Victor)
step 0: owns(Carol, blue_token)
step 1: transfers(Carol, blue_token, Bob)
step 5: transfers(Bob, blue_token, Heidi)
step 8: transfers(Bob, red_token, Mallory)
```
