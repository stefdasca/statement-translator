
**ATTENTION: This problem has a similar statement to *John Mex*, but it is fundamentally different. Read the statement carefully! (not the story)**

John Pork was a lonely humanoid pig, ostracized by society and without friends. In hopes of making new acquaintances, he organized a party, but no one came. Feeling isolated and misunderstood, John tried to call the few friends he had, but no one answered. Among them was his best friend, another humanoid pig named Betty.
John began to withdraw even further, isolating himself in his apartment and refusing any connection with the outside world. His only solace was his phone, which he held tightly, hoping that someone, anyone, would call him.
But the phone remained silent, a bitter reminder of John's loneliness and isolation. Eventually, something strange happened. A familiar voice answered the phone; it was Betty, his best friend. John was stunned and happy to hear her voice, but at the same time, he was confused. How did she know he was looking for her?
Betty explained that she couldn't come to his party because she was busy with another activity, but she appreciated him a lot and was always there for him. John was touched and grateful, feeling less alone than before.
*-chat gpt*

# Task
You are given a matrix $N$ x $M$. 
There are $Q$ queries of the form:
> $query(x1, y1, x2, y2) =$  $MIEX^1$ of the rectangle $(x1, y1, x2, y2)$.
$x1$ and $x2$ are rows, and $y1$ and $y2$ are columns, $x1 \le x2$ and $y1 \le y2$

# Input data
The first line of the file `miex.in` contains $N$ and $M$.
The next $N$ lines contain $M$ numbers each, representing the matrix.
The next line contains $Q$, the number of queries.
The next $Q$ lines contain tuples of numbers in the form: *x1 y1 x2 y2*, representing the queries.

# Output data
In the file `miex.out`, print $Q$ lines, representing the answers to the queries, in order.

# Constraints and clarifications
* $N, M \le 500$
* $Q \le 2 \times 10^4$
* $1 \le$ values $ \le N \times M$ 
* **a value can appear multiple times in the matrix!!!**
* $^1MIEX$ of a set of values is defined in this problem as the smallest **non-zero** natural value that has an **even frequency**. 
* For $20\%$ of the score: $N, M \le 50$ and $Q \le 1000$

# Example
`miex.in`
```
5 5
1 3 2 5 4
4 4 6 9 10
3 2 8 1 10
1 2 3 4 5
12 12 3 4 5
4
1 1 2 3
4 1 4 5
1 1 5 5
3 2 4 3
```
`miex.out`
```
4
6
3
1
```
