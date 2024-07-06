During the Olympiad, the local television station is organizing a new live game. The organizers use a computer that generates and displays two numbers, `N1` and `N2`, on a screen.

Each contestant has a remote control with a single-digit display and certain buttons, as shown in the adjacent figure. The remote control also has a memory where the digits obtained by the contestants are stored in order.
\
~[afisaj.png]
\
The digits of the first number `N1` are successively displayed on each contestant's remote display from left to right. Contestants must transform the first number, obtaining in the memory of their remote the second number, using the buttons available on the remote. After performing an operation on the current digit (the one displayed), the next digit from `N1` automatically appears on the display (if any).

The effects of pressing the buttons are as follows:

- `+` followed by a digit - Generates the sum of the digit on the display and the pressed digit (operation only possible if the sum is still a digit). The sum digit is stored in memory.

$\\\\$

- `–` followed by a digit - Generates the difference between the digit on the display and the pressed digit (operation only possible if the result is still a digit). The obtained digit is stored in memory.

$\\\\$

- `*` followed by a digit - The value of the key actioned after the `*` key is stored in memory. Since no operation is performed on the current digit from `N1`, it does not disappear from the display.

$\\\\$

- `/` - The current digit from `N1` is deleted.

$\\\\$

- `#` - The current digit and all subsequent digits from `N1` up to the end are deleted.

$\\\\$

- `=` - The current digit is copied to memory.

$\\\\$

The action ends when all digits of `N1` have been processed. A solution is obtained when the memory of the remote contains the digits of the number `N2`. A solution is optimal if the number of button presses is minimal. The winners of the game are those contestants who find an optimal solution.

# Task

Given `N1` and `N2`, write a program that determines an optimal solution to transform the number `N1` into the number `N2`.

# Input data

The input file `telecomanda.in` contains the number `N1` on the first line and the number `N2` on the second line.

# Output data

The output file `telecomanda.out` contains two lines:

`min`\
$t_1t_2...t_{min}$

where `n` is a nonzero natural number representing the minimum number of button presses to transform `N1` into `N2`. $t_1t_2...t_{min}$ is a sequence of `min` characters representing the pressed buttons; no separators will be placed between characters.

# Constraints and clarifications

* `1 \leq number\ of\ digits\ of\ each\ number \leq 5000`
* The problem has been modified
* `30%` of the score is awarded for displaying the correct number of steps
* For `50%` of tests we have `1 \leq number\ of\ digits\ of\ each\ number \leq 100`

# Example

`telecomanda.in`
```
372
78
```

`telecomanda.out`
```
4
/=+6
```

Explanations
---

The optimal solution performs `4` steps.\
We skip the first digit of `N1` by pressing `/`, take the new current digit from `N1` by pressing `=` (obtaining `7` in memory), and then add `6` to the last digit of `N1` by pressing `+6` (obtaining `78` in memory), processing all digits of `N1` and obtaining `N2`.\
Other solutions would be `/=*8/`, `+4+1/`, `+4+1#`, or `*7*8#`, which have `5` steps and are not optimal.