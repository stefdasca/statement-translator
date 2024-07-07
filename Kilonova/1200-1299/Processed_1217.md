A treasure hunter has encountered a major problem. After long searches, he managed to discover a secret code that could help him build a key for the chest of a great treasure. The secret code is an integer with a maximum of $10$ digits. The shape of the chest key is somewhat unusual. It consists of multiple squares. For example, for the code $342784$, the key looks like this:

```
      3
    3 3 3
      3
      7
    7 7 7
  7 7 7 7 7
7 7 7 7 7 7 7
  7 7 7 7 7
    7 7 7
      7
```

Odd digits are selected from the secret code. With each of these odd digits, a square is formed. On the diagonal of the square, a number of digits equal to the value of the current corresponding odd digit from the code are written. The digits on the same line are separated by a space. All the digits in a square are identical. If the secret code does not contain any odd digit, the message â€œCufarul nu se deschideâ€ (The chest does not open) will be displayed on the screen.

# Task

Determine the key to the chest, starting from the secret code held by the treasure hunter. Display the key to the chest.

# Input data

The file `comoara.in` contains one line with $n$, the secret code.

# Output data

The file `comoara.out` will contain the encoding of the secret code.

# Constraints and clarifications

* $1 \leq n \leq 2 \cdot 10^9$;

# Example 1

`comoara.in`
```
2345861
```

`comoara.out`
```
    3
  3 3 3
    3
    5
  5 5 5
5 5 5 5 5
  5 5 5
    5
    1
```

## Explanation

The odd digits in the given number are $3$, $5$, and $1$, so the first square is constructed with the digit $3$ and has $3$ digits of $3$ on the diagonal. The second square is constructed with the digit $5$ and has $5$ digits of $5$ on the diagonal. The third square is constructed with the digit $1$.