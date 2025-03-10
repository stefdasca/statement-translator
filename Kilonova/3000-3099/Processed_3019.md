At a supermarket, there are two cash registers where customers can pay for their purchases. When entering the store, each customer receives a unique number. When they want to pay, they line up at one of the two cash registers. Customers are processed in the order they arrive.

# Task

Write a program that processes the queues at the cash registers. This program receives $N$ instructions that must be executed. These instructions can be of the following $4$ types:

| Instruction | Meaning |
| - | ------- |
| $1$ | Cash register number $1$ has become available. The number of the customer who is next in line should be displayed; if there is no one in the queue at that register, display $-1$. |
| $2$ | Cash register number $2$ has become available. The number of the customer who is next in line should be displayed; if there is no one in the queue at that register, display $-1$. |
| $3 \\ x$ | The customer with number $x$ joins the queue at the cash register with fewer customers waiting; if both registers have the same number of customers, then customer $x$ will join the queue at register $1$. The queue the customer $x$ joins must be displayed. It is guaranteed that this customer is not already in line. |
| $4 \\ x$ | The customer number $x$ leaves the queue they were waiting in (it is guaranteed that they were already in line); in this case, nothing needs to be displayed. |

# Input data

The input file `supermarket.in` contains the number of instructions $N$ on the first line. Each of the next $N$ lines contains one instruction, in the format described in the task.

# Output data

The output file `supermarket.out` will contain the results displayed after executing the instructions from the input file, in file order, with one result per line.

# Constraints and clarifications

* $4 \leq N \leq 10^5$
* $1 \leq x \leq 10^6$
* For tests worth $30$ points, $4 \leq N \leq 10^3$
* For tests worth $30$ points, there will be no instructions of type $4$.
* A customer who once left the queue (either after an instruction of type $4$, or because they paid at a register), can return and join the queue again (as if they were coming for the first time).

# Example

`supermarket.in`
```
10
3 5
3 21
3 7
2
1
2
3 5
3 8
4 7
1
```

`supermarket.out`
```
1
2
1
21
5
-1
2
1
8
```

## Explanation

Customer $5$ joins the line at register $1$  
Customer $21$ joins the line at register $2$  
Customer $7$ joins the line at register $1$  
Customer $21$ enters at register $2$  
Customer $5$ enters at register $1$  
There is no one waiting at register $2$  
Customer $5$ joins the line at register $2$  
Customer $8$ joins the line at register $1$  
Customer $47$ leaves the line (nothing is displayed)  
Customer $8$ enters at register $1$  