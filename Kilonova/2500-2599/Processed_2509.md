Floricel wants to make as much money as possible. In order to have enough money to buy an apartment, he has to solve a problem that can be modeled as follows: He has $N$ initial intervals given by their endpoints. Floricel also needs to create new intervals called covering intervals.

An initial interval is considered covered if there exists at least one covering interval with an intersection with the initial interval being at least half the length of the initial interval. For example, interval $[0, 4]$ is covered by the set of intervals $\\{[2, 5], [\text{-}1, 1]\\}$, but it is not covered by the set of intervals $\\{[0, 1], [2, 3], [3, 4]\\}$.

# Task

His friend, Ted, tells him that he needs more challenges in life to be happier, and asks him $Q$ questions of the form: "*If you are allowed to create at most $K$ covering intervals, what would be the minimum length of the longest covering interval so that all initial intervals are covered? And if you can, what is the lexicographically minimal solution? A solution is lexicographically minimal if it is minimal first by the number of covering intervals, and then by comparing the intervals by the left and right ends, ordering the intervals by the left ends.*"

# Input data

The first line of the input file `acoperire.in` contains the number $N$. The next $N$ lines contain two natural numbers $S_i$ and $D_i$, where the numbers on line $i + 1$ represent the left and right ends of the $i$-th interval. Next is a line with the number $Q$, and on the following $Q$ lines there is a number $K$, representing one of Ted's questions for which we want to find out the minimum length of the longest covering interval if we can create at most $K$ covering intervals.

# Output data

The output file `acoperire.out` must contain $Q$ answers in order. For a question with given $K$, the first line must contain the length of the longest covering interval under the given conditions, the next line must contain the number of covering intervals used (at most $K$), and on the following lines the left and right ends of the intervals, ordered by the left end.

If a value is an integer, it should be printed as an integer, otherwise it should be printed as a real number with exactly one decimal place.

# Constraints and clarifications

* $1 \leq N \leq 10^5$;
* $0 \leq S_i \lt D_i \leq 10^8$;
* $1 \leq Q \leq 20$;
* $1 \leq K \leq N$ and the sum of all $K$ is at most $10^5$;
* Points are awarded for a test only if all minimum lengths of the longest covering interval are found correctly. If a solution is not correct or not lexicographically minimal, $75\\%$ of the score for a question will still be awarded. All questions in a test have the same score value.
* If you only want to display the length, you can display $0$ as the number of intervals in the solution.

|# | Points | Constraints|
| - | - | ------------|
|1|10|$N = 1$|
|2|10|$N = 2$ and the initial intervals are disjoint.|
|3|20|$Q = K = 1$|
|4|20|Initial intervals are disjoint, any two.|
|5|40|No additional constraints.|

# Example

`acoperire.in`
```
5
0 2
1 4
1 2
3 5
3 6
3
1
2
3
```

`acoperire.out`
```
3.5
1
1 4.5
1.5
2
1 2.5
4 5.5
1.5
2
1 2.5
3 4.5
```

## Explanation

The input file contains $5$ initial intervals, illustrated in red below.

~[acoperire_ex.png]

For $K=1$ we have one covering interval, of length $3.5$, i.e. $[1, 4.5]$, and the solution is lexicographically minimal.

For $K=2$, the example answer above represents a solution with the longest covering interval of length $1.5$. The solution receives only $75\\%$ of the points for the second question because it is not lexicographically minimal: replacing interval $[4, 5.5]$ with $[3, 4.5]$ represents a lexicographically smaller solution.

For $K=3$, the solution is lexicographically minimal because only two covering intervals are needed.

The solution obtains $(100+75+100)/3 = 91.66\\%$ of the test points.

# Epilogue

â€œIn the end, Floricel realized that material things are necessary but not sufficient for fulfillment in life. Now that he no longer follows what he sees from others, he does not chase fake lifestyles, cringe, and propaganda on social media, and the goals he aims for are chosen by himself, for his own fulfillment and that of those around him. Now he is truly happy.â€