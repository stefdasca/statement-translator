Petrică and Ionuț have invented a game with numbers and digits that they called Cifmaxmin. They have $n$ cards with numbers consisting of at least two digits and at most nine digits, from which Petrică chooses the even numbers and Ionuț chooses the odd numbers written on the cards. All the numbers on the cards have digits different from $0$. The game has the following rules:

- From each number on the drawn card, the smallest digit, called $c_{min}$, and the largest digit, called $c_{max}$, are chosen.
- For each even number, the largest number formed with the digits $c_{min}$ and $c_{max}$ is obtained.
- For each odd number, the smallest number formed with the digits $c_{min}$ and $c_{max}$ is obtained.
- Among the numbers determined by Petrică, the largest number is chosen, and among the numbers determined by Ionuț, the smallest number is chosen.
- After they have finished extracting the $n$ cards, each boy announces what number he obtained according to the game rules and how many cards he extracted.
- All the cards are used in the game: if a card has an even number, it will be chosen by Petrică, and if it has an odd number, it will be chosen by Ionuț.

# Task

Write a program that determines and displays four numbers, in this order: the number obtained by Petrică, how many cards Petrică extracted, the number obtained by Ionuț, and how many cards Ionuț extracted.

# Input data

The input file `cifmaxmin.in` contains on the first line a number $n$, representing the number of cards in the game. The second line of the file contains the $n$ natural numbers written on the cards, separated by a space.

# Output data

The output file `cifmaxmin.out` must contain four natural numbers, separated by a space, in this order: the number obtained by Petrică, how many cards Petrică extracted, the number obtained by Ionuț, and how many cards Ionuț extracted.

# Constraints and clarifications

- $1 < n \leq 1000$
- The numbers written on the cards consist of at least two digits and at most nine digits.
- All the numbers on the cards have digits different from $0$.
- The cards are chosen in the order in which they were arranged before the start of the game.
- There is at least one even number and at least one odd number among the numbers on the cards.

# Example 1

`cifmaxmin.in`
```
5
1839 47536 28 2459 2496
```

`cifmaxmin.out`
```
92 3 19 2
```

## Explanation

The numbers chosen by Petrică are: $47536$, $28$, and $2496$, from which he obtains the numbers $73$, $82$, and $92$. He extracted $3$ numbers and the largest number is $92$. Thus, from the number $47536$, the minimum digit is $3$ and the maximum digit is $7$, resulting in the number $73$, etc.  
The numbers chosen by Ionuț are $1839$ and $2459$, from which he obtains the numbers $19$ and $29$. He extracted $2$ numbers and the smallest number is $19$.