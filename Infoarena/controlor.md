## Task

Recently, Miruna found a new job: she became a controller in the Train of Prosperity. The route that this train follows is composed of $N$ stations where passengers can board or disembark. For each pair of stations $(A, B)$, the number of passengers who board at station $A$ and disembark at station $B$ is known. As you know, several controllers work during a long journey. It is known that Miruna has to board the train at station $P$. Therefore, all passengers who were in the train before station $P$ no longer need to be checked. Miruna is a lazy person, so she only wants to check passengers' tickets once, between stations $Q$ and $Q + 1$. You need to find out how many passengers Miruna will ask for their tickets!

## Input data

The input file `controlor.in` will contain on the first line the natural number $N$, representing the number of stations. On the following lines, there will be a triangular matrix of size $N - 1$ with the following meaning: the element on line $i$ and column $j$ in the matrix represents the number of passengers who board at station $i$ and disembark at station $i + j$.

## Output data

In the output file `controlor.out` you will display the answer for all possible pairs $(P, Q)$. The element on line $i$ and column $j$ of the output file will contain an integer representing the answer if Miruna boards at station $i$ and checks tickets between stations $i + j - 1$ and $i + j$.

## Constraints and clarifications

$2 \leq N \leq 1000$

The elements of the matrix will belong to the interval $[1, 1000]$

## Example

`controlor.in`

```
5
10
8
7
5
5
6
4
3
3
2
```

`controlor.out`

```
30 35 28 14
15 16 9 6
5 2
```