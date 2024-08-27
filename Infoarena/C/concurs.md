# Contest

Furee Pede has been hired at BIT (this company has a hierarchical structure in the form of a tree) and has been given the task of managing a contest. In this contest, teams of two employees participate with their projects. The number of points accumulated by a team is given by the lowest common boss of the two team members. The participating teams in the contest, the company's hierarchy, and the number of points that each employee can give are known.

## Task

Furee Pede is asking for your help and wants to find the winning team (the one that receives the most points).

## Input data
The first line of the file `concurs.in` contains $N$ and $M$, separated by a space. $N$ represents the number of employees, and $M$ the number of teams participating in the contest. The next line contains $N$ natural numbers representing the points that each employee can give. The following $N-1$ lines contain two numbers $X, Y$ each, which describe the company's hierarchy ( $X$ is the boss of $Y$ ). Finally, there are $M$ lines with two numbers each, representing the order numbers of the members of each team.

## Output data
The first line of the file `concurs.out` will contain three numbers, the first representing the score of the winning team, and the other two the members of the winning team.

## Constraints and clarifications

$ 0 < N < 32001$  
$ 0 < M < 500001$  
The maximum score is less than $2\ 000\ 000\ 000$  
In the case where a team member is the boss of the other, the project receives points from this very member.  
In the case where multiple teams achieve the same score, the team in which the order number of the first member is smaller will be displayed, and if this is also equal, the team in which the order number of the second member is smaller will be displayed.  

## Example

`concurs.in` 
```
5 2 
6 4 2 2 2 
1 2 
1 5 
2 3 
2 4 
3 4 
3 2
```

`concurs.out` 
```
4 3 2
```

## Explanation

The common boss of $3, 4$ is $2$, the team earns $4$.  
The common boss of $3, 2$ is $2$, the team earns $4$.  
The answer is $3, 2$ because $3 = 3$, but $2 < 4$.