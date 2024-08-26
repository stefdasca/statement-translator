Dans

At this year's national dance competition, $N$ dancers have announced their presence. Since the performance is the most important part of such an event, the organizers managed to find out (through more or less orthodox means) the preferences of the $N$ dancers in terms of dance partners. Therefore, they currently have $M$ pairs of dancers, with each pair consisting of two compatible dancers. To ensure a great show, the organizers want all these pairs to dance on the dance floor exactly once. For the smooth running of the event, at any given moment, only one pair is dancing on the floor (to be in the spotlight). Additionally, for efficiency reasons, when a dance finishes, only one dancer from the current pair should remain on the floor, and only one other dancer should join (the two dancers being of course compatible). Moreover, the same dancer can dance a maximum of two consecutive dances (obviously, three dances would be exhausting). The organizers ask you to write a program to schedule the order of the $M$ dances, if possible.

## Input Data

The input file dans.in contains on the first line $T$, representing the number of tests. Then follow $T$ tests, each structured as follows: the first line of each test contains the numbers $N$ and $M$. On the following $M$ lines, there are pairs of numbers in the form $x$ $y$, indicating that dancer $x$ is compatible with dancer $y$. 

## Output Data

The output file dans.out will contain the results of the tests from the input file, each on separate lines. For each test proceed as follows: if a solution exists for that test, print on one line the text DA, and on the second line $M+1$ numbers, representing the order in which the dancers go on stage. Otherwise, for that test, print a single line with the text NU.

## Constraints and clarifications

$T \leq 10$   
$3 \leq N \leq 100\ 000$   
$M \leq 500\ 000$   
If the solution is not unique, any can be displayed.   
It is guaranteed that the pairs in the input file are distinct from each other.

## Example

`dans.in`   
```
2   
5 5   
1 2   
4 2   
3 5   
1 3   
4 1   
4 3   
1 4   
3 1   
4 1   
```

`dans.out`   
```
DA   
1 2 4 1 3 5   
NU   
```

## Explanation

For the first test, the pairs dance in the following order: $(1, 2)$ $(2, 4)$ $(4, 1)$ $(1, 3)$ $(3, 5)$.   
For the second test, there is no solution.