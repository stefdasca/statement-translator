Here is the translated problem statement:

---

For a nonzero natural number `n`, let's consider all nonzero natural numbers less than or equal to `n`, taking each number twice: `1, 1, 2, 2, 3, 3, ... , n, n`. These numbers are randomly shuffled and arranged into two rows of `n` elements each. This structure will be called a bipermutation. Figures `1, 2` and `3` show examples of bipermutations for `n=5`.

A bipermutation is perfect if both rows of the structure represent a permutation (see figures `2` and `3`).

By moving to position `p`, we understand the swapping of elements on the same column `p`. In the examples below, the perfect bipermutation in figure `2` was obtained from the bipermutation in figure `1` by applying a move to position `2`. The perfect bipermutation in figure `3` was obtained from the bipermutation in figure `1` by applying moves to positions `1, 2, 4` and `5`.

~[biperm.png]

# Task
Given a bipermutation, determine:
* the number of distinct perfect bipermutations that can be obtained through moves;
* the minimum number of moves required to obtain a perfect bipermutation;
* a perfect bipermutation obtained from the initial bipermutation.

# Input data
The input file `biperm.in` contains on the first line the value of `n`. The next two lines each contain `n` elements separated by spaces, forming a bipermutation.

# Output data
The output file `biperm.out` will contain:
* on the first line, two natural numbers separated by a space, representing the number of distinct perfect bipermutations that can be obtained from the given bipermutation, and the minimum number of moves required to obtain a perfect bipermutation;
* on the next two lines, `n` numbers separated by spaces, representing a perfect bipermutation obtained from the given bipermutation.

# Constraints and clarifications
* `2 < n \leq 10\ 000`;
* correct calculation of the number of distinct perfect bipermutations is worth `30%` of the score;
* correct calculation of the minimum number of moves is worth `10%` of the score;
* printing a perfect bipermutation is worth `60%` of the score. There may be multiple solutions, any correct solution will be accepted;
* it is guaranteed that the number of distinct perfect bipermutations does not exceed `2\ 000\ 000\ 000` for any test.
* awarding of points for a correct answer is conditioned by the existence of previous answers, regardless of their correctness;
* for `40%` of the tests `n \leq 20`;
* for `40%` of the tests `20 < n \leq 400`;
* for `20%` of the tests `400 < n \leq 10\ 000`.

# Example

`biperm.in`
```
5
1 5 5 3 4
3 2 2 4 1
```

`biperm.out`
```
4 1
1 2 5 3 4
3 5 2 4 1
```

Explanations
---

There are `4` perfect permutations. The minimum number of moves is `1` and there are two solutions with the minimum number of moves:
```
1 2 5 3 4             1 5 2 3 4
3 5 2 4 1     and     3 2 5 4 1
```
The other two solutions that are not obtained from the minimum number of moves are:
```
3 2 5 4 1             3 5 2 4 1
1 5 2 3 4     and     1 2 5 3 4
```
For the third task, any of the `4` solutions is acceptable.

---

Please double check for any potential grammar and syntax errors.