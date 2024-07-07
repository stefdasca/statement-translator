It is said that during the war with the gnomes, the trolls sent $n$ elite snipers to eliminate the $n$ enemy leaders.

Fortunately, the enemy leaders were placed in an open field, and the snipers managed to position themselves without being noticed. However, when the command to fire was to be given, it was found that each sniper was not told which leader to shoot, and if two snipers shot the same leader or their deadly rays intersected, then at least one leader would escape and continue the war. Therefore, the leaders had to be eliminated simultaneously, otherwise... History tells us that the trolls won because their commander managed to tell each sniper who to shoot in less than a second. Can you do this?

# Task

Write a program that, reading the positions of the snipers and the leaders, determines which leader each sniper should shoot.

# Input data

The input file `snipers.in` contains on its first line the number $n$. The next $n$ lines contain pairs of integers, separated by space, representing the coordinates of the snipers, followed by another $n$ pairs of integers representing the coordinates of the leaders (abscissa and ordinate).

# Output data

The output file `snipers.out` contains $n$ lines. Line $i$ of the file contains the number of the leader targeted by sniper $i$ ($i=1 \ldots n$).

# Constraints and clarifications

* $0 < n < 200$
* The coordinates are integers in the range $[0, 50\ 000]$
* The deadly ray of any weapon stops at its target
* In the input data, no three persons are collinear

# Example 1

`snipers.in`
```
2
1 3
1 1
3 4
3 1
```

`snipers.out`
```
1
2
```

# Example 2

`snipers.in`
```
5
6 6
4 13
2 8
9 4
5 2
6 11
9 7
3 9
1 4
7 3
```

`snipers.out`
```
2
1
3
4
5
