## Task

Can you handle the zombies? Have you ever thought about what a zombie apocalypse would be like? Perfect, you're in the right place! You are Death, one of the four horsemen of the apocalypse, and your task is to kill as many zombies as possible to populate your empire with souls. Being a perfectionist, you also want to eliminate all of them so as not to tarnish your title 'The Almighty Slasher'. It is known that your favorite weapon is the double-scythe, but to be optimal, you need to use the plasma shield. Let's divide the whole map into an infinite grid. Your shield is at height $1$ and with the left end at horizontal coordinate $1$, and the shield is in the shape of a rectangle with a width of $1$ and length $L$. Zombies are above you, at some predefined starting coordinates, represented by squares of $1×1$. Zombies move down by one square every second. Your moves every second consist of moving the shield left, right by one square, or staying in place. A zombie will be eliminated if, at the moment of reaching height $1$, it falls into the shield (formally, if its horizontal coordinate is included in the current interval of the shield $[start, start + L - 1]$). You need to display a series of shield movements so that you catch all the zombies! Let's get started!

## Input data

The input file `shield.in` will contain on the first line $N$ and $L$, representing the number of zombies and the length of the shield, respectively. The next $N$ lines will contain two numbers $H$ and $C$, representing the height and the horizontal coordinate of a zombie, respectively.

## Output data

The output file `shield.out` will contain on the first line a string of $K$ letters in the form "L", "R" or "S" which represent in which direction the shield will move in that second. (the character "L" will represent a movement to the left, the character "R" will represent a movement to the right, and the character "S" will represent staying in place for that moment of time. $K = the maximum line of a zombie - 1$)

## Constraints and clarifications

The coordinates of the enemies will be in the interval $[-10^6, 10^6]$

The length of the shield will be in the interval $[1, 10^6]$

Zombies are always at heights at least $2$

$1 \leq N \leq 10^5$

It is guaranteed that there is always a solution

Any solution will be scored.

## Example

`shield.in`
```
3 10
3 11
5 14
10 0
```

`shield.out`
```
RRRRLLLLL
```