# Task

ONPHF (The National Rock, Paper, Scissors Olympiad) is a national competition, beloved by many for its simplicity and ease of participation, attracting a large number of contestants. These contestants will be numbered from $1$ to $N$ for easy identification.

The Olympiad consists of a series of Rock, Paper, Scissors matches. The first match takes place between players $1$ and $2$. The winner of this match then plays against player $3$. The winner of that match proceeds to face player $4$, and so on, until the final match, where player $N$ participates. Each player chooses a playing style ($P$, $H$, or $F$) from the start, which will be used in all matches they participate in.

The winner of a match is determined by the following rules:
  * If one contestant uses the style $\text{P}$ and the other uses $\text{H}$, the player using $\text{H}$ wins (paper covers rock).
  * If one contestant uses the style $\text{H}$ and the other uses $\text{F}$, the player using $\text{F}$ wins (scissors cut paper).
  * If one contestant uses the style $\text{F}$ and the other uses $\text{P}$, the player using $\text{P}$ wins (rock crushes scissors).
  * If both players use the same style, the player with the smaller index wins (it is assumed they have won more games up to this point, thus given priority).

# Input Data

The first line contains two natural numbers, $N$ and $Q$, as described in the problem statement. The next line contains $N$ characters from the set $\{\text{P}, \text{H}, \text{F}\}$ **without spaces**. The following $Q$ lines contain the changes, with a number $i$ followed by a space and a character $M$, where $i$ is the index of the player whose style is being changed, and $M$ is the new playing style.

# Output Data

The first character will represent the playing style of the winner **before** the first change. The subsequent $i$-th character will indicate the style of the Olympiad winner after the first $i$ changes.

# Constraints and Clarifications

* $2 \le N \le 10^6$;
* $1 \le Q \le 10^5$;
* For each change, $1 \le i \le N$, $M \in \{\text{P}, \text{H}, \text{F}\}$;
* It is possible for the new playing style to be the same as the old one;
* For tests worth $31$ points, $N, Q \le 5\,000$;
* For other tests worth $33$ points, $N + Q \le 70\,000$;
* For other tests worth $36$ points, there are no additional constraints.

# Example

`stdin`
```
5 3
PHFPP
5 H
4 F
5 P
```

`stdout`
```
PHFP
```

## Explanation

The first three players never change their playing style, so after the first two matches, player $3$ (with style $\text{F}$) always wins.

Initially, player $4$ wins the match against player $3$ and then against player $5$, making the first output $\text{P}$.

After the first change, player $5$ defeats player $4$, so the second output is $\text{H}$.

After the second change, player $4$ is defeated by player $3$, who then defeats player $5$, making the third output $\text{F}$.

After the third change, player $5$ defeats player $3$, resulting in the final output $\text{P}$.