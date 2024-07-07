Gigel has a peculiar â€œbalanceâ€ which he wants to level. In fact, the device is different from any balance you have seen so far. Gigel's balance has two arms with negligible weight and length of $15$ each. From place to place, hooks are attached to these arms, on which Gigel can hang weights from his collection of $G$ distinct weights (natural numbers between $1$ and $25$). Gigel can hang any number of weights on any hook, but he must use all the weights he has.

Using his experience from participating in the National Informatics Olympiad, Gigel quickly managed to balance the scale, but now he wants to know in how many ways it can be balanced.

# Task

Knowing the placement of the hooks and the set of weights that Gigel has at his disposal, write a program that calculates in how many ways the balance can be leveled. It is assumed that it is possible to balance the scale (it will be possible on all tests given during evaluation).

# Input data

The input file `balanta.in` contains the following structure:

- the first line contains the number $C$ of hooks and the number $G$ of weights;
- the next line contains $C$ distinct integers, sorted in ascending order, ranging from $-15$ to $15$ inclusive, representing the locations of the hooks by their position on the X-axis relative to the center of the balance, assuming no weight is hung (so the balance is balanced and aligns with the $X$ axis; the absolute value of the distances represents the distance from the center of the balance, and the sign indicates the arm of the balance where the hook is attached, `-` for the left arm and `+` for the right arm);
- the next line contains $G$ distinct natural numbers sorted in ascending order, ranging from $1$ to $25$ inclusive, representing the values of the weights that Gigel will use to balance the scale.

# Output data

The output file `balanta.out` contains a single line, which contains a number $M$, the number of ways to place the weights that lead to balancing the scale.

# Constraints and clarifications

* $2 \leq C \leq 20$;
* $2 \leq G \leq 20$;
* the weights used have natural values between $1$ and $25$;
* the number $M$ required is between $1$ and $2 \ 000 \ 000 \ 000$;
* The balance is leveled if the sum of the products between the weights and the coordinates where they are placed is $0$ (the sum of the moments of the weights relative to the center of the balance is $0$).

# Example

`balanta.in`
```
2 4
-2 3
3 4 5 8
```

`balanta.out`
```
2
