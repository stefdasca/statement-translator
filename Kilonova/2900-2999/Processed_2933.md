Sure, here is the translated text in English:

---

**Andor** is a planet very, very far away from our planet. Nevertheless, humans and Andoreans (the inhabitants of planet Andor) have a lot in common. One of these things is the passion for chess.

~[plsmergi.png|align=right|width=30%]

Andoreans are not very good at organizing events, so they ask you to help organize a chess contest for young children. However, Andoreans have not set a **maximum** age limit to consider a player to be a child. You have the possibility to choose it.

It is known that there are $N$ participants in this contest, and for each, you know the following two things:

- How good the player is at chess (1 is the lowest score, $10^9$ is the highest score);
- Their age.

You have favorites in this contest, so you would like to answer $Q$ questions of the form: *If the age limit were $t$ years, who would win the contest?*

# Task

You are given $N$ and two arrays $s_1, s_2, \dots s_N$ and $v_1, v_2, \dots v_N$. You are also given $Q$ and the $Q$ queries. Find the answer for each question.

# Input data

The first line of the input file ```concurs.in``` contains the number $N$. The second line contains the array $s_1, s_2, \dots s_N$. The third line contains the array $v_1, v_2, \dots v_N$. The fourth line contains the number $Q$ and the following $Q$ lines contain one number $t$ on each line.

# Output data

The output file ```concurs.out``` must contain $Q$ lines. The $i$-th line contains the answer to the $i$-th question.

# Constraints and clarifications

- $2 \leq N, Q \leq 200\ 000$
- $1 \leq s_i, v_i, t \leq 10^9$
- The unit of time used on planet Andor is different from the unit of time used on Earth, so participants can be very, very old.
- **It is guaranteed that the values in array $s$ are distinct!**
- **It is guaranteed that for each question, there is at least one participant who can participate in the contest**

| #  | Points | Constraints |
|--- |--------|-------------|
| 1  | 25     | $N, Q \leq 2\ 000$ |
| 2  | 20     | $t, v_i \leq 3$ |
| 3  | 30     | $t, v_i \leq 10^6$ |
| 4  | 25     | No additional constraints |

# Example

`concurs.in`
```
7
10 2 8 3 6 4 7
8 2 10 1 5 4 8
12
1
2
3
4
5
6
7
8
9
10
11
12
```

`concurs.out`
```
4
4
4
6
5
5
5
1
1
1
1
1
```

## Explanation

If the age limit were $4$ years, then the participants would be those numbered $2$, $4$, $6$. Their scores being $2$, $3$, $4$. Therefore, the winner would be the $6$-th participant.

If the age limit were $10$ years, all $N$ participants would compete. Therefore, the winner would be the first participant (with a score of $10$).

---

Please feel free to ask if you need any further assistance!