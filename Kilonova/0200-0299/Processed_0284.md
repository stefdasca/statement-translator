~[circular.jpg|align=right|width=20em]
A circular printer has capital letters of the English alphabet arranged in a circle from $A$ to $Z$. The printer has an indicator initially placed at the letter $A$.
To print a letter, the printer's indicator moves left or right. Moving the indicator to an adjacent letter either to the left or right of the current letter takes one second. For example, to print the string $BCY$, it takes $6$ seconds. The printer will always choose the direction that minimizes the movement time.
The printer prints letters in two colors: red or blue. Some letters are printed with red ink, and the rest with blue ink. For simplicity, we will call them red letters and blue letters.
Given a string of blue letters that are not necessarily distinct and the set of red letters of the printer, calculate:
1. The time it takes to print the string of blue letters on the circular printer.
2. Insert a red letter between any two consecutive blue letters to obtain the minimum printing time and display:
   * the minimum time;
   * the number of distinct strings that are printed with the minimum time;
   * the lexicographically smallest string among all strings that are printed in this time.

# Input data
The file `circular.in` contains:
1. The first line contains a natural number $c$ with possible values $1$ or $2$ representing the task;
2. The second line contains a string of blue letters, not necessarily distinct;
3. The third line contains the set of distinct red letters in alphabetical order.

# Output data
The file `circular.out` will display depending on the task:
* If $c = 1$, a single natural number representing the time required to print the string of blue letters on the printer.
* If $c = 2$, it will print three results, each on a separate line:
  * the minimum printing time according to the second requirement;
  * the number of distinct strings printed in minimum time $\\text{modulo }666\\ 013$;
  * the lexicographically smallest string that achieves this time.

# Constraints and clarifications
* The two strings contain only capital letters of the English alphabet.
* The length of the string of blue letters does not exceed $50\\ 000$ letters.
* The set of red letters does not exceed $25$ letters, which are distinct and shown in alphabetical order.
* All other letters that are not in the set of red letters are blue.
* For the case $c = 2$, partial marks are awarded as follows:
  * $25\\%$ of the score for displaying the minimum time;
  * $25\\%$ of the score for displaying the number of strings that achieve the minimum time;
  * $50\\%$ of the score for displaying the lexicographically smallest string.
* **Attention!** To obtain points for the second task, for any test, there must be exactly three lines in the output file that follow the required format.
* Task 1 is worth 24 points, and Task 2 is worth 76 points.

# Example 1
`circular.in`
```
1
BBTH
AEIOU
```

`circular.out`
```
21
```
## Explanation
The printing time of the string $\\color{blue} BBTH$ is $21$ and is obtained as follows:
* from $A$ to $B = 1$ second
* from $B$ to $B = 0$ seconds
* from $B$ to $T = 8$ seconds
* from $T$ to $H = 12$ seconds

# Example 2
`circular.in`
```
2
BBTH
AEIOU
```

`circular.out`
```
23
4
BABATIH
```
## Explanation
The minimum printing time on the printer is $23$ and is obtained for the string $\\color{blue}B \\color{red}A \\color{blue}B \\color{red}A \\color{blue}T \\color{red}I \\color{blue}H$ as follows:
* from $A$ to $B = 1$ second
* from $B$ to $A = 1$ second
* from $A$ to $B = 1$ second
* from $B$ to $A = 1$ second
* from $A$ to $T = 7$ seconds
* from $T$ to $I = 11$ seconds
* from $I$ to $H = 1$ second

In total $23$ seconds.
There are $4$ strings that achieve the minimum printing time: $\\color{blue}B \\color{red}A \\color{blue}B \\color{red}A \\color{blue}T \\color{red}I \\color{blue}H$, $\\color{blue}B \\color{red}A \\color{blue}B \\color{red}A \\color{blue}T \\color{red}O \\color{blue}H$, $\\color{blue}B \\color{red}A \\color{blue}B \\color{red}U \\color{blue}T \\color{red}I \\color{blue}H$, $\\color{blue}B \\color{red}A \\color{blue}B \\color{red}U \\color{blue}T \\color{red}O \\color{blue}H$.
The lexicographically first solution is $\\color{blue}B \\color{red}A \\color{blue}B \\color{red}A \\color{blue}T \\color{red}I \\color{blue}H$.

# Example 3
`circular.in`
```
2
AMYMAMAMY
BCDEFGHIJKLNOPQRSTUVWX
```

`circular.out`
```
96
568708
ABMNYNMBABMBABMNY
```
## Explanation
The minimum printing time is $96$.
There are $214\\ 358\\ 881$ distinct strings, and $214\\ 358\\ 881 \\text{ modulo } 666\\ 013 = 568\\ 708$.
The lexicographically first solution is $\\color{blue}A \\color{red}B \\color{blue}M \\color{red}N \\color{blue}Y \\color{red}N \\color{blue}M \\color{red}B \\color{blue}A \\color{red}B \\color{blue}M \\color{red}B \\color{blue}A \\color{red}B \\color{blue}M \\color{red}N \\color{blue}Y$.