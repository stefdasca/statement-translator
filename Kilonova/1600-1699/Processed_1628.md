**Durotan**, the chieftain of the Frostwolf clan, makes a final attempt to conquer the rival clans (Orcish Horde). According to Orcish hierarchy, clan chieftains are called **warchiefs**, while the leaders of the tribes within a clan are called **shamans**. The tribes that the chieftains come from are dominant tribes, while the tribes led by shamans are vassal tribes.

On the planet, there are $N$ tribes, numbered from $1$ to $N$. The shaman of a tribe has certain combat skills. The chieftain of a clan is the shaman of their tribe. The combat skills known by shamans are numbered from $1$ to $M$. Over time, vassal relationships have been established between the tribes of the same clan. If tribe $1$ is the dominant tribe of vassal tribe $2$, and tribe $2$ has vassal tribe $3$, we will say that tribe $3$ is in the influence zone of tribes $1$ and $2$. Tribes $1$, $2$, and $3$ form a clan.

The power of a chieftain depends on the number of tribes that make up the clan, as well as the unique combat skills learned. The chieftain of a clan has certain combat skills but can also acquire (learn) unique combat skills from the shamans of the clan tribes within their influence zone. By unique combat skills, we mean skills known only by a single shaman from the totality of the clan's tribes.

Example: Consider a clan that has $4$ tribes: $1$ ($3$, $6$), $2$ ($1$, $2$, $4$), $3$ ($3$, $5$, $6$), $4$ ($1$, $3$, $4$). The chieftain of the clan is in tribe $1$, being also considered the shaman of the tribe. This shaman has skills $3$, $6$. The shaman of tribe $2$ has skills $1$, $2$, $4$, the shaman of tribe $3$ has skills $3$, $5$, $6$, and the shaman of tribe $4$ has skills $1$, $3$, $4$. Suppose tribe $4$ is a vassal of tribe $2$, while tribes $2$ and $3$ are vassals of tribe $1$. The chieftain, with the skills $3$, $6$ already had, can acquire the unique skills $2$, $5$ from the shamans of the clan's tribes.

**Durotan** invokes the ancient honor code **Mak'gora**, which involves challenging the clan chieftains to a duel. He wins the duel if he has a strictly higher number of tribes in his influence zone, and in the case of an equal number of tribes, a strictly higher number of different skills. The tribes of the defeated clan will join his clan, with Durotan acquiring (adding to himself) the unique skills of the defeated.

# Task

Given the abilities of each shaman for the $N$ tribes, the vassal relationships between the tribes, and the ordinal number of a tribe of the Frostwolf clan, determine:
- the total number of clans
- the number of tribes in the Frostwolf clan before the duel
- the maximum number of tribes Durotan can have after invoking the Mak'gora code.

# Input data

The input file `warcraft.in` contains on the first line three natural numbers $N$, $M$, $X$ representing $N$ - the number of tribes, $M$ - the number of skills, $X$ - the ordinal number of a tribe that is part of Durotan's clan.

On the next $N$ lines, a description of each tribe: $x$, $y$, $k$, $a_1$, $a_2$, $\dots$, $a_k$ where: tribe $x$ is a vassal of tribe $y$. The shaman of tribe $x$ has $k$ combat skills, $a_1$, $a_2$, $\dots$, $a_k$ in strictly increasing values.

# Output data

The output file `warcraft.out` will contain three natural numbers $n_1$, $n_2$, $n_3$, each written on a separate line, where:
- $n_1$ represents the total number of clans
- $n_2$ the number of tribes of the Frostwolf clan before the duel
- $n_3$ the maximum number of tribes of the Frostwolf clan after Durotan invokes the Mak'gora code.

# Constraints and clarifications

* $2 \leq N \leq 1 \ 000$
* $1 \leq X \leq N$
* $1 \leq M \leq 500$
* $1 \leq k \leq M$
* The number of clans $\leq 500$
* If a tribe is not a vassal of another tribe, then $y = 0$
* Durotan challenges only tribe chieftains to a duel. _In the duel, the skills known or acquired by the chieftain are used_
* For the correct determination of $n_1$, $20\%$ of the points/test are awarded. For the correct determination of $n_2$, $20\%$ of the points/test are awarded. For the correct determination of $n_3$, $60\%$ of the points/test are awarded.

# Example

`warcraft.in`
```
12 6 8
4 10 5 1 2 3 4 5
12 6 4 1 2 5 6
10 0 2 5 6
2 4 4 2 3 4 5
1 12 3 1 4 5
11 0 5 2 3 4 5 6
9 5 2 2 6
6 0 3 2 4 5
7 11 6 1 2 3 4 5 6
8 10 1 4
3 2 3 2 4 5
5 1 3 1 3 6 
```

`warcraft.out`
```
3
5
12
```

## Explanation

There are $12$ tribes, $6$ types of combat skills ($1$, $2$, $3$, $4$, $5$, $6$),
Durotan's tribe is indexed at $10$. Tribe 8 belongs to Durotan's clan.
Tribe $1$ is a vassal of tribe $12$. The shaman of the tribe has 3 skills: $1$, $4$, $5$
Tribe $2$ is a vassal of tribe $4$. The shaman of the tribe has 4 skills: $2$, $3$, $4$, $5$
Tribe $3$ is a vassal of tribe $2$. The shaman of the tribe has 3 skills: $2$, $4$, $5$
Tribe $4$ is a vassal of tribe $10$. The shaman of the tribe has 5 skills: $1$, $2$, $3$, $4$, $5$
Tribe $5$ is a vassal of tribe $1$. The shaman of the tribe has 5 skills: $1$, $2$, $3$, $4$, $5$
Tribe $6$ is dominant (not a vassal). The shaman of the tribe has 3 skills: $2$, $4$, $5$. etc.

There are $3$ clans:
- ($2$, $3$, $4$, $8$, $10$)
- ($1$, $5$, $6$, $9$, $12$)
- ($7$, $11$).

Durotan's clan has $5$ tribes in its influence zone. Durotan's combat skills: $5$, $6$ with the additional unique skill $1$. Thus, the skills used by Durotan in the first duel will be: $1$, $5$, $6$.

The second clan has the chieftain in tribe $6$ and is made up of $5$ tribes. The chieftain's skills in the event of a duel are: $2$, $3$, $4$, $5$. The third clan has the chieftain in tribe $11$. The chieftain's skills in the event of a duel are: $1$, $2$, $3$, $5$, $6$.

Durotan challenges the chieftain of the third clan to a duel. He wins the duel because the number of tribes in his clan is larger. After the duel, the number of tribes in the Frostwolf clan will be $7$, and the skills of Durotan after the duel will be: $1$, $2$, $3$, $4$, $5$, $6$.

Then, Durotan will challenge the chieftain of the second clan to a duel. The number of tribes in the Frostwolf clan after the duel is $12$.