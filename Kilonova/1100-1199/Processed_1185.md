File Contents:
Most participants at ONI2003 have heard, in their childhood, the story of Little Red Riding Hood. For those who know it, here comes the second part; for those who don't, don't worry, knowing it is not necessary to solve this problem. The story doesn't mention what happened on the way Little Red Riding Hood took to return from her grandmother's house. You will find out more details shortly.

On the way, she met the Wolf (the brother of the wolf who left the story in the first part). He wanted to eat her but decided to give her a chance to escape by challenging her to a mushroom picking contest.

Little Red Riding Hood is in position ($1, 1$) of a matrix with $N$ rows and $N$ columns, with mushrooms placed at each position in the matrix. The Wolf is in position ($1, 1$) of another similar matrix. During each minute, both Little Red Riding Hood and the Wolf move to one of the adjacent positions (either on the same row or column) and collect the mushrooms from the respective position. If Little Red Riding Hood reaches a position where there are no mushrooms, she will lose the game. If, at the end of any minute, she has fewer mushrooms than the Wolf, she will lose the game as well. The game starts after both participants have collected the mushrooms from their initial positions (it doesn't matter who has more at the start of the game, only after a strictly positive number of minutes from the beginning). If Little Red Riding Hood loses the game, the Wolf will eat her.

Before the game begins, Little Red Riding Hood called the Hunter, who promised to come to her rescue in a quarter of an hour ($15$ minutes). Thus, Little Red Riding Hood will be free to leave if she does not lose the game after $15$ minutes.

From this point, her goal is not only to stay alive but also to pick as many mushrooms as possible to take home (once the hunter arrives, she won't be allowed to pick any more). The Wolf, known for his proverbial greed, will choose in each minute to move to the neighboring field with the most mushrooms (the matrix is given such that there are no multiple possibilities for selection at any given time). The story says that Little Red Riding Hood went home with her basket full of mushrooms, using the directions given by a program written by a contestant at ONI 2003 (we will not provide additional details about other aspects, such as time travel, to avoid unnecessarily complicating the problem statement). Could this program have been written by you? We shall see...

# Task

Write a program that helps Little Red Riding Hood stay in the game and collect as many mushrooms as possible at the end of the $15$ minutes!

# Input data

The file `scufita.in` has the following structure:

* The first line contains $N$ - the dimension of the two matrices.
* The next $n$ lines contain $n$ values each, representing matrix $a$, from which Little Red Riding Hood collects.
* The next $n$ lines contain $n$ values each, representing matrix $b$, from which the Wolf collects.

# Output data

The file `scufita.out` has the following structure:

* The first line should contain $NR$ - the total number of mushrooms collected.
* The second line should contain $d_1$, $d_2$, $\dots$, $d_{15}$ - the directions Little Red Riding Hood moved, separated by a space (the directions can be $N$, $E$, $S$, $V$ indicating movements toward North, East, South, West; position ($1, 1$) is located in the North-West corner of the matrix).

# Constraints and clarifications

* $4 \leq N \leq 10$;
* The values in both matrices are natural numbers less than $256$;
* Neither Little Red Riding Hood nor the Wolf will leave their respective matrices;
* After a player collects the mushrooms from a position, there will be $0$ mushrooms left in that position;
* In the given tests, Little Red Riding Hood will always have the possibility to last $15$ minutes.
* Any correct solution is acceptable.

# Example

`scufita.in`
```
4				
2 2 3 4				
5 6 7 8
9 10 11 12
13 14 15 16
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

`scufita.out`
```
137
SSSEEENVVNEENVV
```

## Explanation

Little Red Riding Hood made the same moves as the Wolf and always had one more mushroom. In the end, she collected all the mushrooms in the matrix.