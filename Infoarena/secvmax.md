# Secvmax

Fiona has an array of $N$ natural numbers. Occasionally, she wonders for a given number $Q$ what is the longest subarray where all the numbers are less than or equal to $Q$. Help Fiona answer all her questions.

## Input data

The input file `secvmax.in` contains on the first line two numbers separated by a space $N$ and $M$, which represent the length of the initial array and the number of Fiona's questions. The next line contains the $N$ natural numbers separated by a space each. The following $M$ lines each contain one number $Q$ representing Fiona's questions.

## Output data

The output file `secvmax.out` will contain $M$ lines representing the answers to Fiona's questions. More precisely, line $i$ contains the answer to the $i$-th question, namely the length of the longest subarray where all numbers are less than or equal to $Q_i$.

## Constraints and clarifications

$1 \leq N$   
$1 \leq M \leq 10^5$   
All numbers in the input file will be between $0$ and $10^9$.

## Example

`secvmax.in`
```
5 3
4 2 3 5 1
1
3
4
```

`secvmax.out`
```
1
2
3
```

## Explanation

The answers for each question are represented by the bolded numbers:   
$1 \rightarrow \{ 4 \, 2 \, 3 \, 5 \, \mathbf{1} \}$   
$3 \rightarrow \{ 4 \, \mathbf{2 \, 3} \, 5 \, \mathbf{1} \}$   
$4 \rightarrow \{ \mathbf{4 \, 2 \, 3} \, 5 \, 1 \}$