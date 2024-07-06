Disappointed by the result at ONI 2013, Miruna thought of trying her luck at the world championship of “Rock-Paper-Scissors”. For those who are not familiar with the game, the rules are as follows:
- There will always be a direct confrontation between two players.
- To decide the winner of a round, both will make certain gestures simultaneously using their hands:
    - An open hand represents *paper*.
    - Two extended fingers represent *scissors*.
    - A closed fist represents *rock*.
~[rps.jpg]
- Rock beats scissors, scissors beat paper, and paper beats rock.
- If both players make the same choice, the round ends in a draw.

For this edition of the world championship, the organizers want to avoid as much as possible the confrontations that end in a draw. Therefore, they decided that any match will be played in a maximum of $K$ rounds: the first player who manages to win a round will be declared the winner. If in all $K$ rounds the two make the same choices, then the confrontation between them is declared a draw. A victory is worth $W$ points, a draw $D$ points, and a loss does not change the total score of a contestant. The game system is in the form of a championship, which means that Miruna will face each of the other $N$ contestants in turn.

Unlike other “Rock-Paper-Scissors” competitions in the world, at this world championship players are not allowed to make random choices. Instead, before the championship begins, they must present the jury with a series of exactly $K$ options for the $K$ rounds, and in each confrontation they will make the same choices. Practically, the jury members will know the result of any confrontation even before the start of the championship.

Being an early riser, like the contestants at ONI 2013, Miruna wakes up early on the day of the contest and is the first to arrive at the competition venue. Using her amazing charms, Miruna can read the minds of her opponents. Every time another contestant arrives at the competition venue, she can find out the series of $K$ options they will present to the jury. Using this information, Miruna wants to find a strategy that maximizes her score.

Unfortunately, Miruna does not know the total number $N$ of contestants registered for the contest, so every time a new contestant arrives, she rethinks her optimal strategy that maximizes her score (meaning to obtain as many points as possible in the confrontation with those contestants who have already arrived at the competition venue). You are asked to implement a program to help Miruna.

# Task
$N$ lists of length $K$ are given, representing the options of the contestants in the order they arrive at the contest. Each list will consist of the characters `R`, `P` and `S` with the following significance:
- `R` — rock
- `P` — paper
- `S` — scissors

Your program will display $N$ lists of length $K$, consisting of the characters `R`, `P` and `S`, representing Miruna's optimal strategy at each moment when a new contestant arrives. If there are multiple optimal strategies, you must display the lexicographically smallest one.

# Constraints and clarifications
- $1 \leq N, K$
- $1 \leq N * K \leq 1\ 000\ 000$
- $-1\ 000 \leq W, D \leq 1\ 000$
- Miruna only likes 'î' instead of 'â'.

# Input data
The first line of the file `rps.in` will contain the numbers $N$, $K$, $W$, and $D$, with the significance given in the statement.
The next $N$ lines will each contain a string of length $K$ consisting of the characters `R`, `P`, and `S`, representing the options of the contestants.

# Output data
In the file `rps.out`, $N$ lines will be displayed, each containing the requested answer at every moment in time.

# Example
`rps.in`
```
4 3 2 1
RSP
PPP
SSP
SRR
```

`rps.out`
```
PPP
PPS
PPS
RRP
```

# Explanation
The strategies in the output file guarantee Miruna scores of $2$, $4$, $4$ and $6$. These are the maximum scores that can be obtained, and the solutions presented are lexicographically minimal.