> *â€œThe grass is always greener on the other side ...â€*

The recent division of lands in Gheorgheni has generated a lot of envy among the villagers. Thus, some villagers have the impression that the grass grows greener in the yard of some neighbors and would like to move into one of their houses. The Gheorgheni Town Hall has decided on a redistribution of properties so that the overall happiness of the villagers is as high as possible.

The redistribution will be done taking into account the villagers' preferences for certain houses and the degree of happiness of each villager, depending on the house where they would be allocated. There will thus be triplets $(x, y, z)$ with the meaning: villager $x$ would have the happiness degree $z$ if he lived in house $y$. A villager will be satisfied if he receives one of the desired properties after the redistribution. It is possible that not all villagers will be satisfied, in which case their degree of happiness will be $0$.

The mayor of Gheorgheni village would reward you with 100 points if you help him achieve the highest possible degree of happiness in the village, i.e., the sum of the degrees of happiness of the satisfied villagers. This way he would ensure a new term in the next elections.

# Task

Given $N$ and $M$ representing the number of villagers and respectively the number of houses in Gheorgheni, as well as $K$ triplets of the form $(x, y, z)$ as described above, determine the maximum degree of happiness, the number of satisfied villagers after redistribution, and all pairs of the form $(A, B)$ with the meaning: villager $A$ receives house $B$.

# Input data

The input file `terenuri3d.in` will contain on the first line three numbers $N, M$ and $K$ as described above. The next $K$ lines will contain three numbers $x, y, z$ as described above, separated by a space.

# Output data

The output file `terenuri3d.out` will contain on the first line an integer $G$ representing the maximum degree of happiness. The second line will contain a number $P$ representing the number of villagers who will receive a desired house, and on the next $P$ lines will be pairs of numbers $A, B$ separated by a space with the meaning described above.

# Constraints and clarifications
* $N, M \leq 250$
* $K \leq 1 \ 000$
* maximum degree of happiness $ \leq 30 \ 000$
 
# Example

`terenuri3d.in`
```
2 2 3
1 1 1
2 2 2
1 2 10
```
`terenuri3d.out`
```
10
1
1 2
```

## Explanation

Villager $1$ will receive house $2$, and villager $2$ will not be satisfied. The total degree of happiness in the village will be $10$. No other allocation will generate a higher degree of happiness.