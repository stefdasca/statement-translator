## Task

At the beginning of Girl Camp, the participants had fun completing the puzzles of a Scavenger Hunt that took them through the crowded but beautiful streets of Bucharest. The participants were divided into $K$ teams, and each team took a number $N_i$ of photos. At the end of the day, the organizers gathered the photos from each team and wanted to prepare a surprise for them: a chronological timeline of all the events of that day. The cameras of the teams were specially configured so that for each photo they also record the number of milliseconds from the start of the Scavenger Hunt until the moment it was taken. Given the $K$ directories with photos, each containing $N_i$ photos, and knowing for each photo the timestamp when it was taken, help the organizers write a program that quickly merges all the photos to compose a timeline.

## Input data

The input file `interclasari.in` will contain on the first line a number $K$ representing the number of teams. There will follow $K$ pairs of lines describing the photos taken by each team: the first line will contain $N_i$, the number of photos taken by the team, and the second line will contain $N_i$ natural numbers sorted in ascending order, representing the timestamps when they were taken.

## Output data

In the output file `interclasari.out`, the first line will contain the total number of photos taken during the Scavenger Hunt. The next line will contain, in chronological order, all the timestamps when photos were taken during the day.

## Constraints and clarifications

$1 \leq K \leq 20$

$0 \leq N_i \leq 1\,000\,000$

The photos of each team are already sorted in chronological order.

## Example

`interclasari.in`

```
3
6
0 7 8 11 12 15
0
2
6 12
8
0 6 7 8 11 12 12 15
```

`interclasari.out`

```
8
0 6 7 8 11 12 12 15
```

## Explanation

A total of $8=6+0+2$ photos were taken. Put in chronological order, they were taken at the moments $0, 6, 7, 8, 11, 12, 12$ and $15$.