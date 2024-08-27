In the Federal Republic of Serbanistan, presidential elections are conducted using a unique methodology:
- There are only two candidates, and each person in Serbanistan will vote for exactly one of the candidates.
- Serbanistan is divided into multiple states, each having a number of inhabitants ($people[i]$) and an electoral weight ($weight[i]$).
- Candidate $A$ wins the $i$-th state if they have strictly more votes than candidate $B$ in that state. In this case, the total weight of candidate $A$ increases by exactly $weight[i]$.
- In the end, the candidate with the higher total weight wins the election and becomes the new president of Serbanistan. Somewhat counterintuitive for a pure democracy like Serbanistan, this system allows a candidate to win the presidency even if they have fewer total votes than their opponent. Your task in this problem is to detect this possibility. Serbanistan initially does not exist (but is still democratic). Each year among the next $N$, its composition changes by exactly one state: either a new state appears, or one of the existing states decides to leave Serbanistan. It is possible that at different times, Serbanistan's structure causes ambiguities in the election process: it is possible to have tie votes at the state level, at the total weight level, or at the total popular vote level. For this reason, we will limit ourselves to studying only clear situations. We say that Serbanistan is in a clear situation only if all the following conditions are met:
- The number of inhabitants in each state is odd.
- The total number of inhabitants in Serbanistan is odd.
- The total sum of electoral weights is odd.

## Task
You are required to analyze the situation in Serbanistan after each update of its state composition. If after a certain update Serbanistan is not in a clear situation, you will not output anything. Otherwise, you will output "YES" if it is possible for a candidate to win the elections with fewer total votes, or "NO" if this is not possible.

## Input data
The input file `great.in` will contain on its first line the number $N$, representing the number of updates to Serbanistan's composition. The next $N$ lines will contain three numbers $type$ $people$ $weight$. If $type$ equals $0$, it encodes the joining of a new state with $people$ inhabitants and electoral weight $weight$. If $type$ equals $1$, it encodes the removal of an existing state with $people$ inhabitants and electoral weight $weight$ from those existing. It is guaranteed that such a state exists in the composition of Serbanistan at that time.

## Output data
The output file `great.out` will contain multiple lines, equal in number to the occasions when Serbanistan's situation is clear, according to the definition above. Each line will contain a response from the set {"YES", "NO"}.

## Constraints 
$1 \leq N \leq 200\,000$ 

$1 \leq people[i], weight[i] \leq 10^9$

Tests worth 50% of the points have $1 \leq N \leq 1\,500$. 

## Example 
`great.in` 
```
3 
0 3 1 
0 1 1 
0 1 3 
```

`great.out` 
```
NO 
YES 
```

## Explanation 
After the addition of the first state, the situation is clear, but it is not possible for a candidate to win the elections without also winning the popular vote. 
After the addition of the second state, the situation is no longer clear because the total number of inhabitants is now even. 
After the addition of the third state, any candidate winning this state (being voted by its only inhabitant) has already won the elections but can lose the popular vote even with $4$ votes to $1$.