
# Task

The President of an Informatics Contest wants the atmosphere at the closing ceremony to be pleasant. To achieve this, he wants to seat the participants in $n$ rows according to certain rules. These rules are:

- On the first row of seats, $n$ people are seated next to each other.
- On the following rows, the seating in position $i$ (numbering starts from left to right) is conditioned by the seating of people on the previous row. If on the row in front of position $i$ and $i+1$ there are either only boys or only girls, then a girl will be seated. If in these positions there are people of opposite genders, then a boy will be seated.

According to these rules, on the row with the order number $i$ $(i \in{1, 2, \dots, n})$, $n-i+1$ people will be seated.

Given $n$, determine the maximum number of boys that can sit in the hall while following the rules mentioned above.

# Input data

In the text file `sala.in`, the first line contains the number of digits of $n$, and the second line contains the digits of the number $n$ separated by a space.

# Output data

In the text file `sala.out`, the first line will contain the number stated in the task.

# Constraints and clarifications

* $1 \leq n \leq 10^{101}$
* For 30% of the tests, $n < 100$
* For 70% of the tests, $n < 30\ 000$

# Example 1

`sala.in`
```
1
5
```

`sala.out`
```
10
```

# Example 2

`sala.in`
```
2
1 3
```

`sala.out`
```
61
```
