```markdown
# Task

The Spring Carnival has arrived and $n$ tourists have reached to the event. We know that all the tourists must wear a hat which is in one of the $k$ colors.

The carnival organizers have given each tourist a hat and asked them to sit in a line to take a group picture. However, the picture was lost, but fortunately an observer recorded for each person how many people in front of them had a hat of the same color as the hat they were wearing.

For example, if the array is [$0, 1, 0, 1, 2, 3$], the second person had one person in front of them with the same hat color, while the fifth person had two people with the same hat color in front of them.

Assuming that the carnival organizers have an unlimited number of hats of each of the $k$ colors, find out how many different ways exist which could have been used to assign hats to people such that the array the observer recorded would be the same as the array we would record for that given configuration?

Since the answer can be big, print it modulo $10^9+7$.

# Input data

The input will contain on the first line $n$ and $k$ ($1 \le n \le 2 \ 10^5$), ($1 \le k \le 10^8$).

The next line will contain the array $v$ ($0 \le v_i < i$).

For tests worth $10$ points, ($1 \le n, k \le 8$).

For tests worth $30$ more points, ($1 \le n, k \le 1000$).

# Output data

The output will contain a single number, representing the answer modulo $10^9+7$.

# Example 1

`stdin`
```
6 4
0 1 0 1 2 3
```

`stdout`
```
24
```

# Example 2

`stdin`
```
4 3
0 1 0 0
```

`stdout`
```
6
```

# Explanation

For the second sample test case, the arrays we can generate are:

$[1, 1, 2, 3]$, $[1, 1, 3, 2]$, $[2, 2, 1, 3]$, $[2, 2, 3, 1]$, $[3, 3, 1, 2]$, $[3, 3, 2, 1]$
```