## Task

Jon and Daenerys need to find an attack plan to defeat the army of the dead. They know the exact number of enemies, but not their positions. To find their locations, Jon gives Daenerys the equation of a line, and then she flies with her dragons to count how many enemies are strictly to the left of the line. The two repeat the process until Jon manages to find the positions of all the enemies. Since Jon is not good at geometry problems, he asks you for help. You are given $N$, the number of enemies, and you need to find their positions using queries like: $? \ X_1 \ Y_1 \ X_2 \ Y_2$, where $X_1$, $Y_1$, and $X_2$, $Y_2$ represent the coordinates of two points in the plane. In return, you will receive a number representing the number of points located to the left of the line determined by the points $(X_1, Y_1)$, $(X_2, Y_2)$ (see constraints and clarifications for the exact definition). $! X_1 Y_1 X_2 Y_2 \dots X_N Y_N$, where $X_P$, $Y_P$, represent the coordinates of the found positions. The points in this query must be sorted in ascending order by X, and in case of a tie by Y, to get maximum points. This type of query will be made only once.

## Interaction

Initially, the number $N$ is read from stdin. You must print a query and flush stdout. If you make a query of the first type, you must read the response to the query from stdin, otherwise, close the program.

## Constraints

$1 \leq N \leq 2000$ The coordinates of the points are integers. For the hidden points, $1 \leq X, Y \leq 100\,000$. For queries, $0 \leq X, Y \leq 10^9$. For 20 points, $N \leq 10$ and for all points $0 \leq X, Y \leq 10$. For another 20 points, the coordinates $X_i$ and $Y_i$ of any point are distinct. If you use points with non-integer coordinates in the query, you get 80% of the test score. For all sub-tasks except the first one, if you use between 75\,001 and 100\,000 queries, you get 30% of the test score (this restriction is multiplicative with the previous one). To achieve the maximum score on the test, you must use at most 75\,000 queries. The maximum number of allowed queries is 100\,000. If two identical points are given in a type 1 query, 0 points will be taken, with the message "Wrong interaction!" If the query is invalid or you exceed the query limit, you will receive a value of $-1$ and the program will end. A point $(X, Y)$ is to the left of the line determined by the points $(A, B)$, $(C, D)$ if and only if $AD + CY + XB > BC + DX + YA$.

## Example

stdin stdout 

## Explanation

$3$ Contains the number of points 
`? 1 5 4 2` Query with the points $(1, 5)$, $(4, 2)$ 
$2$ The points $(4, 5)$, $(6, 2)$ 
`? 4 2 1 5` Query with the points $(4, 2)$, $(1, 5)$ 
$1$ The point $(1, 2)$ 
`! 1 2 4 5 6 2` Found points

## Clarifications