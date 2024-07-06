Sure, here's the translated competitive programming problem statement:

---

There are only a few weeks left until the vacation. Arriving at a toy store, Robert asks his father to buy him the nicest remote-controlled car. His father tells him that he has not behaved well during the year and does not deserve this toy, but after intense disputes, he decides to give him another chance only if he solves the following problem: Given a string $S$, can we obtain a palindrome from this string by deleting just one character? Robert is not very good at algorithms, so he asks you very much to solve the problem for him so that he can play with the remote-controlled car.

# Task

Find if from a string $S$, it is possible to obtain a palindrome by deleting only one character.

# Input data

The input file `litera.in` contains the first line a value $T$ representing the number of test cases. The following $T$ lines will contain one string representing the question addressed to Robert by his father.

# Output data

The output file `litera.out` will contain $T$ lines with the answer `YES` if it is possible to obtain a palindrome by deleting one single character and `NO` if it is not possible.

# Constraints and clarifications

- $T \leq 100$
- The size of the string $\leq 100\ 000$
- For $10\%$ of the points, the size of the string $\leq 1\ 000$
- The string contains characters from ***a*** to ***z***.
- The size of the string after deleting one character will be smaller than it was before.

# Example 1

`litera.in`
```
4
aaa
abc
abdbca
abba
```

`litera.out`
```
YES
NO
YES
YES
```

## Explanation

* For the first example (`aaa`): We can delete any `a`, and the resulting string is `aa` which is a palindrome.
* For the second example (`abc`): It is not possible to remove exactly one character and obtain a palindrome.
* For the third example (`abdbca`): We delete the character `c`, and the resulting string is `abdba` which is a palindrome.
* For the fourth example (`abba`): We delete `b`, obtaining `aba` which is a palindrome.

---

Please, let me know if you need any further assistance!