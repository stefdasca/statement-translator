Inter

Given $P$ is a permutation of the first $N$ natural numbers. If the Bubble Sort algorithm is applied, the neighboring elements ($P[i]$ and $P[i + 1]$, if $P[i] > P[i + 1]$, for any $i$, $1 \leq i \leq N$) will be swapped until $P$ becomes the identity permutation $(1, 2, 3, \dots, N)$. Starting from the identity permutation, and given the swaps made by the algorithm, construct the original permutation $P$.

## Input data

The input file `inter.in` contains two numbers $N$ and $M$ (the number of elements in the permutation, and the number of swaps, respectively). The next $M$ lines each contain two numbers $x$ and $y$ indicating that $x$ will be swapped with $y$ when they are neighbors.

## Output data

The output file `inter.out` will contain $N$ numbers separated by space representing the original permutation.

## Constraints and clarifications

$3 \leq N \leq 1000$

$M \leq N^2$

## Example

`inter.in`
```
5 4
1 2
1 3
2 3
1 4
```

`inter.out`
```
3 2 4 1 5
```

BubbleSort Algorithm
```cpp
bool sorted = 0;
while(!sorted) {
    sorted = 1;
    for(int i = 1; i <= n - 1; ++i)
        if(v[i] > v[i + 1]) {
            swap(v[i], v[i + 1]);
            sorted = 0;
        }
}
```

