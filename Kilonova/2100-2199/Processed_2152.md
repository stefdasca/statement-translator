```markdown
# Task

You are given a permutation with $N$ elements. Two types of moves can be performed on the permutation:

* Choosing a prefix and reversing it.
* Choosing a suffix and reversing it.

Your task is to sort the permutation in ascending order using the described operations. To obtain all points, you are allowed to perform a maximum of $2 \cdot N$ operations.

# Input data

The file `permsort.in` contains in the first line the number $N$, and in the next line $N$ values representing a permutation.

# Output data

The output file `permsort.out` will contain in the first line the number $M$ of operations performed. The following 4M lines will contain the description of the operations performed as follows:

* If you want to reverse the prefix ending at a certain position, you will display the character `P` followed by the position value.
* If you want to reverse the suffix starting at a certain position, you will display the character `S` followed by the position value.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$ 
* If $M \leq 2 \cdot N$ you will get the maximum score.
* If $2 \cdot N < M \leq 5 \cdot N$ you will get $50\%$ of the score.
* For $M > 5 \cdot N$ no points will be awarded.
* For $70\%$ of tests, $N \leq 200 \ 000$

# Example

`permsort.in`
```
6
6 5 4 1 2 3
```

`permsort.out`
```
2
S 4
P 6
```

## Explanation

After the first operation, the permutation becomes: $6 \ 5 \ 4 \ 3 \ 2 \ 1$. The second operation reverses the entire sequence, and the permutation becomes sorted.
```