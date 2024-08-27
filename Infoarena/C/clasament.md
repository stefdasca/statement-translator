# Ranking

The wonderful Tractomiada programming contest has ended. After a tough and unprecedented round, Tractorel (the contest organizer) posted the ranking. This ranking, in addition to the column with the participants' names sorted by their national position, contains 2 more columns. One column indicating which county each participant belongs to (counties are numbered from $1$ to $J$) and another column indicating the participant's position within their county (their rank in their county). Unfortunately, Tractorel lost part of the database and the column with the counties has disappeared. Since he is just a tractor driver, he asks you to tell him in how many ways he can reconstruct the column with the counties, given only the column with the position within the county. Display the answer modulo $666013$.

## Task

## Input data

The input file `clasament.in` will contain $2$ natural numbers $N$ and $J$, the number of participants in the contest, and the number of counties, respectively. The next $N$ lines each contain a natural number. Line $i$ contains the position of participant $i$ in the county to which they belong. Note: the $N$ participants are given precisely in the order of their accumulated ranking.

## Output data

The output file `clasament.out` will contain a single natural number representing the answer modulo $666013$.

## Constraints

$1 \leq N \leq 100 000$

$1 \leq J \leq 1 000 000 000$

## Example

`clasament.in`  
$5$ $4$  
$1$  
$2$  
$1$  
$1$  
$2$

`clasament.out`  
$48$