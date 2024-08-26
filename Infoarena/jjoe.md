# Jjoe

Joe is a frog who loves to jump a lot. In fact, that's all he does: he jumps forward and backward along the axis of the integer numbers (a straight line marked with all integers, both positive and negative). Initially, Joe is at the point marked with $0$. From here, he can jump in the positive or negative direction of the axis by a distance equal to $x_1$ or $x_2$. From the point where he has arrived, he can jump again a distance equal to $x_1$ or $x_2$, in the positive or negative direction $\dots$ Joe wants to reach the point marked with the number $P$ after exactly $K$ jumps. You need to decide if this is possible.

## Input data

The input file `jjoe.in` will contain $4$ integers: $x_1$, $x_2$, $P$, and $K$, separated by a space.

## Output data

The first line of the output file `jjoe.out` will contain the string "DA" if Joe can reach the point marked with $P$ after exactly $K$ jumps or "NU" otherwise. If the answer is "DA", the second line will contain $4$ integers, separated by a space: $P_1$, $N_1$, $P_2$, $N_2$. $P_1$ is the number of jumps of distance $x_1$ Joe made in the positive direction of the axis. $N_1$ is the number of jumps of distance $x_1$ Joe made in the negative direction of the axis. $P_2$ is the number of jumps of distance $x_2$ Joe made in the positive direction of the axis. $N_2$ is the number of jumps of distance $x_2$ Joe made in the negative direction of the axis. The $4$ numbers must satisfy the relationships:
$$P_1 * x_1 - N_1 * x_1 + P_2 * x_2 - N_2 * x_2 = P$$
$$P_1 + N_1 + P_2 + N_2 = K$$
If there are multiple solutions, you can display any of them.

## Constraints and clarifications

$$0 < x_1, x_2 < 40 000$$
$$-40 000 < P < 40 000$$
$$0 \leq K < 2 000 000 000$$

## Example

`jjoe.in`
```
2 3 -1 12
```

`jjoe.out`
```
DA
1 0 5 6
```