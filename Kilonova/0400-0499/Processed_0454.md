Mihăiță has decided to build a perfect fence with the help of Dorel - a renowned builder. A perfect fence must meet the following requirements:

1. The fence should consist of $N$ planks of not necessarily equal heights;
2. The planks can be arranged in any order;
3. There is an equal number of planks for each height;

Mihăiță accepts a fence as perfect if it meets the above conditions before or after removing a single plank.

# Task
Help Mihăiță verify the perfection of the $T$ fences proposed by Dorel.

# Input data
The first line of the file `gard.in` contains a natural number $T$, representing the number of fences proposed by Dorel. The next $T$ lines contain a natural number $N$, followed by $N$ values $H_i$ separated by a single space, representing the heights of the planks of the fence proposed by Dorel.

# Output data
The output file `gard.out` will contain $T$ lines, each line will print $1$ if the fence is perfect, $0$ otherwise.

# Constraints and clarifications
* $1 \leq T \leq 10$;
* First 50% of tests:
  * $1 \leq N \leq 1\ 000\ 000$;
  * $1 \leq H_i \leq 10\ 000$.
* Next 50% of tests:
  * $1 \leq N \leq 100\ 000$;
  * $1 \leq H_i \leq 1\ 000\ 000\ 000$.
* For 50% of the total tests, removing any plank will not transform an imperfect fence into a perfect one.

# Example

`gard.in`
```
4
6 2 2 3 3 4 4
6 2 3 3 5 5 5
7 3 3 4 4 4 5 5
8 3 3 3 4 4 5 5 5
```

`gard.out`
```
1
0
1
0
```

## Explanation

- $1$: There is an equal number of planks for each height;
- $0$: The fence cannot be perfect either before or after removing any plank;
- $1$: The fence becomes perfect after removing a plank of height $4$;
- $0$: The fence cannot be perfect either before or after removing any plank.