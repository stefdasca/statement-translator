# NASA

Litvinenko is a well-known KGB spy (I'm sure you've seen him on television recently). His mission is to infiltrate NASA's database and steal any plans the Americans have regarding the conquest of the universe. The only way to bypass the Americans' security measures is by intercepting communications between a ground base and a satellite orbiting Earth. From other information that the KGB has, the American communications are encoded using square-free numbers between $A$ and $B$ (inclusive). A number is square-free if it is not divisible by any perfect square. For example, $2$, $3$, $33$ are square-free, while $99$, $121$, $72$ are not square-free. Since he isn't very good at counting, Litvinenko needs a program to help him determine how many of these numbers exist.

## Input data

The first line of the `nasa.in` file contains two integers $A$ and $B$ as described in the task.

## Output data

The only line of the `nasa.out` file will contain the number of square-free numbers between $A$ and $B$ inclusive.

## Constraints

$1 \leq A \leq B \leq 2\,147\,000\,000$  
$0 \leq B - A \leq 100\,000\,000$  

## Example

`nasa.in`  
`10 21`  
`nasa.out`  
`8`  

`nasa.in`  
`123 789`  
`nasa.out`  
`405`

## Explanation

For the first example, the square-free numbers are: $10, 11, 13, 14, 15, 17, 19, 21$