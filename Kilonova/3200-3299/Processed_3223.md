# Let man be content with his poverty, for, if it comes to it, it is not your wealth but the tranquility of your hut that makes you happy. (ASG is a millionaire from TikTok)

ASG is participating in the qualifying match for FNCS (Fortnite Championship) which lasts a maximum of `20` minutes. There, other professional Fortnite players also participate. After this match, ASG wants to find out how many points he has scored in this tournament, as well as who won. To find out these things, he has a list of all the $N$ kills made in that match, each on a separate line, expressed in the format `NAME:MM:SS`, where `NAME` represents the name of the player who made that kill (for example: `ASG`, `Flaviu`), `MM` represents the minute in which that kill was made (for example: `00`, `05`, `19`, `20`, `15`), and `SS` represents the second of the minute in which that kill was made, which can take values between `00` and `59`. Thus, for a kill, `nrs / 15` points will be awarded, where $nrs$ is the number of seconds elapsed from the start of the game until the kill (for example: if `MM:SS` is `17:15`, `69` points will be awarded, and if `MM:SS` is `00:14`, `0` points will be awarded). Additionally, for the last kill in the match, double the points that would normally be awarded for that kill will be given, because it is a Victory Royale.

~[image1.png|align=center|width=50%]

# Task

A natural number $N$ is given, as well as a list of all $N$ kills. Display the name of the winning player (i.e., the one with the most points), how many points this player collected, and how many points ASG collected.

# Input data

The first line contains a single natural number $N$, with the meaning from the statement.  
On the next $N$ lines, there will be a string in the format `NAME:MM:SS`, with the meaning from the statement.

# Output data

The first line will contain two natural numbers separated by a space, representing the name of the winning player, with how many points he won, and how many points ASG collected.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$;
* It is guaranteed that the participants' names will not contain the character `:`.
* In case of a tie, the one who reached the respective amount of points first will win.
* It is guaranteed that ASG will be among the participants.

# Example 1

`stdin`
```
4
ASG:00:14
Flaviu:09:12
Raul:11:30
Flaviu:18:00
```

`stdout`
```
Flaviu 180 0
```

## Explanation

$N$ is 4, so we have 4 kills.  
The first kill was made by `ASG`. It happened in minute `0` second `14`. Thus, only `14` seconds have passed since the start of the game, so ASG does not receive any points.  
The second kill was made by `Flaviu`. It happened in minute `9` second `12`. Thus, `552` seconds have passed since the start of the game, so Flaviu receives `36` points.  
The third kill was made by `Raul`. It happened in minute `11` second `30`. Thus, `690` seconds have passed since the start of the game, so Raul receives `46` points.  
The fourth kill was made by `Flaviu`. It happened in minute `18` second `00`. Thus, `1080` seconds have passed since the start of the game, so Flaviu receives `72` points, however, since it is the last kill, it means Flaviu also gets the Victory Royale, so this score is doubled, and Flaviu receives `144` points.  
The player with the most points is Flaviu (with 180), while ASG collected 0 points.

# Example 2

`stdin`
```
1
ASG:00:03
```

`stdout`
```
ASG 0 0
```

## Explanation

ASG is the only participant, so he won even though he only has $0$ points.