## Task

Starting this year, Ţirbi is TeamLead at an unknown organization (for now) which he is trying to bring into the spotlight. Therefore, he launches the following challenge: given an array with $N$ distinct elements, transform it into a $K$-sorted array. An array is called $K$-sorted if it has exactly $K$ elements in the same positions as in the sorted ascending array. The only type of operation allowed on the array is $swap(i,j)$ which swaps the elements at positions $i$ and $j$. Since Ţirbi is very busy, he gives you an array with $N$ elements and asks you to transform it into a $K$-sorted array with a minimum number of $swap$ operations.

## Input data

The input file `ksort.in` contains on the first line the natural numbers $N$ and $K$ separated by a single space, and on the next line, $N$ distinct natural numbers separated by a single space.

## Output data

The output file `ksort.out` will contain on the first line the minimum number of $swap$ operations performed. On the following lines, these operations are described, one per line, by specifying the positions of the elements to be swapped. If there is no solution, $-1$ will be written on the first line of the output file.

## Constraints

$3 \leq N \leq 100000$ 

$1 \leq K \leq N$ 

All values in the array are distinct two by two and less than or equal to $2 \ 000 \ 000 \ 000$.

## Example

`ksort.in` 
```
9 3
9 4 6 8 7 3 5 2 1
```

`ksort.out`
```
2
1 9
2 4
```