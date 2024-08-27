## Task

At the Gentiana motel, bookings are made for $n$ groups of tourists several years in advance. Knowing the day the bookings begin, with the day being numbered $1$, the groups specify the ordinal number of the first and last days of the period they wish to spend at the motel. The motel owner intends to organize a traditional celebration for each group, which can only be held in the festive hall, where only one group of tourists can fit. An artist will attend these events, and the artist sets those $n$ days when they can come to the celebrations. Help the motel owner determine the day on which the celebration can be organized for each group of tourists.

## Input data

The first line of the input file `motel.in` contains the natural number $n$, representing the number of groups of tourists and the days the artist can come to the motel. The next $n$ lines contain two natural numbers (separated by a space), representing the first and last day of the periods requested by the groups of tourists. The following $n$ lines each contain a natural number, representing the ordinal number of the days when the artist is available.

## Output data

If a solution exists, the output file `motel.out` will contain $n$ lines. Each line will contain two natural numbers, separated by a space. The first number is the ordinal number of the group in the input file, the second is the ordinal number in the input file of the chosen day for the celebration. If there is at least one group for which such a day cannot be determined, the file will contain only two numbers $0$ separated by a space.

## Constraints and clarifications

$1 \leq n \leq 4000$  
$1 \leq ordinal\ number\ of\ a\ day \leq 30000$ 

## Example

`motel.in`
```
5
12 23
100 120
5 15
45 60
35 56
5
48
50
110
13
```

`motel.out`
```
3 1
1 5
5 2
4 3
2 4
```

## Explanation

Another possible solution could have been $3 \rightarrow 1, 1 \rightarrow 5, 5 \rightarrow 3, 4 \rightarrow 2, 2 \rightarrow 4$.