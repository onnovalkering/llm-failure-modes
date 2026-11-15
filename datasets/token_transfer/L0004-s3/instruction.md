Below are facts about three tokens. `owns(X, t)` means X holds token t at step 0.
`transfers(X, t, Y)` at step n means X gives token t to Y at step n. The facts are listed
in random order; the step number gives the time order.

Who holds `red_token` after the last step?

Work this out by reading the facts yourself. Do not write or run scripts or programs to
compute the answer. Write only the name to `/app/answer.txt`.

```
step 8: transfers(Erin, blue_token, Carol)
step 11: transfers(Peggy, green_token, Erin)
step 0: owns(Bob, blue_token)
step 10: transfers(Carol, blue_token, Uma)
step 4: transfers(Ivan, red_token, Sybil)
step 3: transfers(Bob, red_token, Ivan)
step 1: transfers(Ivan, green_token, Heidi)
step 0: owns(Ivan, green_token)
step 2: transfers(Heidi, green_token, Mallory)
step 0: owns(Bob, red_token)
step 9: transfers(Frank, red_token, Wendy)
step 6: transfers(Mallory, green_token, Peggy)
step 7: transfers(Sybil, red_token, Frank)
step 12: transfers(Uma, blue_token, Olivia)
step 5: transfers(Bob, blue_token, Erin)
```
