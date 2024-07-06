# In the solar system **Stelarion**, there are $99$ planets. Planet **Hazard** hosts the **Robotron** team championship. Players are registered in the order of their arrival, regardless of the planet they come from. This year, $N$ players from $M$ planets have registered for the championship. The $i$-th registered player (with $i$ from $1$ to $N$) receives two numbers: $E_i$ — the number on their badge and $P_i$ — the player's power. The number on the badge consists of the player's planet code $CP$ (the number formed by the last two digits on the badge) and the player code $CJ$ (the number formed by the remaining digits). Players from the same planet will be placed in the same team, with their initial position in the team being the order of their registration in the competition. During the championship, several rounds will be played, and in each round, a winning team will be designated.

# Competition Rules

~[robotron.jpeg|align=right|width=20%]

* A round consists of traversing a circuit of $L$ squares, numbered from $1$ to $L$, clockwise, placed as in the figure.
* Each team has a token that is placed in square $1$ at the beginning of each round; a move by the $i$-th player in the registration order consists of moving the team's token by $P_i$ squares, clockwise.
* In each round, the teams play cyclically, in successive sequences, each sequence being in strictly increasing order of the planet codes they come from. In a sequence, all the teams play, only the last sequence of the round might be incomplete, if applicable. The order of the teams does not change from one round to the next. When it's a team's turn to play, one of its members moves the respective team's token.
* In the first round, within each team, players occupy the initial positions, determined at registration. For each subsequent round, in each team, the players' positions change, permuting circularly. Thus, the first player in the previous round becomes the last, and the second player becomes the first.
* In each round, within each team, players move the team's token in turn, in the order of their position within the team in the current round. After the player occupying the last position in the team in the current round moves, the player occupying the first position will move next.
* **The round ends when one of the teams' token has traversed the entire circuit, reaching or passing square $1$ again**. This team is designated as the winning team of the round, and the player who brings the victory to their team is the one who makes the last move of the specified type.

# Task

1. Determine the number $M$ of participating teams and the code $H$ of the host planet Hazard, knowing that the number of players in the host planet's team is strictly greater than the number of players in any other team.
2. Determine the planet code of the team that wins round $K$ and the player code who brings the victory to this team in that round.

# Input data

The input file `robotron.in` contains the following lines:
* The first line contains a number $C$, representing the task number.
* The second line contains $3$ natural numbers $N$, $L$ and $K$ with the significance stated in the task.
* The next $N$ lines contain the players' data: the $i$-th line contains two natural numbers $E_i$ and $P_i$, with the significance stated in the task. The numbers on the same line of the file are separated by a space.

# Output data

The output file `robotron.out` must contain, for $C=1$, the numbers $M$ and $H$, and for $C=2$, the planet code and the player code specified in task $2$. The numbers on the same line of the file are separated by a space.

# Constraints and clarifications

* $1 \leq N \leq 10^5$; $1 \leq L \leq 10^9$; $1 \leq K \leq 10^9$;
* $101 \leq E_i < 10^9$; $1 \leq P_i \leq 10^6$; $1 \leq CP \leq 99$.

|# | Score | Constraints|
| - | - | ------------|
|1|20|$C = 1$, $N \leq 1\ 000$|
|2|30|$C = 1$|
|3|10|$C = 2$, $N \leq 10\000$, $L \leq 10\000$, $K \leq 1\000$|
|4|10|$C = 2$, $N \leq 10\000$, $L \leq 10\000$|
|5|30|$C = 2$|

# Example 1

`robotron.in`
```
1
7 23 2
245 5
3103 5
3203 2
3303 5
2245 6
3003 3
231745 1
```

`robotron.out`
```
2 3
```

## Explanation

There are $7$ players and they will be divided into $2$ teams ($M = 2$), representing the planets with codes $\\textbf{3}$ (players with codes $31$, $32$, $33$, $30$) and $\\textbf{45}$ (players with codes $2$, $22$, $2317$). The host planet Hazard code is $H = 3$, the team from planet $3$ being the most numerous.

# Example 2

`robotron.in`
```
2
7 23 2
2145 5
3103 5
3203 2
3303 5
2245 6
3003 3
2345 1
```

`robotron.out`
```
45 21
```

## Explanation

The circuit contains $23$ squares, and in the first round, the team members have the positions established at registration and will move in the order of these positions:

The team from the planet with code $\\textbf{3}$ has the following players, with the associated codes and powers: ${\\color{red}31} \\ 5$, ${\\color{red}32} \\ 2$, ${\\color{red}33} \\ 5$, ${\\color{red}30} \\ 3$

The team from the planet with code $\\textbf{45}$ has the following players, with the associated codes and powers: ${\\color{blue}21} \\ 5$, ${\\color{blue}22} \\ 6$, ${\\color{blue}23} \\ 1$

In the second round, the members' positions change, the first players from each team moving to the back:

The team from the planet with code $\\textbf{3}$: ${\\color{red}32} \\ 2$, ${\\color{red}33} \\ 5$, ${\\color{red}30} \\ 3$, ${\\color{red}31} \\ 5$

The team from the planet with code $\\textbf{45}$: ${\\color{blue}22} \\ 6$, ${\\color{blue}23} \\ 1$, ${\\color{blue}21} \\ 5$

The team from the planet with code $45$ finishes the game in round 2 after $6$ moves, which for this team, will be executed in order by players $22$, $23$, $21$, $22$, $23$ and $21$. Therefore, the last move is made by the player with code $CJ = 21$, who reaches square $2$, thus passing square $1$.
The order in which the players of the two teams move during this round, as well as the numbers of the squares successively occupied by the two tokens, are illustrated in the table below.

~[robotron_ex.png|align=center]