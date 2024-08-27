# Subarray1000

To purchase tickets for the Cup Final, $N$ people have lined up. Each person has a preferred seat number they wish to occupy, represented by a strictly positive number greater than $1$ and less than or equal to $N$. However, everyone knows there won't be enough tickets for all, so the organizers have decided to take the longest subarray of people to whom they will distribute the remaining tickets. To avoid any suspicion, it has been decided that in this subarray, any two consecutive people must not have seats with numbers that are coprime (in this way, the organizers believe that the people will not stand out). Therefore, in exchange for a profit share worth $100$ points, the organizers seek your help: you need to determine the longest subarray such that any two consecutive elements are not coprime. 

## Input data

The input file `subsir1000.in` contains on the first line $N$, the number of people. The next line contains $N$ numbers within the interval $[2, N]$ representing the preferred seats of the people.

## Output data

In the output file `subsir1000.out`, print the length of the longest subarray that meets the given constraints.

## Constraints and clarifications

$2 \leq N \leq 100\ 000$

Considering that the given array is $A = (a_1, a_2, \dots a_N)$, a subsequence of $A$ is called $B = (a_{i1}, a_{i2}, \dots a_{iK})$ with the property that $1 \leq i1 < i2 < \dots < iK \leq N$.

The organizers do not care if the subarray includes two or more people with the same preferred seat. They give the tickets and leave them to resolve their problem.

## Example

`subsir1000.in`

```
7
5 3 4 6 2 5 6
```

`subsir1000.out`

```
4
```

## Explanation

A possible solution is: $3 \ 6 \ 2 \ 6$