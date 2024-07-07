
Artanis, the commander of the ship **Spear of Adun**, needs to contact the command center located on the planet **Aiur**. Specifically, he needs to send an encoded message consisting of a bit. This message will be transmitted from the computer on the ship to the computer in the command center on **Aiur** through an intergalactic network of computers.

The network of computers can be viewed as a directed graph with `V` nodes and `E` edges. Each edge is of the form `(x, y, p0, p1)` and signifies: "computer `x` can send messages to computer `y`, a bit `0` is correctly transmitted with probability `p0`, and a bit `1` is correctly transmitted with probability `p1`." A bit is correctly transmitted if it retains the same value both in the sending computer and in the receiving computer.

When a computer receives a message, it will randomly and with equal probability choose one of its outgoing edges and forward the message through that edge.

Artanis would like to know the probability that the bit `0` and the bit `1` will be correctly transmitted from the computer on **Spear of Adun** to the computer on **Aiur**.

# Input data
The first line of the input file `network.in` will contain the numbers `V` and `E`. The next `E` lines will contain four numbers `(x, y, p0, p1)`, signifying an edge in the network.

# Output data
In the output file `network.out`, the first line will contain the probability that the bit `0` is correctly transmitted, and the second line will contain the probability that the bit `1` is correctly transmitted to the computer on Aiur.

# Constraints and clarifications
* `1 \leq V \leq 5\ 000`
* `0 \leq E \leq 50\ 000`
* `0 \leq p0, p1 \leq 1.0` for all edges, and these probabilities will be given in the input file with at most two decimals
* We cannot choose a subset of more than `70` computers such that each computer in the subset is accessible from every other computer in that subset
* The computers in the network are represented by indices from `0` to `V-1`
* The computer on the ship **Spear of Adun** is numbered `0`, and the computer on Aiur is numbered `V-1`
* The computer on Aiur will have an out-degree of `0` and will be accessible (directly or indirectly) from all computers in the network
* For any two computers `x` and `y` there will be at most one directed edge from `x` to `y` and at most one directed edge from `y` to `x`, and there will be no edges from a computer to itself
* The solution is considered correct if it differs from the correct answer by at most `0.00001`
* It is guaranteed that for tests worth `20` points, there will be no two distinct computers `x` and `y` such that `x` is accessible from `y` and `y` is accessible from `x`
* It is guaranteed that for tests worth another `40` points, `V \leq 100`

# Examples

`network.in`
```
4 3
0 1 1.0 0.5
1 2 0.2 1.0
2 3 0.1 0.0
```

`network.out`
```
0.8200000
0.0900000
```

Explanations
---

If we transmit the bit `1` from node `0` to node `3`, there is only one correct transmission: we incorrectly transmit the bit on the edge `(0→1)` with a probability of `0.5`. Thus, computer `1` receives the bit `0`. We correctly transmit the bit `0` from computer `1` to computer `2` on the edge `(1→2)` with a probability of `0.2`. Thus, computer `2` receives the bit `0`. We incorrectly transmit the bit `0` from computer `2` to computer `3` on the edge `(2→3)` with a probability of `0.9`. Therefore, the computer on Aiur receives the bit `1` with a probability of `0.5 * 0.2 * 0.9 = 0.09`. A similar process is followed if we want to transmit the bit `0` to the computer on Aiur.
