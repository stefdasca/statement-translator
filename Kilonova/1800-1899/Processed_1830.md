~[mojojojo.jpg|align=right]

Dizzy after the villain party, Mojo Jojo went to the store to buy $N$ bananas numbered with distinct indices from $1$ to $N$ (forming a permutation). The higher the index of a banana, the tastier it is. Like any other noble monkey, Mojo Jojo prefers to save the best for last. Therefore, he would like to eat them in order from the banana with the smallest index (the banana with index $1$) to the banana with index $N$.

Unfortunately, Mojo is too dizzy to sort the bananas as he likes, which is why he will eat them in the order he bought them. Being a genius in banana-nology, Mojo defined the cost of such a permutation as the number of inversions. Before he starts eating, Mojo decided to minimize the number of inversions of the permutation by using two types of operations:
* *Monkey Shot*: Mojo chooses two consecutive elements in the permutation and swaps them.
* *Monkey Punch*: Mojo punches the table and all bananas are shuffled randomly with uniform probability (performing a *random shuffle* of the permutation).

Although Mojo Jojo is a genius in algorithms and competitive programming, he does not feel well enough to deduce an optimal strategy for minimizing the number of inversions in a permutation. Given a natural number $K$, Mojo Jojo can apply up to $K$ of the described operations. Calculate the *expected value* of the number of inversions if Mojo applies an optimal strategy.

# Input data
The input file `mojosort.in` contains on the first line $T$, representing the number of tests. There are then $T$ pairs of lines: the first of these contains two integers $N$ and $K$, as explained in the statement, and the second line contains $N$ distinct integers, separated by spaces, representing the indices of the bananas in the order Mojo Jojo bought them.

# Output data
The output file `mojosort.out` will contain the answer for each of the $T$ tests. You can choose to display these numbers in two ways:
- *mojo-mode*: print a number $R = P \times Q^{-1}\text{ modulo }10^9 + 7$, where $X^{-1}$ denotes the modular inverse of $X$ modulo $10^9 + 7$, and the answer is $P / Q$, with $P$ and $Q$ being natural numbers, co-prime with each other.
- *jojo-mode*: print a real number representing the exact answer with an error of at most $10^{-6}$.

If you choose to display any result in mojo-mode, print the message `mojo` on the first line of the file. Otherwise, print the message `jojo`. All $T$ results must be displayed according to the selected model.

# Constraints and clarifications
* $1 \leq N, T \leq 300$
* $0 \leq K \leq 1\ 000\ 000\ 000$
* If you choose *jojo-mode* you will get $60\%$ of the test score.
* For $40\%$ of the tests, we have $N \leq 50$ and $T \leq 50$.

# Example
`mojosort.in`
```
2
3 2
3 1 2
3 1
3 2 1
```
`mojosort.out`
```
jojo
0.000000
1.500000
```
`mojosort.in`
```
2
3 2
3 1 2
3 1
3 2 1
```
`mojosort.out`
```
mojo
0
500000005
```
Explanation
---

In the first test, Mojo can swap the positions $(1,2)$ and $(2,3)$, obtaining the permutation $1,2,3$. This permutation has $0$ inversions.
In the second test, Mojo randomly rearranges the permutation, and the average number of inversions is $1.5$.
$1.5 = 3/2 = 3\times2^{-1} = 500\ 000\ 005$ modulo $10^9+7$