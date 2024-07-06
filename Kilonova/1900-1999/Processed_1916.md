Tassadar is playing blind man's bluff with Zeratul and needs to find him. Both Tassadar and Zeratul are at two distinct points on the plane. To find Zeratul, Tassadar must be at a distance of at most one meter from him. Tassadar successively takes steps of one-meter length, and after each step, he can maintain the direction or take a step in another direction. Since the game would be too hard for Tassadar, Zeratul will tell him after each step whether he is getting closer or not. Help Tassadar find Zeratul as quickly as possible!

# Interaction

To solve this problem, you must have the following function in your source code:
```cpp
void play();
```
This function will be called once at the beginning of the program execution. From within this function, you can call the following function, provided by the grading program, as often as needed:
```cpp
int makeStep(double direction);
```
By calling this function, you take a step of one meter in the direction expressed in radians. In other words, the $x$ coordinate increases by $cos(direction)$, and the $y$ coordinate increases by $sin(direction)$. This function will return the following values:
- $-1$ if, after this step, you are at a distance of at most $1 + 10^{-9}$ from Zeratul's position
- $1$ if, after this step, you get at least $10^{-9}$ closer to Zeratul's position
- $0$ if you are not in any of the two above cases

Once the function returns $-1$, you no longer have the right to call it. Otherwise, you will receive $0$ points for that test.

# Constraints and clarifications

- $1 < D \\leq 100 \ 000$, where $D$ is the distance between Tassadar and Zeratul at the initial moment
- Throughout the game, Zeratul will remain stationary
- The score awarded for a test will be:
  - $100\%$ of the points if you call the `makeStep` function at most $ceil(D) + 50$ times
  - $60\%$ of the points if you call the `makeStep` function at most $ceil(D) + 100$ times
  - $20\%$ of the points if you call the `makeStep` function at most $ceil(1.5 \cdot D) + 100$ times
  - $0\%$ of the points if you call the `makeStep` function more than $ceil(1.5 \cdot D) + 100$ times

# Example

Grader: `play()`
Contestant: `makeStep(1.5707963)`
Grader: `return 1`
Contestant: `makeStep(1.5707963)`
Grader: `return 1`
Contestant: `makeStep(1.5707963)`
Grader: `return 0`
Contestant: `makeStep(-1.5707963)`
Grader: `return 1`
Contestant: `makeStep(0.0)`
Grader: `return 1`
Contestant: `makeStep(0.0)`
Grader: `return -1`

## Explanation

Initially, Tassadar is at coordinates $(0, 0)$, and Zeratul is at $(2, 1.7)$. Tassadar takes two steps North and gets closer to Zeratul in both cases. When he takes a third step North, he moves farther away. Then, he takes a step South and gets closer to Zeratul. Next, he takes a step East and gets closer to Zeratul, and after the second step East, Tassadar is less than a meter away from Zeratul and finds him.