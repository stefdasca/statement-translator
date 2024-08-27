## Task

Gigel is fascinated by both shoelaces and divisors. For example, yesterday he saw two interesting ways to tie shoelaces on shoes with $6$ pairs of holes: Immediately he wondered in how many ways the shoelaces could be tied on shoes with $n$ pairs of holes. For example, for $3$ pairs of holes, Gigel realized there are $4$ possibilities: What do shoes have to do with divisors? Being more inquisitive, Gigel is not interested in knowing the exact number of ways to tie the shoelaces -- he is much more interested in knowing how many natural divisors the number of ways to tie the shoelaces on shoes with $n$ pairs of holes has. Write a program to help him.

## Input data

The input file `sireturi.in` contains on the first line the number of tests $T$.

The next $T$ lines contain a number $n$ representing the number of holes on the shoes.

## Output data

In the output file `sireturi.out` print on each line for each test the number of natural divisors of the number of ways to tie the shoelaces on shoes with $n$ holes. The results must be printed modulo $9901$.

## Constraints and clarifications

To tie the shoelaces, the laces must pass through each hole only once (the lace is always inserted from top to bottom).

From one hole, the lace must go to a hole on the other side of the shoe.

Two ways of tying the lace are not considered different if they differ only in that one segment passes over or under another segment of the lace.

Obviously, when tying the shoelaces, the topmost pair of holes must be tied directly (that's where the bow is made ;-) ).

$1 \leq n \leq 7500$

$1 \leq T \leq 10000$

## Example

`sireturi.in` `sireturi.out`
```
2
2
3
```
```
1
3
```

## Explanation

For shoes with two pairs of holes, there is only one way to tie the shoelaces. The number $1$ has exactly one natural divisor; modulo $9901$ we get $1$.

For shoes with three pairs of holes, there are $4$ ways to tie the shoelaces (as seen above). The number $4$ has exactly $3$ divisors: $1$, $2$, $4$. The remainder of dividing $3$ by $9901$ is $3$.