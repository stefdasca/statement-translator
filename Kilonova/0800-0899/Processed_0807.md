Hansel and Grettel, lost in the forest, know that their only chance of survival is to find and enter the Gingerbread Castle. The castle gate is closed, and to enter it they need a magic word and an enchanted number.

The Good Fairy sees the children and, wanting to help them, says:  
“Keep walking forward, and along your path you'll encounter trees with characters representing letters or digits written on their trunks. The magic word is formed from all the letter characters in the order they appear, but all written in uppercase. The enchanted number is the smallest number with distinct digits that can be formed from the digit characters.”

# Task

To help Hansel and Grettel enter the Gingerbread Castle, write a program that reads a natural number $n$, then $n$ characters and determines:

* the magic word;
* the enchanted number;

# Input data

The first line of the input file `magic.in` contains a natural number $n$, representing the number of characters written on the trees. The second line contains $n$ characters separated by spaces, representing the characters written on the trees.

# Output data

The output file `magic.out` will contain two lines:

* the first line will contain a string of uppercase letters, representing the magic word;
* the second line will contain a natural number with distinct digits, representing the enchanted number.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$;
* The characters are only digits or lowercase letters of the English alphabet.
* Among the $n$ characters, there is always at least one letter and at least one digit.
* Each tree has a single character written on it.
* The enchanted number always starts with a digit different from zero.
* Solving the task a) grants 40% of the score, solving task b) grants 60% of the score.

# Example 1

`magic.in`
```
6
c 2 5 5 b 2
```

`magic.out`
```
CB
25
```

## Explanation

The smallest number with distinct digits that can be obtained is $25$.

# Example 2

`magic.in`
```
8
c a 5 0 b 2 5 d
```

`magic.out`
```
CABD
205
```

## Explanation

The smallest number with distinct digits that can be obtained is $205$.