```markdown
A group of $N$ angels gathered in a circle - each of them stands on a cloud, at a certain known height. The clouds are numbered in order from $1$ to $N$. The angels will talk "on equal terms" and, aiming to be at the same height, they do not miss the opportunity to play a little. The game consists of winking at each other in a certain order: the "emitter" will be the angel who is closest to the ground, and if there are more at the same minimum height, then the one who stands on the cloud with the smallest order number will emit.

The emitter will look at all the others in order and will wink only at those above him: the angel who receives the signal will reduce the height of his cloud by a value equal to the height where the emitter's cloud is. In the next round, a new emitter is chosen (by the same rule) who will resume the series of "winks". In one step, the emitter will wink once at each angel (if they are higher than him). The game continues until, after a number of such steps, all the angels reach the same height, $H$.

# Task

Write a program that calculates and displays the final height ($H$).

# Input data

The first line of the input file `ingerasi.in` contains a natural number $n$, representing the number of angels. The next line contains, in order, $N$ natural numbers representing the heights of the clouds.

# Output data

The first line of the output file `ingerasi.out` will contain only the value $H$, representing the height at which the clouds finally are.

# Constraints and clarifications

* $1 \leq n \leq 30$;
* The heights of the clouds are natural numbers between $1$ and $10^9$.

# Example 1

`ingerasi.in`
```
3
12 4 10
```

`ingerasi.out`
```
2
```

## Explanation

In the first stage, $2$ is the emitter (at height $4$)

* $2$ winks at $1$ and he will reach the height $12 - 4 = 8$
* $2$ winks at $3$ and he will reach the height $10 - 4 = 6$

In the second stage, $2$ is still the emitter (at height $4$)

* $2$ winks at $1$ and he will reach the height $8 - 4 = 4$
* $2$ winks at $3$ and he will reach the height $6 - 4 = 2$

In the third stage, $3$ is the emitter (at height $2$)

* $3$ winks at $1$ and he will reach the height $4 - 2 = 2$
* $3$ winks at $2$ and he will reach the height $4 - 2 = 2$

The game ends because all the angels are at the same height, $H = 2$
```