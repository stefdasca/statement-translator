```markdown
By convention we call a _weighted arithmetic expression_ an expression constructed as follows:
- the expression contains integers of at most $2$ digits separated by commas;
- we call **k-sequence** an enumeration of $k$ numbers separated by commas $(k \geq 1)$;
- an expression may contain one or more $k$-sequences;
- the expression uses round brackets and square brackets.

The evaluation of the expression is done according to the following rules:

- if the expression contains a single $k$-sequence, then the result of the expression is represented by the sum of the $k$ numbers (**Example:** $2,4,1 = 2+4+1 = 7$);
- if in the expression we encounter a $k$-sequence delimited by round brackets, the result of evaluating this $k$-sequence will be represented by the maximum sum of a subarray belonging to the $k$-sequence, where by subarray we mean a succession of numbers located on consecutive positions in the sequence (**Example:** $(-2,4,-1,3,-2,-3,2) =>$ the subarray with the maximum sum is $4,-1,3$ whose sum is equal to $6$);
- if in the expression we encounter a $k$-sequence delimited by square brackets, the elements of the $k$-sequence being numbered $1,2,..,k,$ the result of evaluating this $k$-sequence will be represented by the value of the element located at position $[ \frac{k + 1}{2} ]$ if the sequence were ordered in ascending order (**the median of a sequence**) (**Example:** $ [-2,9,10,3,5]  =>$ the ordered sequence $[-2,3,5,9,10] =>$ and the value of the expression is equal to $5$).
- the evaluation of the brackets is done from the inside out.

# Task

Given a weighted arithmetic expression, determine:
- how many integers the arithmetic expression contains;
- what is the value of the arithmetic expression.

# Input data

The input file `expresie.in` contains on the first line a string that represents a weighted arithmetic expression.

# Output data

The output file `expresie.out` will contain on the first line the number of integers in the expression, and on the next line will be printed a number that represents the value of the arithmetic expression.

# Constraints and clarifications

* the expression is considered correct
* $3 \leq$ length of an expression $\leq 100\ 000$
* the string encoding the expression may only contain the following characters: digits, round brackets and square brackets opened and closed, comma, minus character
* solving the first requirement earns $20\%$ of each test's value
* $10\%$ of tests will not contain brackets
* $20\%$ of tests will not contain nested brackets

# Example 1

`expresie.in`
```
2,(2,-4,1,-1,5)
```

`expresie.out`
```
6
7
```

## Explanation

The expression contains $6$ integers.
The value of the expression is: $2+5 = 7$

# Example 2

`expresie.in`
```
(3,-1,4),[2,3,1,8]
```

`expresie.out`
```
7
8
```

## Explanation

$6 + 2$

# Example 3

`expresie.in`
```
(2,-1,[1,2,3,4,5],-4,1)
```

`expresie.out`
```
9
4
```

## Explanation

$(2,-1,3,-4,1) = 4$
```
```