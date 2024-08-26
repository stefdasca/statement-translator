# Balloons

The ONIS committee has a problem they prepared just before the competition started. For each problem, we know the number of balloons that are prepared for the teams that will solve that problem, in the appropriate color. For each team, we know the probability of solving each problem. The probabilities of a team solving problems are independent: solving one problem does not change the probability of solving others. What is the probability that the stock of balloons is sufficient? (that there is a suitable balloon for each team that solves a problem). Obviously, balloons for one problem cannot be used for others.

## Input Data

The input file `baloane.in` contains on the first line the number of test cases $T$. Then each test is described as follows: The first line contains $N$ - the number of teams and $M$ - the number of problems, separated by a space. The next line contains $M$ integers - how many balloons we have for each problem in order. The following $N$ lines contain $M$ probabilities separated by a space. The numbers are specified with two decimal places as percentages: $54.23$ indicates a $54.23%$ chance of solving the problem or a probability of $0.5423$.

## Output Data

The output file `baloane.out` will contain the answers to the tests on separate lines, also as percentages but with four decimal places of precision.

## Constraints

$T = 5$  
$2 \leq N \leq 50$  
$2 \leq M \leq 12$  
$0 \leq B \leq 100$, the number of balloons of a certain type

## Example

`baloane.in`  
```
1  
3 4  
2 0 2 1  
50.00 5.00 90.00 30.00  
75.00 0.00 100.00 50.00  
50.00 10.00 80.00 40.00  
```

`baloane.out`  
```
12.6433
```

## Explanation

$12.64%$ The probability that the two balloons for the first problem are sufficient is $81.25%$  
The probability of not needing any balloon for the second problem is $85.50%$ $\dots$ etc.