The city hall of ioliPest city is powered by electricity through a network that is several decades old, and it has significant power losses on the lines. The network consists of nodes and connections between some pairs of nodes. However, the network has a special structure, similar to series-parallel resistance networks, and contains two special nodes called left node and right node. Therefore, the network has a structure that corresponds to one of the following 3 cases:
* **$2$ nodes connected by a connection** (we will call this structure a "basic network"); in the figure, the left node of this network is marked with $T_1$, and the right node with $T_2$;
~[img1.png]
* **series connection of two networks**; considering two networks $R_1$ and $R_2$, they are connected in series by overlapping the right node of $R_1$ over the left node of $R_2$; the left node of the resulting network is the left node of $R_1$, and the right node of the resulting network is the right node of $R_2$;
~[img2.png]
* **parallel connection of two networks**; considering two networks $R_1$ and $R_2$, they are connected in parallel by overlapping the left node of $R_1$ over the left node of $R_2$ and the right node of $R_1$ over the right node of $R_2$; the left node of the resulting network is given by the overlapping of the left nodes of networks $R_1$ and $R_2$, and the right node of the resulting network is given by the overlapping of the right nodes of networks $R_1$ and $R_2$; as a result of the parallel connection, multiple connections can occur between the left node and the right node of the resulting network (for example, in the case of a parallel connection of two "basic networks").
~[img3.png]

In preparation for integration into the European Union, funds have been allocated for changing the network. The operation of changing the network involves, in the first stage, the elimination of all connections between the nodes (these connections will later be replaced with more efficient ones). After calculations, it has been concluded that the most efficient method of eliminating the connections within the network is to remove some of the network's nodes along with all connections adjacent to these nodes. Therefore, a subset of nodes must be removed so that any connection in the network has at least one endpoint in this subset. Obviously, the goal is to remove a minimum number of nodes.

# Task
Given a network whose structure adheres to the rules specified above, determine the minimum number of nodes that must be eliminated so that, along with them, all existing connections in the network are eliminated.
The network is described as a string of characters that follows the following grammatical rules:
~[img4.png]

The character $S$ represents the operation of connecting in series two networks, and the character $P$ represents the operation of connecting in parallel two networks. It can be observed that the described grammar is similar to a grammar of arithmetic expressions, where $S$ and $P$ are binary operators (applied to two networks). Following this observation and to avoid ambiguities that some strings might produce, we will consider that the operator $P$ has a higher priority than the operator $S$. Thus, the string `BPBSB` corresponds to a parallel connection of two "basic networks," the resulting network then being connected in series with another "basic network" (the string is equivalent to `(BPB)SB`, where the presence of parentheses clearly specifies the order of operator application).
The two networks described in the previous figures (except the "basic network") correspond to the following two strings: `(BSBSB)P(BSB)S(BSB)`, and `(BSBSB)PB`.

# Input data
The first line of the input file `rsp.in` contains the integer number $T$, representing the number of networks that will be described next. The following $T$ lines each contain a string of characters that correctly describes a network.

# Output data
In the file `rsp.out`, print $T$ lines, representing the minimum number of nodes that must be eliminated from each network described in the input file. The first number displayed corresponds to the first described network, the second number to the second described network, and so on.

# Constraints and clarifications
* $1 \leq T \leq 10$
* Any string in the input file will contain at most $100\ 000$ characters.
* No string in the input file will contain spaces; the strings are formed only from the characters `B`, `S`, `P`, `(`, and `)`.
* Any line in the input file ends with the "newline" character.
* $60\%$ of the test files will contain only strings having lengths $\leq 5\ 000$ characters.

# Example

`rsp.in`
```
7
B
(BSBSB)P(BSB)S(BSB)
(BSBSB)PB
BPBPBPBPBPBPBPBPBPB
(BSB)P(BSB)P(BSB)P(BSB)P(BSB)
(BSBSB)P(BSBSB)P(BSBSB)P(BSBSB)P(BSBSB)
BPBSBPBP(BSB)S(BSBSB)P(BSBPB)
```

`rsp.out`
```
1
4
2
1
2
6
4
```