~[chibrituri.png|align=right|width=20%]

Gigel, a 5th-grade student, loves to play with numbers and creates all kinds of problems that he then tries to solve. Now he is playing with a box of matches and uses them to form digits. Then, his gaze fell on the face of a digital clock, and he noticed that the digits are made up of horizontal and vertical segments, and he started forming the digits that indicate the time with matches (see the figure).

And immediately, he asked himself: "What is the minimum possible time I can form with $n$ vertical matches and $m$ horizontal matches?"

# Task

Given a number $n$ of vertical matches and a number $m$ of horizontal matches, write a program that determines the number of possible hours, the minimum hour, and the maximum hour that can be formed with these matches, in the way indicated above, using all the respective matches and not changing their orientation.

# Input data

The input file `chibrituri.in` contains on the first line two natural numbers $n$ and $m$, separated by a space, indicating the number of vertical matches and horizontal matches, respectively.

# Output data

The output file `chibrituri.out` will contain on the first line the number of possible ways to form a correct hour, the second line will contain the minimum hour that can be obtained using all the matches and not changing their orientation, and the third line will contain the maximum hour that can be obtained using all the matches and not changing their orientation. The minimum hour and the maximum hour, respectively, will be written in the form $hh:mm$, where the hour $hh$ and the minute $mm$ will each consist of exactly two digits, separated by the character `:` (a colon).

# Constraints and clarifications

* Correctly determining the number of ways will account for 20% of the score, correctly determining the number of variants and the minimum hour will account for 60% of the score, and correctly determining the number of ways, the minimum hour, and the maximum hour will account for the maximum score.
* The digits are formed from matches as follows:

~[chibrituri2.png]

# Example

`chibrituri.in`
```
14 10
```

`chibrituri.out`
```
17
00:28
20:08
```

## Explanation

$17$ possible ways

Minimum hour: $00:28$

Maximum hour: $20:08$