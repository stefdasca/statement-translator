# Ball

Miruna is a teacher of class XII-D at the School of Well-being. Class XII-D consists of $2 \cdot N$ students, $N$ boys, and $N$ girls. The graduation ball is approaching quickly, but the pairs are still not made. Because the boys in this class are too shy to invite the girls directly to the ball, Miruna asked each of them to write the names of the chosen girls on a slip of paper. After the teacher collects all $M$ slips, she raises an existential question: "Is there more than one way to form the pairs for the ball such that each boy dances with one of the girls he wrote on the slips?"

## Input data

The input file `bal.in` will contain on the first line the numbers $N$ and $M$, representing the number of boys (and girls) and the number of slips received, respectively. The next $M$ lines will contain pairs of the form $A$ $B$, meaning that boy $A$ would like girl $B$ to be his partner at the ball.

## Output data

The output file `bal.out` will contain on the first line the word **YES** if it is possible to have exactly one way of forming pairs for the ball. In this case, on the next $N$ lines, $N$ numbers, $X_1$, $X_2$, $\dots$ $X_N$, will be printed, where $X_i$ means that boy $i$ will be paired with girl $X_i$. If there is no arrangement or if more arrangements are possible, only the word **NO** will be printed.

## Constraints

$1 \leq N \leq 100\ 000$  
$1 \leq M \leq 1\ 000\ 000$  
There is a possibility that, due to oversight, a boy might give multiple slips with the name of the same girl. 

## Example

`bal.in`  
```
4 6 
1 2 
1 3 
2 1 
3 3 
4 3 
4 4
```

`bal.out`  
```
YES 
2 
1 
3 
4
```

`bal.in`  
```
4 8 
1 2 
1 3 
2 1 
2 4 
3 1 
3 3 
4 3 
4 4
```

`bal.out`  
```
NO
```