## Task 

Today we need to decide which is the best superhero team: Captain's Team or Iron Man’s (Tony's) Team? There are $N$ angry fans, and each of them must vote for their favorite superhero team: either $C$ (Captain), or $T$ (Tony). Since Captain knows he has no chance of winning and being an honest man, he decides to cheat the elections. He wants to cancel a minimal number of votes. Voting takes place twice separately: in increasing order of the fan indices (excluding those with canceled votes) and in decreasing order of the fan indices (excluding those with canceled votes). Captain is happy if at any moment during the vote counting he does NOT lose to Tony (he doesn’t need to have more votes, just not strictly fewer). Of course, no one can mess with Tony. He knows Captain's plan and wants to know for $Q$ scenarios how many votes Captain will cancel. A scenario is defined by two numbers $L$ and $R$, meaning that only fans with indices from $L$ to $R$ inclusive will participate in the voting session. 

## Input data 

The first line of the input file `election.in` contains a single number $N$, the number of fans. The second line contains a string of $N$ characters from the set $\{C, T\}$, the votes of each fan. The third line contains a single number $Q$, the number of scenarios. The next $Q$ lines describe the $Q$ scenarios in the form $L \ R$, where $1 \leq L \leq R \leq N$. 

## Output data 

The output file `election.out` contains $Q$ lines. The $i$-th line will contain the result for the $i$-th scenario. 

## Constraints and clarifications

For 28 points: 
$1 \leq N, Q \leq 2\000$ 

For another 54 points: 
$1 \leq N, Q \leq 70\000$ 

For another 18 points: 
$1 \leq N, Q \leq 500\000$ 

## Examples 

`election.in`

```
11
CCCTTTTTTCC
3
1 11
4 9
1 6
```

`election.out`

```
4
6
3
```

## Explanation 

In the first scenario, the votes look like this: `CCCTTTTTTCC`. The only solution is to cancel 4 of Tony's votes. 

In the second scenario, the votes look like this: `TTTTTT`. The only solution is to cancel all the votes. 

In the last scenario, the votes look like this: `CCCTTT`. The only solution is to cancel all of Tony's votes.