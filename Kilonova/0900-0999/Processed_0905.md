Emperor The Old Man wants to divide the bags of gold in the palace treasury among his $K$ sons, numbered from $1$ to $K$ in the order of their age. Son number $1$ is the eldest, and the youngest has number $K$.

In the treasury, there are $N$ bags full of gold, arranged in a line, so heavy that their order cannot be changed, and each bag has the number of gold coins it contains written on it.
\\
The emperor calls one of his sons and tells him, "Son, the fortune of the first $x_1$ bags is yours!" The son takes the bags and leaves happily. Then, the emperor calls another son and tells him, "Son, the fortune of the first $x_2$ bags from those remaining is yours!" And so on, until he reaches the last son called, to whom he gives all the remaining bags.

He doesn’t have a specific order in which he calls his sons but makes sure to call each son exactly once. Also, to avoid disputes among them, he ensures that each son receives at least one bag of gold, but **does NOT receive a total amount of gold more than any of his elder brothers**. The emperor’s youngest son is also the bravest, so the emperor wants to give him the maximum possible amount of gold, without upsetting his other sons.

# Task
How could the emperor divide the bags?

# Input Data
The input file `mostenire.in` contains on the first line the natural numbers $N$ and $K$, separated by a space, as stated in the problem. The next $N$ lines each contain a natural number, representing the number of gold coins in each bag, in the order they are to be distributed to the sons.

# Output Data
The output file `mostenire.out` will contain on the first line the sum of gold coins that the youngest son will receive from the emperor. On the next $K$ lines, there will be two natural numbers representing the order number of the son and the number of bags $x_i$ he receives, in the order they were called by the emperor.

# Constraints and Clarifications
- $2 \leq K \leq 100$
- $K \leq N \leq 100\ 000$
- The number of gold coins in each bag will be between $1$ and $100\ 000$.
- The gold coins in any bag cannot be divided among multiple brothers.
- The total number of gold coins in the treasury is less than or equal to $10^9$.
- The old emperor has no two sons with the same age.
- **You can display any solution in which the youngest receives the maximum possible number of gold coins**.
- For each test, correctly displaying the maximum number of gold coins received by the youngest is worth $40\%$ of the test’s score.
- For tests worth 10 points, $N = K$ and $N \leq 100$.
- For tests worth 30 points, $2 \leq K < N \leq 15$.
- For tests worth 50 points, $2 \leq K < N \leq 100$.

# Example 1
`mostenire.in`
```
8 3
1
2
3
4
5
6
7
8
```
`mostenire.out`
```
10
3 4
2 2
1 2
```

## Explanation
The youngest son is called first and takes the first $4$ bags, thus receiving $1+2+3+4 = 10$ gold coins.
The middle son is called second and takes the next $2$ bags, thus receiving $5+6 = 11$ gold coins.
The eldest son is called last and takes the remaining $2$ bags, thus receiving $7+8 = 15$ gold coins.

# Example 2
`mostenire.in`
```
12 4
10
5
23
1
20
4
10
12
6
23
18
17
```
`mostenire.out`
```
35
2 3
4 4
1 3
3 2
```

## Explanation
The second son in the order of age is called first and takes the first $3$ bags, thus receiving $10+5+23 = 38$ gold coins.
The youngest son is called second and takes the next $4$ bags, thus receiving $1+20+4+10 = 35$ gold coins.
The eldest son is called third and takes the next $3$ bags, thus receiving $12+6+23 = 41$ gold coins.
The third son in the order of age is called last and takes the remaining $2$ bags, thus receiving $18+17 = 35$ gold coins.

Another correct solution is:
```
35
2 3
3 4
1 3
4 2
```

