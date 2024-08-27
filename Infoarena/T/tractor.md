# Tractor

Zaharel has bought a tractor and registered for a tractor driving contest. In this contest, there are $ N = 2^K $ participants in total, and the contest is conducted in a knockout system. At the beginning, the $ N $ participants (conveniently numbered from $ 1 $ to $ N $) are arranged by the organizers in some order. In the first round, the participant in position $ 1 $ competes with the one in position $ 2 $, the one in position $ 3 $ with the one in position $ 4 $, the one in position $ 5 $ with the one in position $ 6 $, etc. The winners advance to the next round, while the losers are eliminated from the contest. In the second round, the winner between the participants in positions $ 1 $ and $ 2 $ competes with the winner between the participants in positions $ 3 $ and $ 4 $, and so on, the winner between the participants in positions $ N - 3 $ and $ N - 2 $ competes with the winner between the participants in positions $ N - 1 $ and $ N $. The contest continues in the same manner, with half of the participants being eliminated in each round, until only one remains. The last remaining participant will be considered the winner of the contest. In each tractor driving contest where participant number $ i $ beats participant number $ j $, the prize value $ A_{i, j} $ is added to the prize pool. The prize is taken by the last participant remaining in the contest. Each of the $ N $ players imagines the most favorable scenario (which depends on the arrangement given by the organizers and the winners of each contest) in which he wins the tournament, and the accumulated prize is the maximum possible.

## Task

Determine for each of the $ N $ players what the maximum prize they can obtain is, considering that he wins the tournament.

## Input data

In the file `tractor.in`, the first line contains a natural number $ T $ representing the number of tests. Then follows the description of the $ T $ tests. The first line of a test will contain the number $ N $ of participants, and in the following $ N $ lines, $ N $ natural numbers separated by spaces representing the matrix $ A $ for that test.

## Output data

The output file `tractor.out` will contain $ N $ lines for each test representing the maximum prizes that can be obtained for each player, in order from number $ 1 $ to $ N $.

## Constraints and clarifications

$ 1 \leq T \leq 4 $

$ 1 \leq N \leq 16 $ ($ N $ is a power of 2)

$ 0 \leq A_{i, j} \leq 1\,000\,000 $, $ A_{i, i} = 0 $

## Example

`tractor.in`
```
2 
2 
0 2 
3 0 
4 
0 6 3 5 
2 0 5 1 
3 5 0 2 
4 1 3 0 
```

`tractor.out`
```
2 
3 
16 
12 
13 
13 
```

## Explanation

We will consider the example with $ N = 4 $ where player number $ 1 $ wants to know the maximum prize he can obtain. If the initial arrangement is $ 1 4 2 3 $ and the contests are conducted as follows:

```
[1] 
/   \
1     2 
/ \   / \
1   4 2   3 
```

The prize obtained is $ A_{1, 4} + A_{2, 3} + A_{1, 2} = 16 $, and this is the maximum considering all 24 possibilities for the initial arrangement and all possibilities for the conduct of the matches.