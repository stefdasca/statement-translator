LGT Agency (Liar Game Tournament) has organized a new game: Hide and Seek!!!! Initially, there are $N$ participants (numbered from $1$ to $N$) and $N$ rooms (numbered from $1$ to $N$).

In each room $i$, the initial value $i$ is written. The game proceeds in multiple rounds.

In the first round, participants each position themselves in a specific room. From the second round onwards, each participant looks at the value written in the room they are in and will seek out the participant with that index. More precisely, if a participant (the participant with index $i$) is in room $j$ which has value $k$, they must go to the room where participant $k$ is located. Before leaving, they will change the room's value to their own index (the value written in room $j$ changes from $k$ to $i$).

After many rounds of the game, the participants have forgotten their initial positions. Akiyama (the main character of the story) remembers the positions of the participants in round $x$ and in round $y$. Although he doesn't need your help, your task is to determine the positions of the characters in the first round, given their positions in rounds $x$ and $y$.

# Task

The first line of the input file `hideandseek.in` will contain three natural numbers $N$, $x$, and $y$, with the meaning described above. The second line contains the positioning of the characters in round $x$ (a sequence of $N$ natural numbers where the element at position $i$ represents the index of the participant in room $i$ in round $x$). The third line contains the positioning of the characters after round $y$ (analogous).

# Input data

The input file `hideandseek.in` will contain:

- The first line contains three natural numbers $N$, $x$, and $y$.
- The second line contains a sequence of $N$ natural numbers representing the positioning of the characters in round $x$.
- The third line contains a sequence of $N$ natural numbers representing the positioning of the characters in round $y$.

# Output data

The output file `hideandseek.out` will contain $N$ natural numbers representing the positioning of the characters in the first round.

# Constraints and clarifications

* $ 1 \leq N \leq 10$ for $20\%$ of tests;
* $ 1 \leq N \leq 400 \ 000$ for $80\%$ of tests;
* $ 1 \leq N \leq 1 \ 000 \ 000$ for $100\%$ of tests;
* $ 1 \leq x,y \leq 10^{18}$ for at least $100\%$ of tests;
* Akiyama has decided that it would be preferable to remember two rounds that have coprime indices. More specifically, the greatest common divisor between $x$ and $y$ is $1$.

# Example

`hideandseek.in`
```
4 2 3
1 3 4 2
1 2 3 4
```

`hideandseek.out`
```
1 4 2 3
```

