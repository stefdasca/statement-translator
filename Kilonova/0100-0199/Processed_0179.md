Miruna and her adventure partner, Pikachu, are facing a new challenge. The two characters have arrived next to a mountain range, consisting of `N` peaks arranged in a straight line one after the other. For each mountain peak, its height is known. Using his extraordinary powers, Pikachu is capable of decreasing or increasing the height of a mountain peak by one unit per second. For reasons unknown to ordinary mortals, the two friends want to obtain at least `K` consecutive mountain peaks having the same height, in the shortest possible time.

# Task
Determine the minimum time in which Pikachu can fulfill this task.

# Input data
The input file `pikachu.in` will contain in the first line two numbers `N` and `K` having the meaning from the statement. The second line contains `N` natural numbers representing the heights of the mountain peaks.

# Output data
The output file `pikachu.out` will contain a single natural number `T`, representing the minimum time needed to obtain at least `K` consecutive peaks with the same height.

# Constraints and clarifications
* $1 \leq N \leq 10^5$
* `1 \leq K \leq N`
* The heights of the mountains are positive numbers that can be represented on signed `32`-bit integers
* `20%` of the tests have `1 \leq N, K \leq 100`, and the heights belong to the interval `[1, 100]`
* Another `20%` of the tests have `1 \leq N, K \leq 5000`
* The result can be represented on a signed `64`-bit integer

# Example

`pikachu.in`
```
5 3
5 2 4 3 7
```

`pikachu.out`
```
2
```

Explanation
---

In the first second, the height of the mountain at the second position is increased, and in the second second, the height of the mountain at the third position is decreased. As a result of these operations, the subarray that starts at the second position and ends at the fourth position will contain only peaks with height `3`.