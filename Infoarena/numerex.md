NumereX

Given an array with $N$ numbers, initially equal to $0$, $M$ operations will be performed as follows:

UPDATE $x$ $l$ $k$ : For any $i$, $x \leq i \leq x + l - 1$, the value of the element $i$ in the array increases by $k \times (i - x + 1)$. Practically, the first element in the interval increases by value $k$, the second by $2 \times k$ and so on until the last element.

QUERY $x$ $y$ : It is required to state the sum of elements in the interval $[ x , y ]$. 

## Task

Given $N$, $M$ and the $M$ operations, you must write a program that performs these operations as efficiently as possible and writes the answers for the QUERY operations to the output file. 

## Input data

The input file `numerex.in` will contain on the first line the numbers $N$ and $M$. The next $M$ lines will describe the operations. Each line describing an operation starts with a binary code (an integer of value $0$ or $1$) and continues with $2$ or $3$ integers:
* A code $0$ will signify an UPDATE operation and will be followed by 3 numbers $x$, $l$ and $k$ (with the meaning from the statement)
* A code $1$ will signify a QUERY operation and will be followed by 2 numbers $x$ and $y$ (with the meaning from the statement) 

## Output data

The output file `numerex.out` will contain on separate lines the sums required by each QUERY operation (the sums are required in the order of appearance of the operations in the input file). 

## Constraints and clarifications

$1 \leq N \leq 100 \ 000$  
$1 \leq M \leq 200 \ 000$

For all UPDATE operations you can assume $1 \leq k \leq 100 \ 000$  
For all QUERY operations the answer will be less than $2^{64}$ 

## Example

`numerex.in`  
```
4 4
0 1 3 2
1 2 4
0 2 3 3
1 1 3 
```

`numerex.out`  
```
10
21
```

## Explanation

After the first UPDATE operation, the array will be $2 \ 4 \ 6 \ 0$, and the sum in the interval $[ 2 , 4 ]$ is equal to $10$. After the second UPDATE operation, the array will be $2 \ 7 \ 12 \ 9$ and the sum in the interval $[ 1 , 3 ]$ is equal to $21$.