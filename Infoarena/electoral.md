Electoral

Electoral fraud is the act of influencing elections with the goal of compromising the result of a democratic election process. It is known that a small amount of fraud can change the final result of the elections. Being an illegal endeavor, the one who commits fraud wishes to make as few changes to the votes as possible to achieve their goal. In our problem, the elections are held in $N$ districts, in two stages:

Stage 1: In each district, the cast votes have been counted, and the number of votes each candidate (who received at least one vote) has been recorded. The winner in a district at this stage is the candidate who received at least $[\frac{V}{2}] + 1$ votes, where $V$ is the total number of votes cast in the district. If no such candidate exists, then that district will not be considered in stage 2.

Stage 2: Among the winners from stage 1, the election winner is declared as the candidate who has won in at least $[\frac{K}{2}] + 1$ districts, where $K$ is the number of districts that had a winner in the first stage.

The goal of the person wishing to commit fraud is to ensure that, after stage 2, there is no election winner. This situation is possible if no candidate has won in at least $[\frac{K}{2}] + 1$ districts. They try to influence the elections in this direction by making a minimum number of changes in stage 1. A change consists of shifting any vote in any district in favor of any other candidate. Votes cannot be transferred between districts, and the total number of votes cast in each district remains the same.

## Task

Given $N$ districts, $C$ candidates (numbered with values from the set $1,2,\dots,C$), and for each district, the number $M_i$ of candidates who received votes then the $M_i$ pairs in the form candidate numberVotesReceived from that district, determine:

1. The winner of the elections after stage 2, without making any changes to the recorded votes.
2. The minimum number of changes that need to be made to the votes in stage 1 so that, after stage 2, there is no election winner.

## Input data

The input file `electoral.in` contains:

* The first line contains $T$, the number of the task that needs to be solved, 1 or 2.
* The second line contains two numbers $N$ and $C$, representing the number of districts and the number of candidates, separated by a space.
* Each of the next $N$ lines contains, separated by a space, a number $M_i$ followed by $M_i$ pairs in the form candidate numberVotesReceived.

## Output data

For task 1, the output file `electoral.out` will contain the winner of the elections after stage 2, if no changes are made to the votes.

For task 2, the file `electoral.out` will contain the minimum number of changes that need to be made to the votes in stage 1 so that, after stage 2, there is no election winner.

## Constraints

$4 < N,C < 200000$

$1 < M_i < 10, 1 < i < N$

$1 < numberVotesReceived < 1\ 000\ 000$

In each district, a candidate can appear in at most one pair in the form candidate numberVotesReceived
The existence of a winner after stage 2 is guaranteed. For 20% of the tests, $T=1$ and for 80% of the tests, $T=2$.

## Example

`electoral.in`
```
1 
5 4 
2 3 2 2 4 2 
4 2 1 1 3 
2 3 4 1 3 1 
4 2 1 1 1 4 
1 3 1 1
```

`electoral.out`
```
2
```

## Explanation

Task 1 is solved. There are $5$ districts and $4$ candidates. In the first district, candidate $2$ wins because they have $4$ votes out of $6$. In the second district, candidate $4$ wins with $2$ votes out of $3$. In the third district, candidate $2$ wins with $3$ votes out of $5$. In the $4$th district, there is no winner because no candidate obtained $4/2+1$ votes. In the $5$th district, candidate $2$ is the winner. In total, there are $4$ districts out of $5$ where there was a winner, and candidate $2$ won in three of these, thus candidate $2$ is the winner of the elections.

`electoral.in`
```
2 
5 4 
2 3 2 2 4 2 
4 2 1 1 3 
2 3 4 1 3 1 
4 2 1 1 1 4 
1 3 1 1
```

`electoral.out`
```
1
```

## Explanation

Task 2 is solved. A possible change is transferring one vote from candidate $2$ in district $5$ to candidate $4$ in the same district. Thus, in district 5, candidate $4$ will win in stage 1, and in stage 2, the candidates will be: $2$, winner in 2 districts (1, 3), and $4$, winner in 2 districts (2, 5). Consequently, after stage 2, there is no winner.

`electoral.in`
```
2 
4 5 
2 2 20 3 1 2 
4 2 20 3 3 4 
4 3 5 3 3 3 3 
2 4 4 5 3 4
```

`electoral.out`
```
3
```

## Explanation

Task 2 is solved. In stage 1, we observe that $2$ wins in the first 2 districts, and in districts 3 and 4, there are no winners. Therefore, $2$ wins the elections. The minimum number of changes is $4$, and one possible set of changes is: in district 3, change one vote from candidate $4$ and one vote from candidate $5$ to candidate $3$, who will now have $6$ votes out of $10$ and becomes the winner in stage 1. In district $4$, change two votes from candidate $3$ to candidate $4$, who will now have $6$ votes out of $10$ and becomes the winner in stage 1. Thus, after stage 1, candidate $2$ is the winner in two districts, and candidates $3$ and $4$ win in one district each. As a result, after these changes, there is no election winner.

`electoral.in`
```
2 
4 4 
3 4 7 2 3 1 3 
4 1 2 2 3 2 4 
2 3 1 1 2 1 
3 2 4 2 1 2 3
```

`electoral.out`
```
1
```

## Explanation

Task 2 is solved. In stage 1, we see that $4$ wins in district $1$ with $7$ votes out of $13$, while in districts 2, 3, and 4, there are no winners in this stage. Hence, $4$ is declared the winner in stage 2. We notice that at least one change is required to have no election winner after stage 2. For example, if we change one vote from candidate $4$ to candidate $2$ in district 1, there is no winner in this district in stage 1. Since there were no winners in the other districts, ultimately, there will be no election winner in stage 2.