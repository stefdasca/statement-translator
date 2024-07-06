Sure, here is the translation of the provided programming problem statement:

---

Fan of the Countdown game, especially of the numbers round, Sean wants to use his computer science knowledge. He recalls the rules for those who don't watch the show:
- The game contains two sets of numbers: one with large numbers (`25, 50, 75` and `100`) and one with small numbers, each number from `1` to `10` appearing `2` times (`1, 1, 2, 2, ..., 10, 10`)
- The contestant chooses a total of `6` numbers: between `0` and `4` numbers from the large set and the rest up to `6` from the small numbers set
- Using basic arithmetic operations ($ +, -, *, / $) and some of the chosen numbers, the contestant must obtain a random `3` digit number
- The solution must not contain a fraction or a negative number at any step

Sean chooses a set of `6` numbers according to the rules and asks himself `m` questions: if it is possible to obtain the number `x`, what is the minimum number of numbers needed to obtain it?

# Input data
The first line contains the `6` numbers that Sean can use. Then, the next line contains the number `m`, followed by one line for each question, `x`.

# Output data
For each question, print on each line the minimum number of numbers used, followed by the operations performed. If it is not possible to obtain the required number, print `"IMPOSSIBLE"`.

# Constraints and clarifications
* `1 \ \leq m \ \leq 1\ 000`
* Any correct solution will be accepted
* The expression will not contain spaces

# Example

`stdin`
```
1 2 3 4 25 50
3
102
660
991
```

`stdout`
```
3 (1+50)*2
6 (1+4+25)*(50/2-3)
IMPOSSIBLE
```

---

Please review for any grammar or syntax errors.