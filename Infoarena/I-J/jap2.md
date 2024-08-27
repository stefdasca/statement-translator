# Jap2

Bercea received a task from his mentor to create a beautiful story for the following problem, which will be given at Algoreea 2010. Before that, Bercea would like to know how to solve it, and he asks for your help in exchange for a gift on Facebook. The problem is as follows: Given a prime number $P$ that is less than or equal to $100 007$, respond quickly to $Q$ questions of the form "What is (Combinations of $A$ taken $B$ at a time) modulo $P$?"

## Input data

The first line of the input file `jap2.in` contains two natural numbers $P$ and $Q$ with the meanings from the statement. Each of the following $Q$ lines contains two natural numbers $A$ and $B$ representing a question.

## Output data

The output file `jap2.out` will contain on line $i$ the answer to the $i$-th question.

## Constraints and clarifications

$1 \leq P \leq 100 007$, $P$ is prime.  
$1 \leq Q \leq 100 000$.  
$1 \leq B \leq A \leq 10^{18}$.  
Combinations of $A$ taken $B$ at a time is equal to $\frac{A!}{B!(A-B)!}$, where $A! = 1 \cdot 2 \cdot 3 \cdot \dots \cdot A$.  
For 10% of tests, $A, B \leq 2000$  
For 50% of tests, $A, B \leq 1\ 000\ 000\ 000$  
For 70% of tests, $P \leq 4\ 000  

## Example

`jap2.in`  
```
13 10  
3 3  
5 3  
3 2  
13 1  
7 4  
10 3  
10 8  
3 2  
5 5  
7 4  
```
`jap2.out`  
```
1  
10  
3  
13  
35  
120  
45  
3  
1  
35  
```