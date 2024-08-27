# Toys

After holding a party at his house, Gigel, along with his kindergarten classmates, needs to carry all the toys from the living room to his room. To get from the living room to Gigel's room, the children need to traverse a hallway of length $L$. Gigel has $N$ friends (numbered from $1$ to $N$) and there are $M$ toys left to move. His friends have already started the task and are somewhere between the living room and Gigel's room. Some of them are already carrying a toy, while others are returning to the living room to fetch a new toy. We will identify the position of a child in the hallway by the distance they are from Gigel's room. Specifically, for each child $i$ we will determine two values $d_i$ and $t_i$, with the following meanings: $d_i$ represents the distance at which child $i$ is from Gigel's room, and $t_i = 1$ if child $i$ is transporting a toy from the living room to Gigel's room, and $t_i = 0$ if child $i$ is returning from Gigel's room to the living room without carrying any toy. Each child carries a toy to Gigel's room, then returns to the living room to fetch a new toy, repeating this process until all toys have been transported. Gigel analyzes the configuration of his $N$ friends and observes that $d_1 = S$ and $t_1 = 1$ (meaning the first child is at a distance $S$ from Gigel's room and is transporting a toy). For the other children ($i=2$, $3$, $\dots$, $N$), the values $d_i$ and $t_i$ can be determined using the following formulas (where the values $X$, $Y$, $Z$, $V$ are known):
$$d_i = ( X \cdot d_{i-1} + Y \cdot ( i - 1 ) ) \ \% \ ( L - 1 ) + 1$$
$$t_i = ( Z \cdot d_{i-1} + V \cdot ( i - 1 ) ) \ \% \ 2$$
Here, $a \ \% \ b$ represents the remainder when $a$ is divided by $b$.

## Task

Help Gigel determine the minimum time in which all the toys will be brought back to his room.

## Input data

The first line of the input file `toys.in` will contain three natural numbers: $N$, $L$, and $M$ separated by a space. The next line contains five natural numbers $S$, $X$, $Y$, $Z$, $V$ separated by a space, with the significance given above.

## Output data

The file `toys.out` will contain a single line which will print the minimum time in which all the toys will be transported to Gigel's room.

## Constraints and clarifications

$1 \leq M \leq 2000000000$

$1 \leq N \leq 2000000$

$1 \leq L \leq 2000000$

$1 \leq X,Y,Z,V \leq 2000000$

$1 \leq S \leq L$

The result will fit into 64-bit integer data types.

Children move one unit of distance in one unit of time, and leaving or picking up a toy does not consume time.

## Example

`toys.in`
```
5 101 100 84 89 79 17 97
```

`toys.out`
```
4124
```

## Explanation

There are 5 children, the length of the hallway is 101, and the number of toys is 100. The initial configuration of the 5 children is:
$$d_1 = 84 \quad t_1 = 1$$
$$d_2 = (89 \cdot 84 + 79 \cdot 1) \% 100 + 1 = 56$$
$$t_2 = (17 \cdot 84 + 97 \cdot 1) \% 2 = 1$$
$$d_3 = (89 \cdot 56 + 79 \cdot 2) \% 100 + 1 = 43$$
$$t_3 = (17 \cdot 56 + 97 \cdot 2) \% 2 = 0$$
$$d_4 = (89 \cdot 43 + 79 \cdot 3) \% 100 + 1 = 65$$
$$t_4 = (17 \cdot 43 + 97 \cdot 3) \% 2 = 0$$
$$d_5 = (89 \cdot 65 + 79 \cdot 4) \% 100 + 1 = 2$$
$$t_5 = (17 \cdot 43 + 97 \cdot 4) \% 2 = 1$$