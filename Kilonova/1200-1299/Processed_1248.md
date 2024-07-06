Here is the translated competitive programming problem statement:

---

In Târgoviște, the Autumn Festival is being organized. In the competition "apple carrying", teams are formed by $5$ participants: $3$ "receivers", who each have a prime number of baskets, different both within the team and from the other participants in other teams, a "distributor", and an "assistant". The "distributor" must take from the pile of apples a number of apples that can be equally divided into all the baskets of at least one "receiver" from his team, but cannot be equally divided into the baskets of any other receiver from the other teams. The organizers set a number $n$ of transports that the distributor must carry out. A team is disqualified if the distributor carries in one transport a number of apples that can be equally divided into the baskets of another "receiver" other than those from his team, or cannot be divided into the baskets of any of his "receivers". The organizers establish the following rules:
- $n$ transports must be carried out.
- For each transport $i$, the number $m_i$ of apples must be strictly greater than the number $m_{i-1}$ of apples from transport $i-1$ and it is prohibited that in the interval $m_{i-1}, m_i$ there is another number of apples that can be equally divided into the baskets of at least one "receiver" from the team.
- For "efficiency", the "assistant" can prepare piles of apples for the "distributor" in the order in which he will transport them.

At the beginning of the contest, the team's "distributor", considering the rules of the contest, explains to the "assistant" how to prepare the piles of apples in the order in which he will carry them. 
Example: For the basket numbers of the "receivers" $p_1=2, p_2=3$ and $p_3=5$, the number of transports $n=18$, the number of apples transported will be, in order:
$2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32$

# Input data

The input file `mere.in` contains in the first line the natural number $n$ and in the second line the prime numbers $p1, p2$ and $p3$, separated by a space each.

# Output data

The output file `mere.out` will contain, in increasing order, one per line, the first $n$ numbers with the requested property.

# Constraints and clarifications

* $1 \leq n \leq 800$
* $2 \leq p_1 < p_2 < p_3 \leq 97$
* It is guaranteed that the numbers to be generated are $\leq 2\ 000\ 000\ 000$.

# Example

`mere.in`
```
10
2 3 5
```

`mere.out`
```
2 
3 
4 
5 
6 
8 
9 
10 
12 
15
```

## Explanation

The generated numbers are the smallest $10$ numbers that have prime divisors only the numbers $2, 3$, and $5$.

