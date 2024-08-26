## Task

In the year 3015, the ONIS final has become an intergalactic phenomenon with hundreds of thousands of participants, millions of problems, and dozens of accepted solutions in the competition. The way the ranking is done has also changed: 
1. There is no more penalty because we do not want to suggest that there are competitors who are in some way penalized. 
2. All teams with the same number of problems occupy the same position in the ranking. 
3. These positions are consecutive numbers. 

An example of the ranking:
Position # Team Number of Problems 
1 Employees' Team 10 
2 Anime References Team 6 
2 More Mainstream References Team 6 
3 Musically Skilled Team 5 

The final also has live commentators, being a very popular event. However, the commentators, similar to those who comment on football matches, are not capable of very fine analysis, preferring to recite more or less relevant statistics. 

Thus, in the hour between the end of the contest and the awards ceremony, the commentators decided to calculate the best and worst position that each team could occupy after the ranking freeze. 

More precisely, for each of the $N$ teams, values $preFreeze[i]$, the number of problems correctly solved by team $i$ before the ranking freeze, and $freeze[i]$, the number of problems for which team $i$ submitted sources during the freeze, are known. 

Thus, each team can finally have, from the spectator's point of view, between $preFreeze[i]$ and $preFreeze[i] + freeze[i]$ problems solved. 

Given this information, you are asked to calculate for each team the values $worstCase[i]$, the worst position the team $i$ can get, and $bestCase[i]$, the best position the team $i$ can get. 

## Input data

The input file `comentariu.in` will contain on its first line the number $T$, the number of tests in the file. Next are $T$ tests that have the following structure: the first line contains the number $N$, indicating the number of teams in the ranking. The following are $N$ pairs of integers, $preFreeze[i]$ $freeze[i]$ as described in the statement. 

## Output data

In the output file `comentariu.out`, there will be one line for each team in each test. This line must contain two values: $bestCase[i]$ $worstCase[i]$. 

## Constraints

1 $\leq T \leq 50$ 

1 $\leq N \leq 750$ 

All values in the file are in the range $[0, 1\ 000\ 000]$. 

The teams are given in a random order. 

## Example

comentariu.in 

```
1 
3 
0 1 
0 1 
0 1
```

comentariu.out

```
1 2 
1 2 
1 2
```