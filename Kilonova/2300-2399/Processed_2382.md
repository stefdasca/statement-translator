> "Boom! Dead, you died!"

Marcel is a sixth-grade boy who is passionate about video games. He spends a lot of time playing a level-based game where he needs to kill the monsters in front of him on Margareta Avenue. Each monster has a certain power, so our hero needs to have power greater than or equal to the monster's power. Each time he kills a monster, the power of the character in the video game decreases by the power of the monster he defeated. As mentioned, Marcel spends a lot of time on the computer, so his mother forbids him from playing for a week. To not fall behind and advance in the game, he asks you to play in his place.

# Task
Given $N$, $K$ and $N$ natural numbers, find the maximum level you can reach while playing. The obtained level is determined by the number of monsters killed, knowing that you can start the game at any position on the avenue.

# Input data
The first line of the input file will contain $N$ representing the number of monsters on the avenue, $K$ representing the power of the character. The second line will contain $N$ numbers representing the power of each monster.

# Output data
The output file will contain a single line that will display the maximum level you can reach.

# Constraints and clarifications
- $1 \le N \le 100\ 000$
- $0 \le a_i \le 10^9$
- $0 \le K \le 10^{14}$
- For tests worth $30$ points, $1 \le N \le 2\ 000$.

# Example
`kido.in`
```
5 9
2 4 3 6 8
```
`kido.out`
```
3
```

## Explanation
It is optimal to start from position $1$. Thus, we kill the monster at position $1$, leaving us with power $9 - 2 = 7$. We move forward and kill the monster at position $2$, leaving us with power $7 - 4 = 3$. We move forward and kill the monster at position $3$, leaving us with power $3 - 3 = 0$. We cannot advance any further because the monster at position $4$ has power $6$, we have power $0$, so $6 > 0$ and we cannot defeat it.