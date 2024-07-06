```markdown
Once upon a time, in a distant land, there lived a pig named John Pork. He never had a phone, but he wanted to talk to people and have friends. John Pork made many plans and saved money to buy his first phone. After many efforts, he managed to buy a mobile phone. He was so excited that he couldn't hold his joy for himself. He started calling people, but no one answered him. However, John Pork did not give up.
*-chat gpt*

# Task
Given an $N$ x $M$ matrix containing **all values from $1$ to $N$ x $M$**. 
There are $Q$ queries of the form:
> $query(x1, y1, x2, y2) = {MEX}^1$ of the rectangle $(x1, y1, x2, y2)$, where $x1$ and $x2$ are rows, and $y1$ and $y2$ are columns, $x1 \\le x2$ and $y1 \\le y2$.

# Input data
The first line of the file `mex.in` contains $N$ and $M$.
The next $N$ lines contain $M$ numbers each, representing the matrix.
The next line contains $Q$, the number of queries.
The next $Q$ lines contain tuples of numbers in the form: *x1 y1 x2 y2*, representing the queries.

# Output data
In the `mex.out` file, print $Q$ lines, representing the answers to the queries, in order.

# Constraints and clarifications
* $N, M \\le 1000$;
* $Q \\le 2 \times 10^5$;
* The $^1{MEX}$ of a set of values in this problem is defined as the minimum **non-zero** natural value that is not present in that set. 
* For $20\%$ of the score: $N, M \\le 50$ and $Q \\le 1000$.

# Example

`mex.in`
```
5 5
14 24 12 8 18 
22 10 17 9 19 
15  3  2 6  1 
20  7 25 11 4
13 23 16 21 5
3
1 1 5 5
3 2 3 5
4 4 5 5
```

`mex.out`
```
26
4
1
```
```
```