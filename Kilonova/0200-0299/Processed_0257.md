Adriana is learning about surface filling problems at school. Today's problem involves filling a rectangle with a length of $N$ cm and a width of $3$ cm using squares with a side length of $1$ cm and squares with a side length of $2$ cm.

Adriana managed to solve the problem quite easily, but she realized that the problem has multiple solutions and is curious to find out the number of distinct ways to fill the rectangle with a length of $N$ cm and a width of $3$ cm, using squares with a side length of $1$ cm and squares with a side length of $2$ cm.

## Task
Help Adriana determine the number of distinct ways to fill the rectangle as described. Because this number can be very large, it is sufficient to find the remainder of dividing this number by $1\,000\,000\,007$.

# Input data
The input file `patrate.in` contains on the first line a natural number $N$.

# Output data
In the output file `patrate.out` you will write a single natural number, which represents the number of ways to fill the specified rectangle, modulo $1\,000\,000\,007$.

# Constraints and clarifications
* $3 \leq N \leq 1\,000\,000\,000$;
* For $30\%$ of the tests, $3 \leq N \leq 15$;
* For $60\%$ of the tests, $3 \leq N \leq 100\,000$;
* The tests are not the ones from the competition.

# Example 1
`patrate.in`
```
3
```
`patrate.out`
```
5
```

# Explanation

~[exemplu.png]

# Example 2

`patrate.in`
```
85
```
`patrate.out`
```
928344252
```