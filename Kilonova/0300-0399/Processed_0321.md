Here is the translated problem statement:

The most anticipated competition of the year, the FIFA World Cup, has ended. In the midst of the Argentine celebrations, some upset French decided to attack FIFA's servers and completely erase the results from the knockout bracket. The upset French didn't know that our engineers recorded the bracket as a complete binary tree, where the costs between edges represent the score the team had with the team that is its sibling.

The team with the higher score will always advance. Moreover, to ease the scoring notation, matches that ended in a penalty shootout are noted with an extra goal for the winning team, so we do not deal with an extra score. Given the large data and the huge request for bringing the scores back, the FIFA engineers are asking for your help in confirming the champion!

# Task
Given the teams from the knockout bracket and the scores of each match, determine which team is the champion of the tournament.

# Input data
The first line will contain a number $N$, where $2^N$ will represent the total number of teams in the knockout bracket. The next $2^N$ lines will contain the names of the teams on the bracket. The following $2^{N+1} - 2$ lines will contain the edges of the tree in the form `x y g`, where $x$ represents which team (the winner of match $x$) is, $y$ represents the match being played, and $g$ represents the number of goals scored.

# Output data
Print the name of the champion team.

# Constraints and clarifications
- $1 \leq N \leq 8$
- The team names have at most $10000$ characters and are a single word
- The team names will only contain characters from the English alphabet (including uppercase)
- $g \leq 100$ for all edges
- It is guaranteed that the order of matches is given strictly increasing (i.e., if we sort the tree topologically, we get a strictly increasing sorted array)
- The third-place playoff is not relevant to us
- For 100 points: Messi > Ronaldo

# Example
`stdin`
```
4
Netherlands
USA
Argentina
Australia
Japan
Croatia
Brazil
SouthKorea
France
Poland
England
Senegal
Morocco
Spain
Portugal
Switzerland
1 17 3
2 17 1
3 18 2
4 18 1
5 19 1
6 19 2
7 20 4
8 20 1
9 21 3
10 21 1
11 22 3
12 22 0
13 23 1
14 23 0
15 24 6
16 24 0
17 25 2
18 25 3
19 26 2
20 26 1
21 27 1
22 27 2
23 28 1
24 28 0
25 29 3
26 29 0
27 30 2
28 30 0
29 31 4
30 31 3
```

`stdout`
```
Argentina
```

# Explanation
~[lionel-messi-argentina-lifts-fifa-783783853.webp]