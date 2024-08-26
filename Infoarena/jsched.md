# Jsched

A processor needs to execute $N$ applications, numbered from $1$ to $N$. Each application $i$ has an execution time $t(i)$ and a weight $w(i)$. The applications will be executed on the processor in any order, without interruption. Let the order in which the applications are executed be $p(1), \dots, p(N)$. The cost associated with application $p(i)$ is $C(p(i))=(t(p(1))+\dots+t(p(i)))* w(p(i))$. The total cost associated with executing all applications is equal to $C(1)+\dots+C(N)$. Determine the minimum possible total cost (which obviously depends on the order chosen to execute the applications).

## Task

Determine the minimum possible total cost (which obviously depends on the order chosen to execute the applications).

## Input data

The input file `jsched.in` contains on the first line the natural number $N$. The $i$-th of the following $N$ lines contains 2 natural numbers: $t(i)$ and $w(i)$, separated by a space. 

## Output data

In the output file `jsched.out` you will print the minimum possible total cost. 

## Constraints

$1 \leq N \leq 100\ 000$ 

$1 \leq t(i) \leq 1\ 000$ 

$1 \leq w(i) \leq 1\ 000$ 

This problem has tests divided into 2 groups, worth 30 and, respectively, 70 points. 

## Example

`jsched.in`
```
3
2 4
5 2
1 7
```

`jsched.out`
```
35
```

## Explanation

The applications will be executed in the order $3, 1, 2$. We will have $C(3)=1*7=7$ , $C(1)=3*4=12$ and $C(2)=8*2=16$. The total cost is $7+12+16=35$.