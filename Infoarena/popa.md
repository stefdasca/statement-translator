## Task

E haiduc, şi e vestit Andrii Popa cel voinic Zi şi noapte tot călare Trage bir din drumul mare Şi din ţară peste tot Fug neferii cât ce pot - "Andrii Popa", Phoenix Ghiţă has a sequence $S$ with $N$ integers, indexed from 0. As he is the king of the Carpathians, he wants to build a binary tree whose nodes have indices $0, 1, \ldots, N-1$ such that: The inorder traversal (i.e., left child, then root, then right child) of the tree is $0, 1, \ldots, N-1$ . If node $x$ is the parent of node $y$ , then $S_x$ divides $S_y$ . Unfortunately, the famous haiduc Andrii Popa stole the sequence $S$ , and Ghiţă can no longer access it directly. With the help of advanced technology (his mobile phone), he can, for any two continuous subarrays $[a, b]$ , $[c, d]$ of $S$ , determine if $\text{gcd}(S_a, \dots, S_b) = \text{gcd}(S_c, \dots, S_d)$ . Unfortunately, the technology is expensive - if Ghiţă uses it more than $Q$ times, he will have to pay extra. Help him use the technology at most $Q$ times to construct the desired tree.

## Interaction

This problem is interactive. Initially, you will read from stdin the number $T$ of test cases that you will need to solve. Each test has the following format: initially you will read from stdin $N$ . To use Ghiţă’s technology, print $0$ followed by 4 numbers $a \ b \ c \ d$ to stdout , all followed by a space, then flush stdout (for example with $\text{fflush(stdout)}$ in C or with $\text{std::cout << std::flush}$ in C++ ). Then read the response to your query from stdin ( $1$ indicates that the $\text{gcd}$ -s match, $0$ that they do not). To print your answer, print $1$ , followed by the answer in the following format: first the root of the tree, followed by $N$ numbers, where the $i$-th number represents the left child of $i-1$ , or $-1$ if $i+1$ does not have a left child, then another $N$ numbers, where the $i$-th number represents the right child of $i-1$ , or $-1$ if $i-1$ does not have a right child, all followed by a space (including the last number). Then flush stdout.

## Constraints and clarifications

There is always a solution 

Any tree that meets the conditions will be accepted 

For $40$ points, $N = 100$ and $Q = 10\ 000$

For $20$ points, $N = 1\ 000$ and $Q = 20\ 000$

For $40$ points, $N = 1\ 000$ and $Q = 2\ 000$

$Q$ is not visible to the contestant's program.

## Example

```
stdout            stdin
1                 6
T and N
0 0 1 3 5         Query
0                 Response to query
0 4 5 1 3         Query
1                 Response to query
1 3 -1 0 -1 1 -1 -1 -1 2 -1 4 5 -1         Final problem answer
```

## Explanation

Here, $S = [12, 4, 16, 2, 2, 20]$ .