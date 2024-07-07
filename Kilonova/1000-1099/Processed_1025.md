
One of the ways to sort an array of numbers in ascending order, called insertion sort, is described below. We assume that the elements of the array are natural numbers, arranged on $n$ consecutive positions starting at $1$ and named $s[1], s[2], ..., s[n]$. We call *prefix $i$* the sequence of values occupying positions $1, 2, ..., i$. Thus, *prefix $1$* is the first element, *prefix $2$* is the first element followed by the second, *prefix $n$* is the entire array. At step $i$, with $i$ starting from $2$, we assume that prefix $i \text{−} 1$ is sorted and we insert the element $s[i]$. The insertion is done by comparing the new element with values from the end of prefix $i \text{−} 1$, in descending order of indices, and when the current element (the one at position $i$ at the beginning of this step) is smaller, the two are swapped. Obviously, when we reach the front or encounter an element smaller than the current one, the current step ends, thus obtaining prefix $i$ as sorted, being therefore ready for the next step.

Here is an example. Consider the array $s[1] = 2, s[2] = 4, s[3] = 3, s[4] = 5, s[5] = 1$.

At step 2, we consider prefix $1$, formed only with the element with value $2$, sorted. We insert $s[2] = 4$ into this prefix. No swapping operation is necessary, so the array remains unchanged:
`2 4 3 5 1`.

At step 3, the element $s[3] = 3$ needs to be inserted into the sorted prefix formed by $2$ and $4$. It is compared with $4$, requiring a swap, then it encounters a smaller element, $2$, and we stop. Thus, the array becomes:
`2 3 4 5 1`

At step 4, we need to insert $s[4] = 5$. The previous prefix is sorted. Since $5$ is already larger than the last element of the previously sorted prefix, no swap is necessary.

At step 5, the element $1$ requires $4$ swaps, in order with $5, 4, 3, 2$ until it reaches its place.

The task is to determine how many elements do not participate in any swaps if we apply this sorting algorithm and what these elements are (for the example above, the result would have been $0$ since any element must undergo at least one swap).

# Input data

The first line of the input file contains the number $n$ representing the size of the given array. The second line contains the $n$ numbers of the array. It is guaranteed that these are the values from $1$ to $n$, each appearing exactly once (in other words, a permutation of the array $1, 2, ... n$). The numbers on the second line are separated by a space.

# Output data

The first line of the output file will contain $r$, the number of values that do not participate in any swaps.
The second line contains the $r$ determined values, in ascending order, separated by a space.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$
* In specialized materials, there are various variants of the insertion sorting algorithm, including by avoiding the swapping of two values. In this problem, we strictly analyze the variant described above.

# Example

`insertsort.in`
```
7
2 1 3 6 5 4 7
```

`insertsort.out`
```
2
3 7
```
