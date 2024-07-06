Ionel is a great enthusiast of the game Tribes. The idea of the game is that each player owns a few villages in a region at some point and tries to dominate that region by conquering villages owned by other players in that area. Ionel has come to own many villages and finds it increasingly difficult to organize his attacks.

At this moment, he has $n$ villages, numbered from $1$ to $n$, and is about to organize coordinated attacks on enemy villages. Ionel knows how long it takes for the army from each of his villages to reach each enemy village.

Ionel has chosen two enemy villages $X$ and $Y$ that he wants to attack. He thought of the following scenario: select $k$ of his different villages and send all armies from them to attack one of the two enemy villages. All $k$ attacks must be coordinated, meaning all troops from the $k$ villages must arrive at the attacked village at exactly the same time (for this, they can start at different moments of time). It is known that after this attack, enough troops survive from each of Ionel’s villages to return to their original village and can participate in a new attack. Then Ionel will select again $k$ of his villages, among which may be villages that participated in the first attack, and launch the offensive on the other enemy village. Again, the armies coming from the $k$ villages must arrive at the objective they are attacking at the same time.

Ionel wants the time elapsed from the departure of the first army until the arrival of the armies at the second attacked village to be as short as possible to surprise the enemy this way.

We will consider that Ionel’s first army will leave for the attack at $00:00$ and all $2 \cdot k$ attacks will reach the target by $23:59$ of the same day at the latest.

The time required for an army to return to the original village after attacking an enemy village is equal to the time required to travel from the original village to the attacked village, and the attack is instantaneous (does not consume time).

# Input data

The input file `triburi.in` contains:

* The first line contains two natural numbers $n$ and $k$ representing the number of villages owned by Ionel and respectively the number of armies that must participate in the attack on each enemy village.
* The next $n$ lines contain four numbers $h_{1_i}$, $m_{1_i}$, $h_{2_i}$, $m_{2_i}$, $(i = 1, 2, \dots, n)$ separated by a space, representing the time (expressed in hours and minutes) required for the troops from the $i$-th village to reach the enemy village $X$ $(h_{1_i}, m_{1_i})$ and respectively the time (expressed in hours and minutes) required for the troops from the $i$-th village to reach the enemy village $Y (h_{2_i}, m_{2_i})$.

# Output data

The output file `triburi.out` will contain on the first line two natural numbers $h$ and $m$, separated by a space representing the hour and minute of the arrival of the troops at the second attacked village.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$
* $1 \leq k \leq n$
* Insignificant zeroes are not shown in hours or minutes, so the hour $06:05$ will be expressed as $6 \ 5$.

# Example

`triburi.in`
```
6 3
1 10 2 34
2 16 1 35
3 20 1 40
2 17 1 32
3 15 3 46
0 29 1 15
```

`triburi.out`
```
3 15
```

## Explanation

First, village $Y$ will be attacked with troops from villages $3$, $4$, and $6$, in this order, with the arrival time at village $Y$ being $1:40$. Then village $X$ is attacked with troops from villages $1$, $2$, and $5$, and the armies arrive at village $X$ at $3:15$. It is observed that the troops from village $6$ attack village $Y$, the survivors return to their village, and then attack village $X$.