# STV

The dragon Arhirel has started to be passionate about elections. He realized that elections are very important and decided to vote in all upcoming elections. In the post-election period, Arhirel reflects a lot on the election results and voting systems. Arhirel does not like the single-round system with multiple participants at all. After long periods of contemplation, Arhirel concluded that it would be great if the Single Transferable Vote system could be implemented. The system allows a citizen to rank the candidates according to their preference. After all preferences are expressed, candidates are eliminated one by one (until only one remains). At each step, the candidate who is the favorite on the fewest lists is eliminated (in case of a tie, the one with the highest index is eliminated). The votes attributed to the eliminated candidate are redistributed to the next candidate still in the race (in the order of preference list). The order in which the candidates are eliminated determines the final ranking of the elections. For example, suppose there are $3$ candidates and $9$ votes have been registered, and the ballots look like this (the names of the voters are omitted to preserve the anonymity of the vote):

$Gicu \quad Nicu \quad Ţicu$  
$1 \quad 2 \quad 3$  
$1 \quad 2 \quad 3$  
$1 \quad 2 \quad 3$  
$1 \quad 2 \quad 3$  
$- \quad 2 \quad 1$  
$- \quad 2 \quad 1$  
$- \quad 2 \quad 1$  
$3 \quad 1 \quad 2$  
$- \quad 1 \quad 2$  

(the candidate marked with number $1$ is considered favorite, followed by the one marked with number $2$, and so forth)

In the first step, Nicu is eliminated, who is the favorite for only $2$ out of the $9$ voters (votes $8$ and $9$). He is eliminated from all voters' lists. Then, votes $8$ and $9$ will be redistributed to the second candidate in the order of preferences (if he exists). Thus, Ţicu will end up receiving a total of $5$ votes (votes $5$, $6$, $7$, $8$, $9$), which will ensure his victory against Gicu. The final ranking will consist of Ţicu (1st place), followed by Gicu (2nd place), and finally, Nicu (3rd place). However, before popularizing the system, Arhirel decided to test it and will ask for your help.

## Input data

The input file `stv.in` contains the first line which contains $N$ - the number of voters and $M$ - the number of candidates (candidates will have order numbers from $1$ to $M$). It is followed by $N$ lines of the form $c[i]$ - the number of candidates on the voter's $i$ list, followed by $c[i]$ distinct natural numbers from the interval $1 \dots N$, representing the candidates chosen in the order of the citizen's preference.

## Output data

In the output file `stv.out` you must print a permutation, representing the ranking of the candidates following the elections (the winner being the first).

## Constraints and clarifications

$1 \leq N$

$M \leq 100$

## Example

`stv.in`

```markdown
9 3
3 1 2 3
3 1 2 3
3 1 2 3
3 1 2 3
2 3 2
2 3 2
2 3 2
3 1 2
2 2 1
```

`stv.out`

```markdown
2 3 1
```

## Explanation

The first example is identical to the one explained in the task. Candidate $1$ is Gicu, candidate $2$ is Nicu, and candidate $3$ is Ţicu. In example $2$, in case of a tie, the candidate with the highest index is eliminated; therefore, candidate $2$ is eliminated, and candidate $1$ wins.