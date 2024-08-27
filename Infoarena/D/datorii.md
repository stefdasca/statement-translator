# Debts

Gigel's father and mother are involved in selling computer systems. The business has proven very profitable due to an incredible customer credit system: a customer who buys a computer on day \(X\) (at this moment \(N\) days have passed since the store was founded, the days are numbered from 1 to \(N\), \(0 < X \leq N\)) can return the money whenever they want, with no imposed time limit. Thus, almost every day, various customers come to the family shop to fully or partially pay for a computer purchased in previous days. Because they want to start a new business, Mother and Father wish to entrust Gigel with managing the computer store. To do this, Gigel must fulfill an essential condition: at any moment of his stay at the store, he can be asked by his father over the phone to quickly answer the following family of questions: what is the remaining unpaid amount considering the purchases made by customers on days \(P\), \(P+1\), \(P+2\) $\dots$ \(Q-1\), \(Q\) (\(0 < P \leq Q \leq N\)). It is known that two computers have never been purchased on the same day. Help Gigel prove to his parents that he can manage the store.

## Task

Given: \(N\), \(M\), an array of numbers \(A_1\), \(A_2\) $\dots$ \(A_N\), and \(M\) operations. \(A_i\) (\(1 \leq A_i \leq 1000\), \(1 \leq i \leq N\)) represents the remaining unpaid amount of an order made on day \(i\). An operation can be of two types: \(A\) (payment - a value is subtracted from the remaining amount of a specific day) \(B\) (query - the sum of all remaining amounts for a range of days is requested). The program must write the sum requested by each operation of type \(B\) at the time of the query to the output file.

## Input data

The file `datorii.in` will contain on the first line the numbers \(N\) and \(M\). The next line contains the values of the array \(A_1\), \(A_2\) $\dots$ \(A_N\) separated by a space. The next \(M\) lines describe the operations (payments or queries) performed in the given order. Each line describing an operation starts with a binary code (an integer with the value 0 or 1) and continues with 2 integers. A code 0 followed by two integers \(T\), \(V\) (\(1 \leq T \leq N\), \(1 \leq V \leq 1000\)) represents an operation of type \(A\) (at that moment a value \(V\) has been paid from the remaining amount of day \(T\)). A code 1 followed by two integers \(P\), \(Q\) (\(1 \leq P \leq Q \leq N\)) represents an operation of type \(B\) (the sum of all remaining amounts from days \(P\), \(P+1\), \(P+2\) $\dots$ \(Q\) is requested at that moment).

## Output data

The file `datorii.out` will print on each line the sums required by each operation of type \(B\) (the sums are requested in the order of the operations in the input file).

## Constraints and clarifications

\(1 \leq N \leq 15000\)

\(0 < M \leq 100000\)

At any moment, \(A_i\) (\(1 \leq i \leq N\)) is non-negative.

## Example

`datorii.in`  
```
6 6
1 3 2 0 0 10
1 3 6
1 1 4
0 3 1
1 1 6
0 6 2
1 1 6
```

`datorii.out`  
```
12
6
15
13
```