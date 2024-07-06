```markdown
On Saturday, I spend time with my friends at the "Why not" nightclub in the city center. From there, we leave at dawn as a group of $p$ people, and we need to get each one of us home. Both at the nightclub, at the destination points of the group members, and at other points in the city, there are Team-Taxi stations that we can use on the way home, paying a fixed sum per each road segment that a driver demands (depending on the length of the road and not on the number of passengers).

At any station, only those who have reached their destination can leave the group, in which case *homogeneous groups* formed will split up (because the linkage people have disappeared) and will continue to take taxis to different destinations. Two different homogeneous groups can go to the same destination, but using different taxis.

A homogeneous group is a formation of people with consecutive numbers. For example, if there are $p=6$ people, the group starts from the nightclub in the formation $1 \\ 2 \\ 3 \\ 4 \\ 5 \\ 6$. If at a station person number $3$ stops, two *homogeneous groups* are formed, $1 \\ 2$ and $4 \\ 5 \\ 6$. They split up and take two different taxis. Two groups formed from $1 \\ 4 \\ 5$ and $2 \\ 6$ are ***not homogeneous*.

As long as $k$ people are taking a taxi on a segment where any driver invariably demands the sum $c$, each person's contribution on that segment is $c/k$. If a person goes alone in a taxi on that segment, they will have to pay the entire sum alone.

# Task
Knowing the number of people, the network of taxi stations, transportation costs on each segment of the network, and the destination points of each group member, determine the minimum total cost that the group members can pay so that, using taxis in the described manner, everyone gets home.

# Input data
From the file `team.in`:
* $p$ the number of people in the group leaving from the nightclub, on line $1$;
* $n$ the number of taxi stations in the city, on line $2$; the stations are numbered from $1$ to $n$;
* $m$ the number of segments directly linking two stations, on line $3$;
* $m$ triplets in the form $i j c$ ($i$ and $j$ are the stations between which the segment is considered, and $c$ is the transportation cost on that segment), on the next $m$ lines;
* $d_1 d_2 \ldots d_p$ the destination stations of the group members (not necessarily distinct), on the last line.

# Output data
The file `team.out` will contain a single line with a number representing the determined minimum cost.

# Constraints and clarifications

* $1 \leq p \leq 50$
* $2 \leq n \leq 500$
* $1 \leq i, j \leq n$
* $0 \leq c \leq 1 \ 000$
* $1 \leq d_1, d_2, \ldots, d_p \leq n$
* Station 1 is considered the starting point (the nightclub).
* All roads are bidirectional.
* There is always a solution for the provided test data.
* All input data are natural numbers.

# Example

`team.in`
```
4 
5 
8 
1 2 6
1 3 4
3 4 8
2 4 1
3 5 7
2 3 1
1 5 6
2 5 0
5 2 4 4
```

`team.out`
```
6
```

## Explanation

~[img1.png]
```