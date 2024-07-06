Lizuca has $n$ ornamental flowers with heights $h_1, h_2, \dots, h_n$, expressed in centimeters. To water the plants, Lizuca follows this schedule: on the first day, she will choose one plant to water, on the second day, she will choose two plants to water, on the third day, she will choose three plants to water, and so forth. If a plant is watered on a particular day, it grows by $1$ centimeter by the end of that day; if it is not watered, it remains at the height it had at the end of the previous day.

# Task

Write a program that determines:
1. a natural number $S$, expressed in centimeters, representing the sum of the final heights of all plants if Lizuca waters them according to the described procedure, for $n$ days;
2. a natural number $K$, representing the maximum number of days Lizuca can water the flowers according to the described procedure, so that at the end of day $K$, no ornamental plant reaches the height $H$.

# Input data

The first line of the file `flori.in` contains two natural numbers $n$ and $H$, separated by a space, having the meaning described above.
The second line contains $n$ natural numbers: $h_1, h_2, \dots, h_n$ separated by a single space, representing the initial heights of the plants.

# Output data

The file `flori.out` will contain on the first line a natural number $S$ having the meaning described in Task 1. The second line will contain a natural number $K$, having the meaning described in Task 2.

# Constraints and clarifications

* $1 \leq n, H \leq 100$;
* $1 \leq h_1, h_2, \dots, h_n < H$;
* A plant can be watered only once per day.
* For correctly solving Task 1, $30\%$ of the total score will be awarded for each test.
* For correctly solving Task 2, $70\%$ of the total score will be awarded for each test.

# Example 1

`flori.in`
```
3 4
2 1 1
```

`flori.out`
```
10
2
```

## Explanation

If on the first day plant $3$ is watered, then the heights become: $2 \ 1 \ 2$;
If on the second day plants $1$ and $2$ are watered, then the heights become: $3 \ 2 \ 2$;
The process stops here because on the third day, all plants would need to be watered, and plant $1$ would reach the height $4$.

# Example 2

`flori.in`
```
4 5
1 3 2 1
```

`flori.out`
```
17
3
```

## Explanation

If on the first day plant $1$ is watered, then the heights become: $2 \ 3 \ 2 \ 1$;
If on the second day plants $1$ and $4$ are watered, then the heights become: $3 \ 3 \ 2 \ 2$;
If on the third day plants $1, 3$ and $4$ are watered, then the heights become: $4 \ 3 \ 3 \ 3$.