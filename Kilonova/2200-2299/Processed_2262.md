Here's the translated problem statement:

---

In a distant land, in a parallel universe, there is the bravest pokemaster, Qwerty. A pokemaster has three pokeballs, each containing a pokemon. In the pokemon world, there are $N$ species of pokemon and no unbeatable pokemon. Pokemaster Qwerty will participate in a poketournament of pokebattles organized at pokeColosseum. If a pokebattle occurs between any two pokemaster $A$ and $B$, then both $A$ and $B$ will use all three pokemon they each have. The pokemon in the first pokeball of $A$ will battle with the pokemon in the first pokeball of $B$, the pokemon in the second pokeball of $A$ will battle with the pokemon in the second pokeball of $B$, and the pokemon in the third pokeball of $A$ will battle with the pokemon in the third pokeball of $B$. If in a pokebattle pokemon $i$ battles pokemon $j$, then the pokemaster who owns pokemon $i$ will receive $a_{i,j}$ points and the pokemaster who owns pokemon $j$ will receive $a_{j,i}$ points. A pokebattle is won by the pokemaster who has the most points. In case of a tie, no pokemaster will win that pokebattle.

Qwerty knows he will battle sequentially with $M$ pokemasters and knows which pokemon they have. He is allowed to change any number of pokemon from his pokeballs between battles with pokemon from his collection. His collection contains three specimens from all $N$ species of pokemon. He wants to win all the pokebattles by making a minimum number of pokemon swaps.

# Task

Qwerty provides you with all the necessary data and offers you $100$ poke-points if you succeed in finding the minimum number of swaps he needs to make to win all the pokebattles in the poketournament held at pokeColosseum.

# Input data

In the input file `pokemon.in` the first line contains two natural numbers $N$ and $M$ representing the number of pokemon and the number of pokemasters. The second line contains three natural numbers $P_1$, $P_2$, and $P_3$ representing the pokemon in the pokeballs that Qwerty has at the start of the poketournament. Next, there are $N$ lines each containing $N$ natural numbers representing the elements of an array $a$. The $j$-th number on the $i$-th line represents the number of points a pokemaster will receive in a pokebattle where he owns pokemon $i$ and his opponent owns pokemon $j$. Next, there are $M$ lines each containing three natural numbers representing the pokemon of Qwerty’s opponents.

# Output data

In the output file `pokemon.out` print on the first line a single natural number representing the minimum number of pokemon swaps Qwerty needs to make in order to win all the pokebattles of the poketournament.

# Constraints and clarifications

* $4 \leq N \leq 50$
* $1 \leq M \leq 100$
* $a_{i,j} \leq 100\ 000\ 000$
* For $40\%$ of the tests $N \leq 35$ and $M \leq 40$

# Example

`pokemon.in`
```
4 3 
1 2 3 
7 8 1 2 
2 8 1 9 
7 2 2 1 
3 4 8 6 
4 1 4 
2 3 1 
4 2 4
```

`pokemon.out`
```
3
```

## Explanation

In the first pokebattle Qwerty will switch the pokemon from pokeballs $2$ and $3$ with pokemon $3$ and $1$ respectively because if he does not do this, in the battle $1\ 2\ 3$ vs. $4\ 1\ 4$ he will have $5$ points while his opponent will have $19$ points. In the battle $1\ 3\ 1$ vs. $4\ 1\ 4$ Qwerty wins with a score of $11$ to $7$. In the second pokebattle Qwerty keeps the same pokemon. In the battle $1\ 3\ 1$ vs. $2\ 3\ 1$ Qwerty wins with a score of $17$ to $11$. In the last pokebattle Qwerty swaps the pokemon from pokeball number $2$ with pokemon $1$. In the battle $1\ 1\ 1$ vs. $4\ 2\ 4$ Qwerty wins with a score of $12$ to $8$. The above scenario is not the only one that guarantees the minimum number of swaps.

---

Please double-check for any potential grammar or syntax errors according to the rules of the English language. If you find any, feel free to correct them.