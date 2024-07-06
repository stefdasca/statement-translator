~[image.png|align=right]

Tudorel has built a beautiful vacation house in Bușteni. Because he wants the yard to be beautiful as well, he decided to cover it with grass turf. The yard has a rectangular shape, with dimensions $a$ and $b$, expressed in meters.

Tudorel discussed with a specialized company, and the company's specialists told him that they can cover the yard with square turf tiles with a side length of $d$ meters. If necessary, the tiles can be cut with a special knife. The knife has a long blade ($\\gt d$), can be placed parallel to one of the sides of the tile, and when it cuts, it makes a complete cut from one end to the other, obtaining two rectangular strips. However, the specialists state that the grass does not withstand multiple cuts in one tile and that it is mandatory that, when a yard area is not covered by a whole tile, it must be covered by a single strip (not multiple). In this way, the specialists say, it is possible that a rectangular area remains uncovered in one of the corners of the yard. Tudorel says that in this case, he will buy a dog and install the dog's kennel there.

Obviously, Tudorel wants to cover the entire yard with grass spending as little money as possible. The company communicated to him:

- the cost $cd$ of a turf tile
- the cost $ct$ of a cut
- the cost $cm$ of installing a tile or a strip

# Task

Write a program that reads the dimensions of the yard, the dimension of a tile, as well as the 3 costs, $cd, ct$, and $cm$, and solves the following three tasks:

1. Determine the number of whole tiles mounted in the yard and the minimal area of the dog's kennel ($amin$);
2. Determine the total minimum number of turf tiles needed to cover the entire yard;
3. Determine the minimum amount Tudorel has to pay to cover the entire yard.

# Input data

The first line of the input file `gazon.in` contains a natural number $C$, representing the task that needs to be solved ($1, 2$ or $3$). The second line of the file contains three natural numbers separated by a space, $a b d$, representing the dimensions of the yard and the dimension of a turf tile. The third line of the input file contains three natural numbers separated by a space, $cd ct cm$, representing the costs of a tile, a cut, and the installation of a tile or strip.

# Output data

The output file `gazon.out` will contain a single line on which the answer to the task indicated in the input file will be written. If the task is $1$, the answer will consist of two natural numbers separated by a space, $nr amin$, where $nr$ represents the number of whole tiles mounted in the yard, and $amin$ the minimal area of the dog's kennel. For tasks $2$ or $3$, the answer will be a single natural number (the total minimum number of tiles needed for task $2$, respectively the minimum amount for task $3$).

# Constraints and clarifications

* $1 \\leq a, b, d \\leq 10 \\ 000 \\ 000$
* $1 \\leq ct, cd, cm \\leq 1 \\ 000$
* If there is no room for the dog's kennel, $amin$ will be $0$.
* Solving task $1$ grants 10% of the score, solving task $2$ grants 60% of the score, and solving task $3$ grants 30% of the score.

# Example 1

`gazon.in`
```
1
13 14 4
1 1 1
```

`gazon.out`
```
9 2
```

## Explanation

$9$ whole tiles; the area that cannot be covered has an area of $2(2 \times 1)$

# Example 2

`gazon.in`
```
2
13 14 4
1 1 1
```

`gazon.out`
```
14
```

## Explanation

$14$ tiles ($9$ whole + $5$ cut) $5$ cuts

# Example 3

`gazon.in`
```
3
13 14 4
1 1 1
```

`gazon.out`
```
34
```

## Explanation

$14$ tiles ($9$ whole and $5$ cut) $5$ cuts $15$ installations

~[image2.png|align=left]