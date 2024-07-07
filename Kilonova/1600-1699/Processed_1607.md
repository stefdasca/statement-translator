# Task

You are given a sequence of $n$ natural numbers, each with at most $9$ digits, and you need to answer the following tasks:

1. how many numbers in the sequence are palindromes;
2. how many numbers in the sequence would be palindromes if we arranged their digits conveniently;
3. find the maximum number of palindrome numbers with at least two digits that we could obtain if we arranged all the digits of the numbers in the sequence, forming **other numbers**, not necessarily the ones in the sequence and not necessarily $n$ numbers.

# Input data

The first line contains $n$, the number of numbers in the sequence. The next line contains the $n$ values of the sequence.

# Output data

The first line will contain the number of palindromes in the sequence, the second line will contain the number of numbers in the sequence that could be palindromes if their digits were arranged conveniently, and the third line will contain the maximum number of palindrome numbers we could obtain if we arranged all the digits of the numbers in the sequence, forming other numbers.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$;
* The numbers in the sequence have at most $9$ digits and at least $2$ digits;
* After arrangements, the numbers are not allowed to start with the digit zero;
* A palindrome number is a number that reads the same if its digits are reversed. For example, $121$ is a palindrome while $110$ is not.
* Task 1 is worth 30 points, task 2 is worth 30 points, and task 3 is worth 40 points. **To receive scores on separate tasks, you must follow the display format presented above.**

# Example 1

`stdin`
```
3
402 440 323
```

`stdout`
```
1
2
3
```

## Explanation

$323$ is the only palindrome number in the sequence.

Besides $323$, $440$ would also become a palindrome if we arranged its digits conveniently, as $404$ is a palindrome.

If we arranged the digits of the numbers in the sequence, forming the numbers $303$, $44$, $22$ and $40$, we would obtain $3$ palindrome numbers with at least two digits, which is the maximum possible answer.

# Example 2

`stdin`
```
7
161 3933595 49294 953393 732 393 888
```

`stdout`
```
4
5
12
