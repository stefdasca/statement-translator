At the horseshoe-making workshop, $N$ workers are employed, numbered from $1$ to $N$ for simplicity. Each worker has a contract specifying the number of horseshoes the worker must produce each working day, and which day the worker is off. More precisely, worker $i$ ($1 \leq i \leq N$) must produce $p_i$ horseshoes on each working day, and every $k_i$-th day will be off (i.e., worker $i$ will be off on day $k_i$, $2k_i$, $3k_i$, ...). On the off day, the worker will not come to the workshop and thus will not produce horseshoes. The workshop has just received an order for $M$ horseshoes.

# Task
  
Write a program that determines the minimum number of days after which the order can be fully delivered.

# Input data
  
The input file `potcoave.in` contains the following:
- The first line contains the natural number $M$ representing the number of horseshoes that need to be delivered.
- The second line contains the natural number $N$ representing the number of workers.
- The following $N$ lines contain the contractual data of the $N$ workers. On the $i$-th line among the $N$ lines, there are two natural numbers separated by space $p_i \ k_i$, with the significance described in the statement ($1 \leq i \leq N$).
  
# Output data
  
The output file `potcoave.out` will contain a single line which will print the minimum number of days after which the order for $M$ horseshoes from the received order can be delivered.

# Constraints and clarifications
  
* $1 \leq M \leq 10^{18}$
* $1 \leq N \leq 10^{4}$
* $1 \leq p_i \leq 10^{18}$, for $1 \leq i \leq N$
* $2 \leq k_i \leq 10^{18}$, for $1 \leq i \leq N$
* For $10$ points, $N=1$.
* For another $16$ points, $1 < N \leq 10$ and $M \leq 100 \ 000$.
* For another $18$ points, $N=2$ and $M>100 \ 000$.

# Example
  
`potcoave.in`
```
100
3
2 3
3 4
5 7
```
  
`potcoave.out`
```
13
```
  
## Explanation
  
Day $1$: all $3$ workers work and produce $2+3+5=10$ horseshoes.
Day $2$: all $3$ workers work and produce $2+3+5=10$ horseshoes.
Day $3$: workers $2$ and $3$ work and produce $3+5=8$ horseshoes.
Day $4$: workers $1$ and $3$ work and produce $2+5=7$ horseshoes.
Day $5$: all $3$ workers work and produce $2+3+5=10$ horseshoes.
Day $6$: workers $2$ and $3$ work and produce $3+5=8$ horseshoes.
Day $7$: workers $1$ and $2$ work and produce $2+3=5$ horseshoes.
Day $8$: workers $1$ and $3$ work and produce $2+5=7$ horseshoes.
Day $9$: workers $2$ and $3$ work and produce $3+5=8$ horseshoes.
Day $10$: all $3$ workers work and produce $2+3+5=10$ horseshoes.
Day $11$: all $3$ workers work and produce $2+3+5=10$ horseshoes.
Day $12$: only worker $3$ works and produces $5$ horseshoes.
Day $13$: all $3$ workers work and produce $2+3+5=10$ horseshoes.
After $13$ days, the total number of horseshoes produced is $10+10+8+7+10+8+5+7+8+10+10+5+10=108$, enough to fulfill the order.