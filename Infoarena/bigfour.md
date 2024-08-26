## Big Four

You have an accountant friend who asked you to spend an afternoon with his children, and you agreed. Now you are trying to play with them, but apparently, most of the games they play have a financial background. Today, they want to play the following game:
- There are $4$ companies, each having a capital, which is a natural number.
- At each step, the player can choose two companies with capital $A$ and $B$, respectively, and perform a merger. Thus, the two companies will no longer exist, and in their place, a single company with capital equal to $A + B$ will be created.
- Due to certain strange regulations, this operation can only be performed if $|A - B| \leq D$, for a certain $D$ set at the beginning of the game.
- The goal is that in the end, there is only one company. This game is quite boring for you, but they are young and can do this all day. You are considering writing a short program to analyze multiple game configurations and decide for each whether there is a solution (i.e., if there is a sequence of steps such that in the end only one company remains).

## Input data

The input file `bigfour.in` will contain on the first line the value $T$, representing the number of tests in the file. The next $T$ lines will contain $5$ natural numbers each: representing, in order, the value $D$, and the capital of the $4$ companies in the game.

## Output data

The output file `bigfour.out` will contain $T$ lines, each containing the string "DA" if the corresponding test has a solution, and "NU" if the test does not have a solution.

## Constraints and clarifications

All values in the file (including $T$) are natural numbers in the range $[1, 100]$.

## Example

`bigfour.in`
```
2
9 5 8 20 43
10 5 8 20 43
```

`bigfour.out`
```
NU
DA
```