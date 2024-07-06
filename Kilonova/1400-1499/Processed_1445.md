Sure, here is the text translated into English while preserving the required formatting and structure:

---

It's no secret that Mireluș practices algorithm problems in his spare time. Recently, he discovered that a natural number \( N \), for which there are two non-zero natural numbers \( A \) and \( B \ (B>1) \) such that \( N = A^B \), is called a **_power_**. Mireluș set out to determine the number of **_powers_** in the interval \([X, Y]\), where \( X \) and \( Y \) are non-zero natural numbers.

As you probably already guessed, Mireluș couldn't solve this problem and decided to ask for the help of Olimpia D’Info. To make sure she doesn't make any mistakes either, he gave her a set of intervals and asked her to determine the number of **_powers_** corresponding to each interval.

# Task

Given the number of intervals \( T \) and for each of the \( T \) intervals the two endpoints, determine the number of powers corresponding to each interval given by Mireluș to Olimpia.

# Input data

The input file `puteri.in` contains on the first line the number of intervals \( T \), and on each of the next \( T \) lines, two non-zero natural numbers \( X \) and \( Y \), separated by exactly one space, representing the endpoints of the intervals.

# Output data

The output file `puteri.out` contains \( T \) lines. Each line will contain the number of powers that belong to the corresponding interval from the input file.

# Constraints and clarifications

* \( 1 \leq T \leq 131 \)
* \( 1 \leq X \leq Y \leq 10^{18} \)
* The interval \([X, Y]\) contains both numbers \( X \) and \( Y \).
* For \( 10\% \) of the tests \( Y \leq 5 \ 000 \).
* For another \( 25\% \) of the tests \( Y \leq 100 \ 000 \).
* For another \( 20\% \) of the tests \( Y \leq 10 \ 000 \ 000 \).

# Example

`puteri.in`
```
1
1 36
```

`puteri.out`
```
9
```

## Explanation

The 9 numbers are:

`1, 4, 8, 9, 16, 25, 27, 32, 36`

