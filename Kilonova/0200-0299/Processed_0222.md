After the adventure on *Cetățuie*, Alex is undecided: he doesn't want to go home yet, but he also doesn't know where to go next. He has come up with an ingenious idea: he knows `M` other tourist attractions in Jluc. Therefore, he decided to make a poll where his `N` friends can decide for each attraction whether they like it or not. Then, he will choose a subarray `S` of friends and will only consider their opinions. Having now all the answers from his friends, Alex decides to use the following algorithm: he takes each tourist attraction in order, from `1` to `M`, and eliminates from his list all the votes of friends who are not in the majority for the current attraction (in case of a tie, it is considered that those who voted that they like it are in the majority). In the end, Alex will be left with a single opinion (even though it can belong to more than one friend), and he will use it to make a final decision. However, Alex now wonders: for each friend `i`, what is the number of subarrays `S` that contain `i`, for which, if the above algorithm is applied, the final opinion is that of `i`. Since this number can be large, he only wants to know the remainder of its division by `MOD`.

# Input data
The first line contains the numbers `N`, `M`, `MOD` separated by spaces, with the meaning as described above. Then, on the following `N` lines, there will be `M` numbers each, value `j` on line `i` having the value `1` if friend `i` liked tourist attraction `j`, and `0` otherwise.

# Output data
Print `N` values separated by space, the `i`-th number representing the answer for friend `i`.

# Constraints and clarifications
* `1 \leq N \leq 4\ 000`
* `1 \leq M \leq 1\ 000`
* `2 \leq MOD \leq 1\ 000\ 000\ 007`, and `MOD` is a prime number

## Subtask 1 (6 points)
* `1 \leq N \leq 15` and `1 \leq M \leq 15`

## Subtask 2 (7 points)
* `1 \leq N \leq 20` and `1 \leq M \leq 40`

## Subtask 3 (45 points)
* `1 \leq N \leq 200` and `1 \leq M \leq 200`

## Subtask 4 (42 points)
* No additional constraints

# Examples

`stdin`

```
3 2 11
10
11
10
```

`stdout`

```
3 3 3
```

## Explanations

For the subarray of friends formed by the first `2` elements `10, 11`, after the first attraction the subarray does not change, but for the second attraction, the first will be eliminated from it because they are in the minority.