The Unleashed Dacians have discovered that Mihai Eminescu is alive and is being held captive by the antidacians in a bunker in the Hoia Forest. Their leader, Feliciu Graur, has decided to initiate a fight to liberate the Poet.

The Dacians will head to the battlefield one by one. A Dacian will not desert before reaching the battlefield if and only if the Dacian who started before him is stronger than he is.
Feliciu wants to send them in an order that results in the highest possible total power during the fight. Determine the maximum total power.

# Input data
The input file `padure.in` will contain in the first line the integer $N$, representing the number of Dacians, and in the second line the integers $p_1, p_2, ..., p_N$, separated by a space, representing the power of each Dacian.

# Output data
The output file `padure.out` will contain an integer, representing the maximum total power that can be obtained in the fight.

# Constraints and clarifications
* $1 \leq N \leq 10^5$
* $1 \leq p_i \leq 10^9, \forall i \in [1, n]$
* For tests worth $20$ points, $N \leq 10^3$ and $p_i \leq 10^4, \forall i \in [1, n]$.
* For other tests worth $30$ points, $p_i \leq 10^7, \forall i \in [1, n]$.
* For other tests worth $10$ points, $p_1, p_2, ..., p_N$ are distinct.
* For other tests worth $40$ points, there are no additional constraints.
* The total power in the fight is equal to the sum of the powers of the Dacians present on the battlefield.
* The first Dacian to go to the battlefield will always desert.
* The leader does not participate in the fight and is not included in the $N$ Dacians in the input file.

# Example 1

`padure.in`
```
2
4 4
```

`padure.out`
```
0
```

# Example 2

`padure.in`
```
3
5 3 5
```

`padure.out`
```
3
```

# Example 3

`padure.in`
```
4
2 2 2 1
```

`padure.out`
```
1
```

# Example 4

`padure.in`
```
4
1 15 15 1
```

`padure.out`
```
2
```

## Explanations

In the first example, both Dacians will desert, no matter what order they are sent in. The first Dacian to leave will always desert (see the second observation). The second Dacian will desert because his power $(4)$ is equal to the power of the Dacian who left before him $(4)$, no matter the order in which they are sent.

In the second example, Feliciu can maximize the total power by first sending the first Dacian in the input file (power $5$), then the third (power $5$), and then the second (power $3$). The first Dacian to leave will always desert (see the second observation). The second Dacian to leave will desert because he has a power of $5$, and the one who left before him has the same power of $5$, and $5$ is not greater than $5$. The last Dacian to leave will not desert because the one who left before him has a greater power $(5)$ than his $(3)$. Since only the last Dacian sent reaches the fight, the total power is equal to his power, which is $3$. No order results in a total power greater than $3$.

In the third example, Feliciu can maximize the total power by sending the Dacians in the order from the input file. The first Dacian to leave will always desert (see the second observation). The second to leave will desert because he has a power of $2$, and the one who left before him also has a power of $2$, so he is not stronger than him. The third will desert for the same reason. The last Dacian to leave will not desert because the one who left before him has a higher power $(2)$ than his $(1)$. Since only the last Dacian sent reaches the fight, the total power is equal to his power, which is $1$. No order results in a total power greater than $1$.

In the fourth example, Feliciu can maximize the total power by first sending the second Dacian from the file (power $15$), then the last one (power $1$), then the third (power $15$) and finally the first (power $1$). The first Dacian to leave will always desert (see the second observation). The second Dacian to leave will not desert because his power is $1$, and the one who left before him has a power of $15$, so he is stronger $(15 > 1)$. The third Dacian will desert because he has a power of $15$, and the one who left before him has a power of $1$, so he is not stronger ($1$ is not greater than $15$). The last Dacian will not desert because the one who left before him has a higher power $(15)$ than his $(1)$. Since the second and fourth Dacians (in the order they leave) are the ones who reach the fight, with the other two deserting, the total power is equal to the sum of their powers: $1+1=2$. No order results in a total power greater than $2$.