Union

After finishing your career as an informatics olympian, you opened a factory for binary matrices. Having no other skills, this seemed like the best option. Fortunately, your products seem to be successful. So successful that counterfeits have started appearing, pretending to be your work. Today, you want to check if such a matrix is a counterfeit. You may not remember exactly which matrices you produced in the respective series, but you remember that all produced matrices were created starting with a matrix full of zeros and then coloring at most $K$ submatrices with the value $1$. It is possible that the selected submatrices for coloring overlap. Is it possible that the matrix you are analyzing was produced according to the mentioned algorithm?

## Input data

The input file `union.in` contains on its first line $T$, the number of tests in the file. The structure of a test is as follows: the first line contains the numbers $N$ $M$ $K$. The next $N$ lines each contain a string of characters of length $M$. The characters of the string are from the set $\{0, 1\}$.

## Output data

In the output file `union.out` will be the answer for each of the $T$ tests. If it is not possible that the current matrix was produced according to the described rules, the answer is $-1$. Otherwise, you will describe a sequence of coloring operations that can produce the given matrix. On the first line of the solution, you will print $NR$, the number of operations performed. Of course, this must be less than or equal to $K$. The next $NR$ lines each contain $4$ numbers $x_1$ $y_1$ $x_2$ $y_2$, which describe the top-left corners and the bottom-right corners of the chosen submatrices. The row indices must be in the interval $\[0, N - 1\]$, and the column indices must be in the interval $\[0, M - 1\]$.

## Constraints and clarifications

$1 \leq T \leq 21$ 

$1 \leq N, M \leq 20$ 

$1 \leq K \leq 6$ 

At least $13$ tests have $K \leq 5$ 

## Example

`union.in` 
```
3
3 3 3
001
000
010
3 3 1
001
000
010 
4 4 2
0110
0110
0111
0111
```

`union.out` 
```
2
0 2 0 2
2 1 2 1
-1
2
0 1 3 2
2 1 3 3
```