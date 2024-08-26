##  Mergesort

The Great Sage has come to explain the MergeSort algorithm to you. The MergeSort algorithm is used to sort arrays. It works as follows: Let $V$ be a permutation and the recursive function $MergeSort(left, right)$ which sorts the array $V$ in the interval $(left, right)$. Initially, the function $MergeSort(1, N)$ is called to sort the entire array. The function $MergeSort(left, right)$ works as follows: it determines the middle of the interval $middle = (left + right) / 2$ and calls the functions $MergeSort(left, middle)$ and $MergeSort(middle + 1, right)$ in turn, after which the two just sorted arrays are merged resulting in a sorted array between positions $left$ and $right$. The program runs as follows: 
``` 
void mergesort(int left, int right) { 
    if (left == right) return; 
    int middle = (left + right) / 2; 
    mergesort(left, middle); 
    mergesort(middle + 1, right);  
    // merge the 2 arrays from left to middle, and from middle + 1 to right 
    $\dots$ 
    $\dots$ 
} 
``` 
A coder has delved deeper into this algorithm and decided to make the following optimization: if the function $MergeSort(left, right)$ is called, and the array from $left$ to $right$ is already sorted, the function should stop. More precisely, if the function $MergeSort(left, right)$ is called, it should continue only if the array between $left$ and $right$ is NOT sorted. Knowing that each time the function $MergeSort$ is called it increments a natural number $SOL$ which initially is 0 by +1, determine $SOL \% 1.000.003$ after calling the function $MergeSort(1, N)$ on all permutations of order $N$.

##  Input data

The input file `mergesort.in` will contain the first line a natural number $N$.

##  Output data

The output file `mergesort.out` will contain the first line a natural number representing $SOL \% 1.000.003$.

##  Constraints and clarifications

$1 \leq N \leq 1.000.000$

##  Example

`mergesort.in` 
```
2
```

`mergesort.out` 
```
4
```

##  Explanation

For the permutation $(1,2)$ we call $MergeSort(1,2)$ and stop. $SOL = 1$. For the permutation $(2,1)$ we call $MergeSort(2,1)$. $SOL$ becomes $2$. Since the array is not sorted, we continue. We call $MergeSort(1,1)$ and $MergeSort(2,2)$ and we have sorted the array. In the end $SOL$ becomes $4$.