## Task

Varu is an eager young man looking for recognition and does not shy away from any task assigned to him. A few days ago he received a rather odd homework from his math teacher. He has an array of $N$ natural numbers (not necessarily distinct) on which he can perform the following operation: at a certain step, he chooses element $i$ of the array, which he can increase or decrease by one unit. By applying this method to certain elements of the array, Varu is tasked to obtain (with a minimum number of operations) at least $K$ distinct elements, which must belong to the interval $[A, B]$. As his intuition alone won't help him this time, he is asking you to build another array starting from the initial array that meets his teacher's requirements.

## Input data

The file `smen.in` contains on the first line $N$, $K$, $A$ and $B$ with the meanings from the statement. The next line contains the $N$ numbers of the initial array separated by spaces.

## Output data

The file `smen.out` contains on the first line the minimum number of operations needed to obtain an array that meets the requirements from the statement. The second line will contain $N$ numbers, separated by spaces, representing one of the possible optimal solutions.

## Constraints

$1 \leq K \leq N \leq 200$

$-200 \leq A \leq B \leq 200$

each element of the initial array will not exceed the value $200$

an element $i$ can have more than one operation applied to it

if you correctly answer the first requirement you will receive 4 points for that test, and if you correctly answer both requirements you will receive 10 points

## Example

`smen.in`
```
5 4 0 3 
2 1 2 1 2
```

`smen.out`
```
2 
2 0 2 1 3
```