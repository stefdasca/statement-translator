On an island, after multiple chemical experiments, an extremely dangerous phenomenon occurs. The wasps multiply very quickly causing significant damage. The governor decides that after $n$ days the island should be evacuated. The task is to determine the number of wasps present on the day of departure, knowing that on the first day after the phenomenon there are $p$ wasps, on the second day there are $q$ wasps, and on the days with the number $k$ the number of wasps is equal to four times the number of wasps from the day $k-1$, minus the number of wasps from the day $k-2$.

# Input data

In the text file `viespi.in`, the first line contains $n$, $p$, and $q$ separated by a space.

# Output data

The first line of the output file `viespi.out` will contain a single integer, the number of wasps after $n$ days.

# Constraints and clarifications

* $1 \leq p, q \leq 100$;
* $3 \leq n \leq 100$;

# Example 1

`viespi.in`
```
4 2 3
```

`viespi.out`
```
37
```