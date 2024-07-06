Parents of Gigel gave him a peculiar mobile phone as a birthday gift. Happy, Gigel wants to ensure he is not late for his first class tomorrow to show his friends the new mobile as soon as possible. However, he has difficulty waking up in the morning. Fortunately, the mobile phone has an alarm. To set the alarm time, the data must be entered in the "hour and minute" format $\text{HHMM}$ (exactly $4$ digits). The first $2$ digits represent the hour, and the last two digits represent the minutes. Gigel noticed that if he enters the hour $74$, the screen displays $02$, which is the remainder when divided by $24$. Similarly, if he enters $84$ as minutes, the screen will show $24$ (the remainder when divided by $60$). If Gigel wants to wake up at $0826$ (8 hours and 26 minutes), he can enter $0826$ or $5686$.
~[alarma.png|align=right]
The arrangement of the $10$ keys corresponding to the digits $0, 1, ..., 9$ is special, as there are many other keys on the mobile, and the digits are arranged randomly. For example, if the keys on Gigel's mobile are arranged in $5$ rows and $6$ columns, numbered from $1$ to $5$ and $1$ to $6$, respectively, then he could have the numeric keys arranged as in the adjacent figure.
To set the alarm, Gigel wants to consume as few calories as possible. The number of calories consumed to move a finger from key $A$, located at row $x_A$ and column $y_A$, to key $B$, located at row $x_B$ and column $y_B$, is calculated using the formula:
$$\text{Calories}(A, B) = |x_A - x_B| + |y_A - y_B|$$
If the keys are arranged as in the figure above and considering that the key $1$ is at row $1$ and column $1$, to type $5686$, Gigel will consume $11$ calories, as follows:
$$\text{Calories}(5, 6) + \text{Calories}(6, 8) + \text{Calories}(8,6) = (|5 - 2| + |1 - 3|) + (|2 - 1| + |3 - 5|) + (|1 - 2| + |5 - 3|) =$$
$$= (3 + 2) + (1 + 2) + (1 + 2) = 11$$

# Task

Given the coordinates of the keys corresponding to the digits from $0$ to $9$ and the time Gigel wants to wake up, write a program that determines the $4$ digits that must be typed so that the number of calories consumed is minimal. If there are multiple solutions, the one for which the typed number is minimal should be displayed.

# Input data

The first $10$ lines of the input file `alarma.in` contain pairs of non-zero natural numbers, $x_i \ y_i$, separated by a space, representing the coordinates of the numeric key corresponding to digit $i, 0 \leq i \leq 9$, in increasing order of the values of the digits on the keys. The eleventh line contains $4$ digits representing the time when Gigel wants to wake up, in the format $\text{HHMM}$.

# Output data

The output file `alarma.out` should display on the first line a natural number representing the minimum number of calories consumed, and on the second line, the four digits the user must press to set the alarm.

# Constraints and clarifications

* The coordinates $x_i$ and $y_i$ of a key represent the row and respectively the column where the numeric key $i$ is located.
* $1 \leq x_i \leq 99; 1 \leq y_i \leq 99$ for any value of $i$ from $0$ to $9$.
* $0 \leq \text{the number represented by the first two digits HH is natural} \leq 23$
* $0 \leq \text{the number represented by the last two digits MM is natural} \leq 59$
* For correctly determining the minimum number of calories consumed, $40\%$ of the score is granted, and for correctly determining the $4$ pressed digits, $60\%$ of the score is granted.

# Example

`alarma.in`
```
1 2
71 1
18 25
12 2
82 73
3 1
52 3
3 35
2 54
1 93
0124
```

`alarma.out`
```
179
9784
```

## Explanation

$$\text{Calories}(9, 7) + \text{Calories}(7, 8) + \text{Calories}(8, 4) = (|3 - 1| + |93 - 35|) + (|3 - 2| + |54 - 35|) + (|82 - 2| + |73 - 54|) = 2 + 58 + 1 + 19 + 80 + 19 = 179$$

