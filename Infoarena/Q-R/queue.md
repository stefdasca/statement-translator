# Queue

We want to simulate a Queue using 2 Stacks. A queue is a data structure that supports the following operations: 
$push\_back(X)$ - the element $X$ is added to the right end of the queue 
$pop\_front()$ - an element is removed from the left end of the queue 
A stack is a data structure that supports the following operations: 
$push(S,X)$ - the element $X$ is added to the top of the stack $S$ 
$pop(S)$ - an element is removed from the top of the stack $S$ 
After performing a $pop$ operation, the value from a stack will be placed in the $WR$ variable. For example, to move the top of stack 1 to stack 2, you need to perform the following set of operations: 
$pop(1)$ 
$push(2,WR)$. 
The top of stack 1 will end up in the $WR$ variable, and we can use this variable to insert the value into stack 2.

## Input data

The input file `queue.in` will contain on the first line the natural number $N$ representing the total number of operations performed on the Queue. Each of the next $N$ lines will contain one operation on the Queue, from the 2 operations described in the statement.

## Output data

In the output file `queue.out` there should be $N$ lines. Each line in the output file should start with the index of the input operation to which the sequence of operations on the current line corresponds, followed by the characters $:$,$\space$. On line $i$ there should be a series of valid operations performed on the stacks, separated by a space. If the input operation is of type $push$, to introduce the value from the input into the variable $WR$, the instruction $read(WR)$ must be used. If the input operation is of type $pop$, to display the variable $WR$, the instruction $write(WR)$ must be used.

## Constraints and clarifications

$1 \leq N \leq 30 \ 000$ 

A $push$ operation performed on one of the stacks is considered valid if the value used is in $WR$. 

All values used in $push\_back$ operations will be distinct. 

All values used in $push\_back$ operations will be natural numbers $\leq 10 \ 6$. 

On each line of the output file, you can display a maximum of $500 \ 000$ characters; otherwise, the output will be considered invalid.

For every $push\_back(x)$ operation, exactly one $read(x)$ operation must be performed.

For every $pop\_front()$ operation, exactly one $write(x)$ operation must be performed.

## Example

`queue.in`
```
5 
push_back(3) 
push_back(5) 
pop_front() 
pop_front() 
push_back(2)
```

`queue.out`
```
1: read(3) push(1,3) 
2: read(5) push(1,5) 
3: pop(1) push(2,5) pop(1) write(3) 
4: pop(2) write(5) 
5: read(2) push(2,2)
```