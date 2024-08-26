## Task

You are given a string $S$ of length $N$. We need to find the palindromic subsequence of $S$ with the maximum even length. Additionally, we have a budget of $B$ dollars. Once we choose a solution, we have to take into account $R$ constraints that will deduct from our budget. A constraint of the form $(a, b, c)$ means that if the subarray between $a$ and $b$ is taken in the palindrome, we have to pay $c$ dollars. This means that if all positions between $a$ and $b$ are chosen in the resulting palindrome, we have to pay $c$ dollars. What is the longest even-length palindrome such that in the end, we remain with a non-negative number of dollars?

## Input data

The input file `palsubsecv.in` will contain on the first line $T$, the number of tests. The first line of each test will contain three integers $N$, $R$ and $B$, separated by a space. The second line will contain the string $S$. The following $R$ lines of a test will each contain three integers $a$, $b$ and $c$, separated by a space, as described above.

## Output data

The output file `palsubsecv.out` will contain $T$ lines, on each line a natural number which will represent the answer to the task.

## Constraints and clarifications

$1 \leq T \leq 20$

$1 \leq N \leq 33$

$1 \leq R \leq 5000$

$1 \leq B \leq 10^9$

$1 \leq a \leq b \leq N$

$1 \leq c \leq 10^5$

$S$ contains only lowercase English letters

$x$ is non-negative if $x \geq 0$

Attention! You must choose a subsequence of the string, not a subarray! Only the cost is calculated based on subarrays.

We recommend that if you hold dollars in your left hand, you should also hold Leu notes in your right hand. 

## Example

`palsubsecv.in`
```
2 
5 2 9 
acbba 
1 2 10 
4 5 11 
4 
2 5 
xyyx 
3 4 2 
2 3 3 
2 4 
```

`palsubsecv.out`
```
4 
2 
```

## Explanation

In the first example, we can either take the subarray $aa$ or $bb$. We cannot take both, because we would need to pay 11 dollars since we take all characters in the interval $[4, 5]$.

In the second example, we take the entire string $S$ and pay $2 + 3 = 5$ dollars.