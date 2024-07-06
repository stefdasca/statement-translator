A mischievous child was walking through the park when suddenly a bear appeared on the path. Fortunately, a very old witch appeared and saved the child from the bear's claws. However, the witch's help is not unconditional. To repay her, the witch brought her dwarfs and said to the child:

"Look closely at the dwarfs. Each of them has three numbers written on their foreheads. Let's denote the numbers of dwarf $i$ with $v_i$, $b_i$ and $x_i$. We consider the number $m_i$, which is equal to the number of gadfadearian numbers from $0$ to $v_i$. You may wonder what a gadfadearian number is. Well, it is a number that has $x_i$ ones in its representation in base $b_i$. I want to know $m_i$. However, I will be generous today and only ask you for the result modulo $10^9 + 7$."

Help the witch find the answer to the question!

# Input data

The first line contains a natural number $n$, representing the number of dwarfs.

The next $n$ lines contain the numbers on the dwarfs' foreheads, the number $v_i$ representing the number written on the forehead of dwarf $i$, $b_i$ represents the base referred to by the witch, and $x_i$ represents the number of ones in base $b_i$ that we need. **The number is given in base $b_i**.

# Output data

For each dwarf, print on a separate line the required answer, representing the value of $m_i$ modulo $10^9 + 7$.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* $v_i$ has at most $10^5$ digits in base $b_i$;
* $2 \leq b_i \leq 10$;
* $0 \leq x_i \leq |v_i|$;

|#|Score|Constraints|
|-|-----|-----------|
|1|11|$v_i \leq 10^3$|
|2|10|$v_i \leq 10^6$|
|3|15|$v_i$ has at most $10^3$ digits, $b_i = 2$ and $x_i \leq 1$, for all queries|
|4|11|$v_i$ has at most $10^3$ digits, $b_i = 2$ and $x_i \leq 2$, for all queries|
|5|23|$v_i \leq 10^{18}$|
|6|30|No additional constraints|

# Example 1

`stdin`
```
6
99 10 1
1110100011 2 3
1110100011 2 2
12103 5 2
681 9 0
999 10 2
```

`stdout`
```
18
120
45
219
377
27
```

## Explanation

For the first example, the valid numbers are $1$, the numbers from $10$ to $19$ except for $11$, and the numbers $21$, $31$, $\dots$, $91$.