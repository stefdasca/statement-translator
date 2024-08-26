## Task

Since the last time he pretended to be a second-rate artist, Marcel has refined his methods. Now he has a rooted tree, $M$ colors indexed from $0$ to $M-1$, and a magic brush. $Q$ times, he will choose a node and a color, dip the brush into the respective color, and with one stroke, recolor all nodes on the path from the chosen node to the root in that color. In the end, he wonders, for each node, what is its level of confusion. Every time a node with color index $u$ is recolored in color $v$, its level of confusion increases by $u\ \text{xor}\ v$ (in $C(++)$ language, we use the operator $u \ \hat{} \ v$).

## Input data

Although the official solution does not use this aspect, the operations will not be explicitly in the input. They will be generated pseudo-randomly as we will explain. The input file `pensula.in` contains, on the first line, the number $N$ of nodes in the tree, the numbers $M$ and $Q$, and the number $C$ whose purpose is described below. The second line contains $N$ numbers, representing the father of each node. If the father is $0$, it means that the respective node is the root. Initially, all nodes have the color with index $0$. The $Q$ pairs (node, color) are generated as follows:

```cpp
long long m = M;
unsigned int c = C;
for (int i = 0; i < Q; i++) {
    c = 5 * c + 1;
    int node = i % N + 1;
    int color = (m * c) >> 32;
}
```

## Output data

In the output file `pensula.out` contains the number $ans$, calculated as follows. If in the array $res[i]$ we retain the level of confusion of each node $i$, we can obtain the answer as follows:

```cpp
int ans = 0;
for (int i = 1; i <= N; i++)
    ans = (23LL * ans + res[i]) % 1000000007;
```

## Constraints and clarifications

$1 \leq N \leq 100.000$  
$1 \leq M \leq 1.000.000.000$  
$1 \leq Q \leq 700.000$  
$1 \leq C < 2^{31}$  

For 50 points, it is guaranteed that the degree of each node is at most 2; in other words, the tree is a line or chain.

For 30 of the 50 points described above, it is also guaranteed that the root has a degree of 1; in other words, the root is at one end of the line or chain.

For 20 points, $N \leq 2.000$ and $Q \leq 4.000$ – some points are common with those described above.

For 60 points, $N \leq 60.000$ and $Q \leq 120.000$ – ditto.

## Example

`pensula.in`
```
9 23 23 23 
8 9 9 9 2 3 3 4 0
```

`pensula.out`
```
253631257
```

## Explanation

$res[1\ \dots \ 9] = 17\ 51\ 26\ 73\ 7\ 4\ 0\ 19\ 101$