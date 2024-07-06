# ACPC (**The Association of Cats' Politically Correctness**)

ACPC has stated that *all cats are equally cute*, a statement that is certainly false, considering the existence of cats without fur.

Outraged by this statement, the organizers of a cat exhibition decided to host a contest within the exhibition. They will evaluate all `N` exhibited cats to establish once and for all the cutest among them.

Each cat was evaluated based on three criteria:

1. **Fluffiness** or genetic score: how fluffy the cat's fur is;
2. **Photogenicity** or artistic instinct: how photogenic the cat is;
3. **Lovability** or luck in life: how loved the cat is by its owner.

The exhibition organizers created a separate ranking for each of the three categories, determining the order of the `N` cats according to each criterion. However, they now wish to create a cumulative ranking that establishes a clear and undeniable order of their cuteness.

Since it has often proven difficult to establish this, they have agreed that a cat `i` (`1 \leq i \leq N`) is considered "absolutely cuter" than a cat `j` if cat `i` appears before cat `j` in at least two of the three individual rankings.

As they do not have much experience with contests, the organizers ask you to help determine if there is a valid cumulative ranking and, if it exists, to find it. A ranking is considered valid if, for any two cats `i` and `j` (`1 \leq i, j \leq N`), cat `i` appears before cat `j` in the ranking **if and only if** cat `i` is "absolutely cuter" than cat `j`.

# Implementation Details

You will implement the function with the following header:

```cpp
std::vector<int> rank_cats(std::vector<int> p, std::vector<int> f, std::vector<int> d)
```

**Attention!** The `rank_cats` function will be called **at least once and at most 10 times**. The three arrays `p`, `f` and `d` will have the same length and will represent the rankings of all `N = |p|` cats according to each of the three mentioned criteria. For example, $p_i (0 \leq i < N)$ will represent the order number of the cat in the `i + 1` position according to fluffiness. **It is guaranteed that each of the three arrays represents a permutation of the numbers from** `1` **to** `N`**.**

For the returned solution to be valid, the length of the returned array must be equal to `N` and it must represent a valid cumulative ranking according to the explanations in the prompt. **If no valid ranking exists, the function must return an empty array (of length zero).**

# Scoring

## Subtask 1 (8 points)
* `1 \leq N \leq 10`
## Subtask 2 (8 points)
* `1 \leq N \leq 17`
## Subtask 3 (23 points)
* `1 \leq N \leq 2000`
## Subtask 4 (61 points)
* `1 \leq N \leq 100000`

# Sample Grader

The grader will read input data from the console in the following format:
- line 1: $N$, representing the number of cats
- line 2: $p_0 \\ p_1 \\ ... \\ p_{N-1}$ (separated by spaces)
- line 3: $f_0 \\ f_1 \\ ... \\ f_{N-1}$ (separated by spaces)
- line 4: $d_0 \\ d_1 \\ ... \\ d_{N-1}$ (separated by spaces)

The grader will print your response to the console in the following format:
- line 1: $r_0 \\ r_1 \\ ... \\ r_{N-1}$ (separated by spaces), representing the cumulative ranking.

If your response is an empty vector, the grader will print a single line with the message `NO SOLUTION`.

# Examples
`stdin`
```
6
3 1 6 4 5 2
1 3 4 5 6 2
3 4 2 6 1 5
```
`stdout`
```
3 1 4 6 5 2
```
`stdin`
```
3
3 1 2
2 3 1
1 2 3
```
`stdout`
```
NO SOLUTION
```

Explanation
---

The three exhibited cats corresponding to the second example are illustrated below:

~[Enunt_Pisi.jpg]

The contestant with number `1` is fluffier and more loved than contestant `2`, but it is less fluffy and less photogenic than contestant `3`. On the other hand, contestant `2` is more photogenic and more loved than contestant `3`.

In conclusion, a cumulative ranking of the three contestants cannot be determined.