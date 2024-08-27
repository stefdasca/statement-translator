Perb

SMB studied the structure of DNA sequences in biology. He receives a DNA sequence of length $N$, a sequence that contains only the characters $A$, $C$, $G$, or $T$. SMB then receives $M$ queries of the type: what is the minimum number of characters in the sequence that need to be modified such that the subarray located between positions $x$ and $y$ in the string is periodic? For example, the subarray $ACTACT$ is periodic of length $3$, while the subarray $ACTACTA$ is not periodic.

## Input data

The input file `perb.in` will contain on the first line two natural numbers, $N$ and $M$, having the meanings from the statement. The next line contains the DNA string. The following $M$ lines contain two natural numbers $x$ and $y$ having the meanings from the statement.

## Output data

The output file `perb.out` will contain $M$ lines, each line containing the answer to the queries from the input file.

## Constraints and clarifications

$1 \leq N \leq 600$

$1 \leq M \leq 500 \ \ 000$

## Example

`perb.in`

```
12 4
ACTACTGCTACG
1 3
1 9
5 10
1 12
```

`perb.out`

```
2
1
2
1
2
```

## Explanation

For the first query, the length of the period needs to be $1$. Therefore, we need to modify $2$ characters so that all three are identical. 

For the third query, the subarray $CTGCTA$ needs to be periodic. For this, we can modify a single character, the last $A$ into $G$, obtaining the subarray $CTGCTG$ which has a period of $3$.