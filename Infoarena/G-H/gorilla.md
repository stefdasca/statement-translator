## Task

You might remember the old game in QBasic, gorilla.bas. In case you don't, the game was about two gorillas throwing explosive bananas at each other. Each gorilla was controlled by one of the two players. Each player could choose the angle and speed of the throw, and the banana followed a parabolic trajectory. As if finding the right angle and speed to hit the opponent's gorilla was not hard enough, there were also some buildings in the game, which could block the banana's trajectory. This time you find yourself nearly at the end of a game where, by coincidence, both gorillas are located at the same height (equal to 0). To be more precise, your gorilla is a point located at coordinates $(0, 0)$, and the opponent's gorilla is a point located at coordinates $(d, 0)$. Between the two gorillas, there are $N$ buildings (vertical segments) of various heights. You want to finish the game as quickly as possible, so you want the next throw to be the last one. Therefore, the banana (which is also a point) must be thrown in such a way that it hits the opponent's gorilla but not the buildings (although it can touch the top of any building). Moreover, to showcase your superior skills to your opponent, you want the speed $v$ with which you throw the banana to be minimal (but you can choose any angle between $0$ and $\pi$). When solving this problem, you will use the value of the gravitational acceleration $g$ (provided in the input file), as well as the following laws of motion:

## Input data

The first line of the input file `gorilla.in` contains an integer $T$, representing the number of upcoming tests. The first line of each test contains 3 numbers, separated by spaces: an integer $d$, a real number $g$, and an integer $N$. The $i$-th of the next $N$ lines contain 2 integers, separated by a space: $X_i$ and $H_i$. $X_i$ is the $X$ coordinate of the $i$-th building, and $H_i$ is its height. Additionally, $X_i < X_{i+1}$.

## Output data

For each of the $T$ tests, in the order from the input file, print to the output file `gorilla.out` one line containing the minimum value of speed necessary to throw the banana. Print this value with 3 decimal places, rounded (up or down) depending on the fourth decimal place.

## Constraints and clarifications

$1 \leq T \leq 10$

$0 \leq g \leq 10$

$1 \leq d \leq 1\ 000\ 000$

$0 \leq N \leq 50\ 000$

$1 \leq X_i < d$

$1 \leq H_i \leq 1\ 000\ 000$

## Example

`gorilla.in`
```
2
1 9.8 0
1000 1 1
500 10000
```

`gorilla.out`
```
3.130
141.466
```