# Critical Tunnels

Algorel has a network of underground tunnels in his basement, frequented by rats. The network consists of $N$ shelters numbered from $1$ to $N$ and $M$ tunnels between them. Shelters $1$ and $N$ connect to the surface, being the only places in the network with this property (no other shelters or tunnels have an exit to the surface). Algorel wants to send the maximum number of cats into the network. The cats enter through shelter $1$ and exit through shelter $N$. No cat can remain in the network. Each tunnel has a known resistance, that is, the maximum number of cats that can pass through it without collapsing. If a cat passes through a tunnel with non-zero resistance, its resistance decreases by one unit. Algorel noticed that there are certain tunnels with the property that if their resistance increases while the resistance of the other tunnels remains the same, the maximum number of cats he can send through the network will increase as well. He has named such tunnels critical tunnels.

## Task

Given the network in Algorel's basement, determine the critical tunnels.

## Input Data

The first line of the file `critice.in` contains the natural numbers $N$ and $M$ representing the number of shelters and the number of tunnels in the underground network. The next $M$ lines contain three natural numbers separated by spaces, $A$ $B$ $C$, with the meaning: between shelters $A$ and $B$ $(A \neq B)$ there is a tunnel with resistance $C$.

## Output Data

The first line of the output file `critice.out` contains a natural number $K$ representing the number of critical tunnels in Algorel's network. The next $K$ lines each contain a natural number representing the indices of the critical tunnels. The indices will be sorted in ascending order. The tunnels are numbered from $1$ to $M$ according to their order in the input file.

## Constraints and Clarifications

$1 \leq N \leq 1000$ 

$1 \leq M \leq 10000$ 

Resistances are natural numbers less than or equal to $10000$

There is at most one tunnel between any two nodes

Any tunnel can be traversed in both directions

For $50\%$ of the tests $M \leq 1000$

## Example

`critice.in`

```
5 6
2 1 2
2 3 3
3 5 4
1 4 7
4 3 2
4 5 6
```

`critice.out`

```
2
1
4
```
