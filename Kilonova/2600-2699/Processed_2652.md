Yamada, the best player of the game Forest of Savior, is preparing to participate in a battle along with his teammates. To win this fight, Yamada must use various magical objects he has obtained over time.

Yamada's magical objects come in three types:
   * **Spell books.** If the character has power $P$ and reads a book of magical power $x$, then the character's power will become $P^x$.
   * **Potions.** If the character has power $P$ and drinks a potion of magical power $x$, then his new power will be $P + x$.
   * **Gems.** If the character has power $P$ and breaks a precious stone of magical power $x$, then the new obtained power will be $P \\cdot x$.

His character has an initial power $P_0$, and each of these objects, once used, will change his power irreversibly. For example, if Yamada's character starts with an initial power $P_0 = 3$, after using a potion of magical power $2$, the character's power increases and becomes equal to $5$. Subsequent use of a spell book of magical power $3$ will increase the character's power to $125$.

Yamada can use the objects in any order, but being overwhelmed by the number of ways he can use the objects, he asks for your help!

# Task

Help Yamada determine:
   1. Among all the available objects, which is the most powerful spell book, which is the most powerful potion, and which is the most powerful gem.
   2. In what order he should use the magical objects so that, in the end, his character's power is maximized.
   3. What is the maximum power his character can achieve. Since this number can be very large, Yamada only wants to find out the remainder of this number divided by $1 \\ 000 \\ 000 \\ 007$.

# Input data

The first line of the input file `apgreid.in` will contain the value $T$, which represents the task that needs to be solved and can have one of the values $1$, $2$, or $3$.

The next line contains the natural numbers $M$ and $P_0$, representing, in order, the total number of objects Yamada has, and his character's initial power.

Each of the next $M$ lines contains a description of a magical object. Line $i$ ($1 \\leq i \\leq M$) contains a character of type letter $l_i$, representing the type of object (`c` — spell book, `p` — potion, and `n` — gem) and a number $x_i$, representing the magical power depending on the type of the object. The values $l_i$ and $x_i$ are separated by a space.

# Output data

For task $T = 1$, the first line of the output file `apgreid.out` will contain three natural numbers representing, in order, the highest magical power of a spell book, a potion, and a gem.

For task $T = 2$, the output file will contain on different $M$ lines the pairs of characters and numbers, representing the type and power of the objects in the order Yamada should use them to maximize his character's power. Each line will contain a character $l$ (which will be one of `c`, `p`, or `n`) separated by a space from a number $x$ representing the magical power of the respective object. If there are several ways to achieve the maximum power, any of them will be considered correct.

For task $T = 3$, the first line of the output file will contain an integer representing the remainder of the maximum power Yamada's character can achieve divided by $1 \\ 000 \\ 000 \\ 007$.

# Constraints and clarifications

* $1 \\leq T \\leq 3$
* $1 \\leq M \\leq 100 \\ 000$
* $1 \\leq P_0 \\leq 1 \\ 000 \\ 000 \\ 000$
* $l_i \\in \\lbrace$`c`$,$ `n`$,$ `p`$\\rbrace$ for any $1 \\leq i \\leq M$
* $1 \\leq x_i \\leq 1 \\ 000 \\ 000 \\ 000$ for any $1 \\leq i \\leq M$
* If $T = 1$, then Yamada has at least one magical object of each of the three types.

|#| Points |        Constraints                                    | 
|-|-------|---------------------------------------------------------|
|1| 19    | $T = 1$                                                 |
|2| 13    | $T = 2$, $1 \\leq M \\leq 1\\ 000$                       |
|3| 17    | $T = 2$                                                 |
|4| 9     | $T = 3$, $1 \\leq M \\leq 1\\ 000$, $1 \\leq x_i \\leq 1\\ 000$ |
|5| 11    | $T = 3$, $1 \\leq x_i \\leq 1\\ 000$                      |
|6| 12    | $T = 3$, $1 \\leq M \\leq 1\\ 000$                        |
|7| 19    | $T = 3$                                                 |

# Example 1

`apgreid.in`
```
1
6 3
p 1
n 3
c 10
n 2
p 12
p 8
```

`apgreid.out`
```
10 12 3
```

# Example 2

`apgreid.in`
```
2
2 3
c 3
p 2
```

`apgreid.out`
```
p 2
c 3
```

# Example 3

`apgreid.in`
```
3
2 3
p 2
c 3
```

`apgreid.out`
```
125
