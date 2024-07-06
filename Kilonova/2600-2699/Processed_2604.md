Maria Antoaneta was a controversial figure in the history of France, becoming the wife of King Louis XVI on May 16, 1770. The queen was an avid reader of historical novels, and her scientific interest led her to attend hot air balloon launches. She was fascinated by the philosophy of Rousseau and the culture of the Incas from Peru, with their sun worship. On the other hand, the young princess was passionate about dresses and jewelry. The Affair of the Diamond Necklace was a major scandal. A great Austrian jeweler was tasked with dismantling the crown jewels to create an even more valuable and beautiful piece of jewelry. This jeweler knows the value of the jewelry to be dismantled, which can be in the order of millions. The value is an integer $N$ with $K$ digits. Since the jeweler is very talented and knows the market value, we know that he has correctly estimated the price $N$ and that it does not start with digits of $0$. To fulfill his duty, he wants to know all the ways to obtain a piece of jewelry with a value strictly greater than $N$. He has defined $B(N)$ as the number of integers strictly greater than $N$, which are formed by permuting the digits of $N$.

# Task
Given $K$ and $N$, determine $B(N)$.

# Input Data
The input file `bijuterie.in` contains the natural number $K$ on the first line and on the second line $K$ digits representing, in order, the digits of the number $N$.

# Output Data
The output file `bijuterie.out` will contain on the first line the value of $B(N)$. Since this value can be very large, print the result modulo $1\ 000\ 000\ 007$.

# Constraints and clarifications

- $1 \leq K \leq 1\ 000\ 000$
- It is guaranteed that the number $N$ does not start with digits of $0$.

|#| Score | Constraints                                         |
|-|---------|--------------------------------------------------|
|1| 11       | $1 \leq K \leq 9$                               |
|2| 22       | $10 \leq K \leq 5\ 000$ \t\t                     |
|3| 36       | $5\ 001 \leq K \leq 10\ 000$    \t\t\t\t\t     |
|4| 31       | No additional constraints                     |

# Example 1
`bijuterie.in`
```
2
15
```
`bijuterie.out`
```
1
```

# Example 2
`bijuterie.in`
```
4
1123
```
`bijuterie.out`
```
11
```
