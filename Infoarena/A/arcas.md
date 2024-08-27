## Task

After Hercules demonstrated his skill with his magical spear, he noticed that he no longer impresses the ladies like in the good old days, so he decided to learn archery. To conquer hearts again, Hercules decided to shoot arrows from multiple positions on the plane, with the arrow tip at $45$ degrees, and use his famous powers to make the arrow disappear after a certain period. Specifically, there are $N$ vertical targets in the plane represented by $x$, $y_1$, and $y_2$, meaning that the target is located from position $(x,y_1)$ to position $(x,y_2)$ in the plane. He shoots $M$ times with the bow from different positions represented by the coordinate pair $(x,y)$ and with power $r$, which means that after the arrow passes through the points $(x,y)$, $(x+1,y+1)$, $(x+2,y+2)$, $\dots$, $(x+r,y+r)$, he uses his powers to make it disappear. Your task is to help Hercules impress all the ladies by telling him how many targets he hit (a target is hit if the arrow passes through it, including its ends).

## Input data

The input file `arcas.in` contains on the first line two natural numbers $N$ (number of targets) and $M$ (number of shots). The next $N$ lines contain a triplet of natural numbers in the form $x$ $y_1$ $y_2$ meaning there is a target with ends at positions $(x,y_1)$ and $(x,y_2)$. The next $M$ lines contain a triplet of natural numbers in the form $x$ $y$ $r$ meaning Hercules shoots with the bow from the coordinate point $(x,y)$ with power $r$.

## Output data

The output file `arcas.out` will contain the answer for each shot on a separate line, specifically how many targets Hercules hit at each shot.

## Restrictions and clarifications

$1 \leq N, M \leq 10^5$  
$1 \leq x, y_1, y_2 \leq 10^5$  
$1 \leq x, y, r \leq 10^5$  
$y_1 \leq y_2$  

## Example

`arcas.in`  
```
4 3
2 3 6
4 1 3
7 4 7
9 2 6
1 2 4
2 1 6
7 2 2
```

`arcas.out`  
```
1
1
2
```

## Explanation

The targets are colored brown, and the arrow trajectory is colored red