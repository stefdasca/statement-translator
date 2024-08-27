## Task

Recently, Dorel resigned from his road construction job and got a new position at the fresh beer can factory near Timișoara. His task is the following: initially having $N$ empty cans, he has to pass these cans through two processes: the $A$ process, where beer is poured into cans, and the $B$ process, where cans are sealed. Naturally, since no one would buy an empty beer can, the order of the processes must be $A$ first and then $B$. It is known that the $A$ process can be executed on any of the $Nr\_A$ associated processors, with the execution time for each processor known (to fill the can with beer). Similarly, the $B$ process can be executed on any of the $Nr\_B$ associated processors, with the execution time for each processor known (to seal the can). Dorel wants to finish the job as quickly as possible so he can enjoy his work. Thus, he needs to determine the minimum time in which the $N$ cans are filled with beer and sealed. Since he promised you a share of the $N$ cans, you need to help him determine this minimum time.

## Input data

The input file `fabrica.in` contains the following data:

- The first line contains $N$, $Nr\_A$, and $Nr\_B$.
- The following $Nr\_A$ lines contain $Nr\_A$ numbers, with the $i$-th line containing the execution time on the $i$-th processor associated with $A$.
- The following $Nr\_B$ lines contain $Nr\_B$ numbers, with the $i$-th line containing the execution time on the $i$-th processor associated with $B$.

## Output data

The output file `fabrica.out` will contain two numbers: the first represents the minimum time in which the $N$ cans are passed through the $A$ process, and the second represents the minimum time in which the $N$ cans are passed through the $A$ process and the $B$ process.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$  
$1 \leq Nr\_A, Nr\_B \leq 50\ 000$  
$1 \leq execution\ time\ on\ a\ processor \leq 10\ 000\ 000$  
20% of the score is awarded for the correct calculation of the first requirement  
The result fits within 32-bit integers (beer production is fast)  
Note! A processor can process at most one beer can at a time.  

## Example

`fabrica.in`  
```
3 2 2
1 1
1 1
2 3
```

`fabrica.out`  
```
1 4
```