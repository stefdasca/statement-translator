Thread

Gigel has $N$ threads, numbered from $1$ to $N$. Thread $i$ $(1 \leq i \leq N)$ performs the operation $x += c_i$. The execution of the operation $x += c_i$ consists of the following atomic operations: 
- read the value of $x$ from memory,
- add $c_i$ to it,
- write the result back to memory. 

Initially, the value of $x$ is $0$. The $N$ threads execute in parallel. When the threads execute in parallel, their atomic operations are interleaved in a manner chosen by the system. The task is to find how many possible values the variable $x$ can take at the end of executing all threads. 

## Input data

The first line of the input file `thread.in` contains the number $T$ of tests. The following lines contain the tests. The first line of each test contains the number $N$ of threads. The second line of each test contains the numbers $c_1, \dots, c_N$. 

## Output data

For each test, print on a separate line the number of possible values that $x$ can take at the end of execution in the output file `thread.out`.

## Constraints and clarifications

$1 \leq T \leq 128$  
$1 \leq N \leq 256$  
$0 \leq c_i \leq 256$  

## Example

`thread.in`  
`1`  
`2`  
`1 2`  

`thread.out`  
`3`  

## Explanation

The two threads are $x += 1$ and $x += 2$. At the end of execution, there are $3$ possible values for $x$: $1, 2$, and $3$. 

The value $1$ can be obtained as follows: 
- the first thread starts (reads $x$, which is $0$) 
- the second thread completes execution, after which $x$ becomes $2$ 
- the first thread continues execution (adds $1$ to the value $0$ of $x$ read at the beginning) 

The value $2$ can be obtained as follows: 
- the second thread starts (reads $x$, which is $0$) 
- the first thread completes execution, after which $x = 1$ 
- the second thread continues execution (adds $2$ to the value $0$ of $x$ read at the beginning) 

The value $3$ can be obtained as follows: 
- the first thread completes execution (after which $x = 1$) 
- the second thread completes execution (after which $x = 3$)