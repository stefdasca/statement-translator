# Fenrir

On a fair pasture's edge, In a heavenly place, Here they come along, Descending to the valley, Twenty herds of lambs, With twenty young shepherds. In this extension of the Miorița ballad, our shepherds are facing Fenrir, a character from Norse mythology, who, after a slight geographical confusion, has also ended up on the same fair pasture's edge. Moreover, he is about to attack the herds at dusk. Bored with the attitude of the Moldavian shepherd, who had begun to plan his own funeral once more, the others decided to take a more pragmatic approach and confront the problem. They concluded that the problem could be formulated as follows: The twenty young shepherds have twenty sheepfolds, each sheepfold sheltering a herd of lambs. They can construct direct, bidirectional paths between any two sheepfolds. They know that Fenrir will strike only once, at dusk, passing through each sheepfold at most once (being a relatively busy mythical animal) and destroying the herds in those sheepfolds. Knowing this, the shepherds want to build a network of paths that ensures good communication during the attack but, at the same time, does not make Fenrir's movement too easy. More precisely, the network of paths must meet the following properties: 
1. There must not be a path formed by paths that visits all 20 sheepfolds exactly once. Otherwise, Fenrir will certainly use it and consume all 20 herds, which would be disastrous for the shepherds. By protecting at least one herd during the attack, they could repopulate the other sheepfolds later. 
2. Every two sheepfolds must be connected, directly or indirectly, by paths. Furthermore, if we were to count the neighboring sheepfolds for each sheepfold, the minimum of these values should be as high as possible. The shepherds do not have time for generalizations, so you need to solve this problem only for this case with 20 sheepfolds. Instead, your score will depend on the minimum number of neighbors of a sheepfold in the solution you offer. More precisely, if we denote this number by $cMin$, your score will be Score $=$ $(cMin + 1)^2$ 

##  Input data

The input file `fenrir.in` does not contain anything relevant for your program, for obvious reasons. Nevertheless, we will include the full version of the Miorița ballad there, in case you want to read it. 

##  Output data

The first line of the output file `fenrir.out` will contain a number $M$, representing the total number of paths in your solution. The next $M$ lines will contain a pair of distinct numbers $X$ $Y$, signifying that the sheepfolds numbered $X$ and $Y$ are connected by a bidirectional path. These numbers must be in the range $[1, 20]$. All displayed pairs must be distinct.

##  Constraints

Number of sheepfolds $=$ $20$

##  Example

`fenrir.in` 
```
Pe-un picior de plai, Pe-o gură de rai, Iată vin în cale, Se cobor la vale, $\dots$
```

`fenrir.out` 
```
5 
1 10 
2 10 
5 14 
2 20 
1 20 
```
##  Explanation

This solution would score $0$ points because it does not ensure a path between any two sheepfolds.