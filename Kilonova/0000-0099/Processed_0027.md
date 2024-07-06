After the ninja heroes defeated Nadakhan, on the Day of the Departed, Zane was supposed to guard the `n` dolls in the museum. Among these dolls, there are `m` corridors that can be traversed in both directions. It is guaranteed that on the `m` corridors, Zane can reach each of the `n` dolls. Skulkiu, having `5` types of obstacles `A, B, C, D, E` at his disposal, tries to stop Zane by placing `4` obstacles on each corridor. Zane can destroy obstacles of types `A, B, C` and `D`, but he cannot destroy obstacles of type `E`. To destroy an obstacle of type `A`, Zane's weapon needs `1` unit of energy, for type `B` it needs `2` units of energy, for type `C` it needs `3` units of energy, and for type `D` it needs `4` units of energy. Due to the device Skulkiu uses to place the obstacles on the corridor, the four obstacles on the same corridor have increasing depth, which implies that destroying the second obstacle placed on the corridor requires `5` times more energy than usual, destroying the third obstacle requires `25` times more energy than usual, and destroying the fourth obstacle requires `125` times more energy than usual. Regardless of the direction Zane traverses the corridor to remove the obstacles, the energy consumed is the same, depending only on the order in which Skulkiu placed the obstacles. Zane will not remove the obstacles from all corridors, only the strictly necessary ones to access each doll. Zane wants to let the other ninjas train, so he minimizes the help needed for removing `E` type obstacles and then uses a minimum number of energy units himself. For the corridors with `E` type obstacles, Zane only consumes energy for obstacles of types `A, B, C` and `D`. Initially, Zane is next to doll `1`.

# Task
1. Specify how many of the `n` dolls Zane can reach before asking for help from the other ninjas.
2. Specify for the clearance of how many corridors he needs external help to reach all `n` dolls and how many `E` type obstacles are there in total on these corridors.
3. Specify what is the minimum number of energy units used.

# Input data
The file `ninjago.in` contains on the first line a natural number `v` that can only have the values `1, 2` or `3` representing which task will be solved. The file `ninjago.in` contains on the second line the natural numbers `n` and `m` separated by a space, and on the next `m` lines, for each corridor, two natural numbers separated by a space representing the two dolls between which the corridor is, followed by a space and four letters corresponding to the four types of obstacles in the order Skulkiu placed them on that corridor. There are no spaces between the four letters.

# Output data
If the value of `v` is `1`, then the output file `ninjago.out` will contain on the first line only the number of dolls that Zane can reach before asking for help from the other ninjas.
If the value of `v` is `2`, then the output file `ninjago.out` will contain on the first line the number of corridors he cannot clear alone and on the second line the total number of `E` type obstacles on these corridors.
If the value of `v` is `3`, then the output file `ninjago.out` will contain on the first line only the minimum number of energy units used.

# Constraints and clarifications
* $1 \leq N, M \leq 31200$;
* Correctly solving the first task will earn `20` points;
* Correctly solving the second task will earn `40` points;
* Correctly solving the third task will earn `30` points;
* The problem will be evaluated on tests worth `90` points;
* An additional `10` points will be awarded automatically.

# Examples

`ninjago.in`
```
1
9 15
1 2 CBAA 
1 5 ABAA 
2 6 CBEA 
2 7 ACBA 
2 5 CBEA 
3 4 ABAA 
3 7 AECE 
3 8 CBAC 
3 9 ECEE 
4 8 DBAD 
4 9 ECEB 
5 6 CBAD 
5 7 BAAD 
6 7 CBAA 
7 8 ECEB 
```

`ninjago.out`
```
5
```

`ninjago.in`
```
2
9 15
1 2 CBAA 
1 5 ABAA 
2 6 CBEA 
2 7 ACBA 
2 5 CBEA 
3 4 ABAA 
3 7 AECE 
3 8 CBAC 
3 9 ECEE 
4 8 DBAD 
4 9 ECEB 
5 6 CBAD 
5 7 BAAD 
6 7 CBAA 
7 8 ECEB 
```

`ninjago.out`
```
2
4
```

`ninjago.in`
```
3
9 15
1 2 CBAA 
1 5 ABAA 
2 6 CBEA 
2 7 ACBA 
2 5 CBEA 
3 4 ABAA 
3 7 AECE 
3 8 CBAC 
3 9 ECEE 
4 8 DBAD 
4 9 ECEB 
5 6 CBAD 
5 7 BAAD 
6 7 CBAA 
7 8 ECEB 
```

`ninjago.out`
```
1593
```

Explanations
---

For the first test:
Zane can reach the nodes `1, 2, 5, 6, 7` by clearing alone the corridors `(1,2), (1,5), (2,7)` and `(6,7)`

For the second test:
Zane needs to ask for help to clear `2` corridors to reach all `9` dolls. Zane needs help to clear the corridors `(3,7)` and `(4,9)`. On each of these `2` corridors, there are `2` `E` type obstacles, so in total there are `4` `E` type obstacles.

For the third test:
Zane will consume a minimum of `1593` energy units as follows:
`163` for the corridor `(1,2)`
`161` for the corridor `(1,5)`
`191` for the corridor `(2,7)`
`161` for the corridor `(3,4)`
`76` for the corridor `(3,7)`
`413` for the corridor `(3,8)`
`265` for the corridor `(4,9)`
`163` for the corridor `(6,7)`

For the corridor `(4,9)`, the obstacles are `ECEB`, so Zane will consume $0 + 3  \cdot 5 + 0  \cdot 25 + 2  \cdot 125 = 265$ energy units.