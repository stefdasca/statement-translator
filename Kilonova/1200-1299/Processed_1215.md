The text you provided is a competitive programming problem statement in Romanian. Below is the translated version in English, while preserving the original syntax, structure, and format:

---
Prince Algorel is in trouble again: he was captured by the Black Spânul while trying to save the princess and is now locked up in the Big Tower. Algorel can escape if he finds the magic combination that can open the tower gate. The prince knows how to form this magic combination: he must use __all__ the digits written on the tower door to obtain two palindromic numbers, so that their sum is minimal, and this sum is the magic combination that will unlock the door. The first palindromic number must have at least $L$ digits, and the second can have any length different from $0$. The formed palindromic numbers cannot start with the digit $0$. Now, you step in as his most skilled friend in algorithms. Through his new super-phone, the prince transmits the number of occurrences of each digit on the tower door as well as the minimum length $L$ of the first number, and you must send him as quickly as possible the numbers with which he can achieve the magic combination.

# Task

Given the necessary data, find two palindromic numbers with which the magic combination can be obtained.

# Input data

The first line of the file `pal.in` contains an integer $L$ representing the minimum length of the first number.

The next $10$ lines: the $i+2$-th line will contain an integer representing the number of occurrences of the digit $i$, for $i$ ranging from $0$ to $9$.

# Output data

The first line of the output file `pal.out` contains the first palindromic number, and the second line contains the second palindromic number. If there are multiple solutions, only one of them will be written.

# Constraints and clarifications

* In total, there will be at most $100$ digits
* $1 \leq L < 100$ and $L$ will be less than the total number of digits
* For the test data, __there will always be a solution__: two numbers can be formed from the digits written on the tower door that start with a digit different from $0$, and the first number has at least $L$ digits
* A number is palindromic if it matches its reversed form. For example, $12\ 321$ and $7\ 007$ are palindromic numbers, while $109$ and $35\ 672$ are not
* For $30$\% of the tests, the total number of digits will be at most $7$, for another $40$\% of the tests the total number of digits will be at most $18$, and for the remaining $30$\% of the tests the total number of digits will be at least $30$
* Each line in the input file and the output file ends with a newline marker

# Example

`pal.in`
```
5
3
2
3
0
0
0
0
0
0
0
```

`pal.out`
```
10001
222
```

# Explanation

For this example, we have $L = 5$

There are $3$ $0$ digits, $2$ $1$ digits, and $3$ $2$ digits. The digits from $3$ to $9$ are missing from the tower door.

The two palindromic numbers with which the magic combination is generated are $10\ 001$ and $222$. The magic combination will be their sum, namely $10\ 223$ (which is the minimal sum we can obtain).

---

Everything should be correctly translated and any potential grammar or syntax errors fixed according to the rules of the English language.