# Zebughil

Zebu, during his downtime at his chicken farm when he doesn't have to feed the chickens or clean, is planning to create an ovo-lactarian monopoly in Bistrita Nasaud county. The first step to fulfilling this dream involves building a new hall for the chickens. To build his dream hall, he bought $N$ large stone blocks that he wants to bring to his firm for processing. His friend Ghilau has a transport company and offers his services for free on the condition that Zebu uses the minimum number of trucks to transport the stone blocks. Each truck from Ghilau's company has the same maximum transport capacity $G$, while Zebu's blocks have weights $z_i$. A truck will be used only once to avoid wearing it out too much, and a stone cannot be cut.

## Task

Find out for Zebu what is the minimum number of trucks he needs to use for transporting the blocks.

## Input data

The input file `zebughil.in` will contain three tests.
The first line of the file will contain two integers $N$ and $G$ separated by a space, representing the number of stone blocks
and the maximum weight supported by a truck, respectively.
The next line will contain $N$ integers separated by a single space representing the weights of the blocks.
The second test will start from line 3
and will be structured the same,
and the third test will start from line 5.

## Output data

The output file `zebughil.out` will contain three lines, each containing a single integer representing the minimum number of trucks needed for the corresponding test on that line.

## Constraints and clarifications

$1 \leq N \leq 17$

$0 \leq z_i \leq G \leq 2000000000$

For tests worth $70$ points,

$0 \leq z_i \leq G \leq 500$

No partial scores are awarded.

## Example

`zebughil.in`
```
4 10
6 7 5 4
4 4
2 3 1 2
1 5
1 3 2 1
```

`zebughil.out`
```
3
2
1
```

## Explanation

: for the first test, we can distribute the blocks into the groups $\{6, 4\}$ $\{7\}$ $\{5\}$, for the second test into $\{2, 2\}$ $\{3, 1\}$, and for the third into $\{1\}$.