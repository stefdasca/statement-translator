Gigel wants to start an advertising company. Since he doesn't have experience, he decided to start modestly by renting $Q$ billboards, from which he will subrent certain portions. Thus, he decided to divide each billboard with a height $H$ into the maximum possible number of horizontal regions/bands, all of height $h$, hence identical, with the condition that they do not overlap. Additionally, he conducted market research and associated the profit $P_h$ that he could obtain for a region of height $h$, $1 \leq h \leq h_{max}$. Since each client has their own opinion about the perfect ad size, profits are not correlated with sizes, thus making it possible that smaller regions generate higher profits.

# Task

Given the sequence of profits, $P_1$, $P_2$, $\\dots$, $P_{h_{max}}$, Gigel wishes to find out the maximum profits associated with a list of billboards $H_1$, $H_2$, $\\dots$, $H_Q$.

# Input data

The input file `panou.in` contains on the first line $h_{max}$ and $Q$, separated by a space. The second line contains $h_{max}$ numbers $P_1$, $P_2$, $\\dots$, $P_{h_{max}}$ separated by a space representing the profits. The third line contains, separated by a space, the heights $H_1$, $H_2$, $\\dots$, $H_Q$ of the $Q$ billboards that will be rented.

# Output data

The output file `panou.out` will contain $Q$ lines, on line $k$, $1 \leq k \leq Q$, it will contain a number representing the maximum profit obtained for the $k$-th billboard.

# Constraints and clarifications

* $1 \leq hmax \leq 100\ 000$
* $1 \leq Q \leq 10\ 000$
* $1 \leq P_i \leq 100\ 000$
* $1 \leq H_i \leq 10\ 000\ 000$
* For $70\%$ of the score $H_i \leq 100\ 000$
* For $10\%$ of the score $h_{max} \leq 1\ 000$ and $Q \leq 1\ 000$

# Example

`panou.in`
```
3 2
1 3 5
6 8
```

`panou.out`
```
10
12
```

## Explanation

For $H = 6$ we have two bands of height $3$ obtaining the maximum profit $2 \cdot 5 = 10$  
For $H = 8$ we have $4$ bands of height $2$ obtaining the maximum profit $4 \cdot 3 = 12$