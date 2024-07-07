---

Alex and Răzvan, geography enthusiasts, play Geoguessr online. The world map consists of $ N $ locations numbered from $ 1 $ to $ N $, each designating a point in a coordinate plane $ (X_i, Y_i) $. Alex carefully studied all $ N $ locations and determined a list of $ L $ characteristics of interest for the given locations, numbered from $ 1 $ to $ L $. For example, characteristic $ 1 $ could be "Is this location in Europe?", and characteristic $ 2 $ could be "Is Spanish spoken in this location?", and so on. For each location $ i $ and characteristic $ j $, the value $ Z_{i,j} \in \{0, 1\} $ is known, with $ Z_{i,j} = 1 $ if and only if location $ i $ has characteristic $ j $. For example, if location 1 is in Asia and Spanish is spoken there, then we would have $ Z_{1, 1} = 0 $ and $ Z_{1, 2} = 1 $.

A game of Geoguessr consists of $ Q $ rounds. During a round, the computer chooses a location $ i $ from the $ N $ locations without revealing it to Alex. Instead, Alex receives several illustrations of the respective place; his goal is to identify location $ i $. By thoroughly analyzing only the illustrations, Alex can determine for any characteristic $ j $ whether location $ i $ has it or not. However, due to the limited time for each round, Alex won't always manage to find the values $ Z_{i, j} $ for all characteristics $ j $ on time but only for some. Therefore, to be as efficient as possible, Alex adopted the following game strategy inherited from his Grandfather: first, Alex will determine the value $ Z_{i,T_1} $; then, if there is still time, Alex will find the value $ Z_{i,T_2} $; then the value $ Z_{i,T_3} $, and so on until the allocated round time expires. Depending on the round's time limit (which may vary from round to round), this strategy might allow Alex to find more or fewer information about the location including none (i.e., no $ Z_{i, j} $ values discovered). We denote the information discovered by Alex by $ R_1, R_2, ..., R_L $ until the end of the round. More precisely, $ R_j = Z_{i,j} $ if Alex managed to find out whether location $ i $ has characteristic $ j $ on time, or $ R_j = -1 $ otherwise.

Attention! Alex's strategy, represented by the sequence $ T_1, T_2, ..., T_L $, remains the same for all $ Q $ rounds. The sequence $ T_1, T_2, ..., T_L $ consists of distinct values and $ T_1, T_2, ..., T_L \in \{1, 2, ..., L\} $.

# Task

At the end of a round, it is possible that multiple locations out of the $ N $ match the sequence $ R $ of information found by Alex, so he asks himself two existential questions:

What is the number $ K $ of locations out of the $ N $ that respect the sequence $ R $ of information found during the round? We say a location $ i $ respects the sequence $ R $ if for any characteristic $ j $ we have that $ R_j = Z_{i, j} $ or $ R_j = -1 $.

For each location $ i $ out of the $ N $, $ 1 \leq i \leq N $, a value $ W_i $ is given. Considering the locations that respect the sequence $ R $, $ 1 \leq i_1, i_2, ..., i_K \leq N $, for a point $ P $ of integer coordinates $ (A, B) $ in the plane, not necessarily corresponding to one of the $ N $ locations, we define
\[ d_P = W_{i_1}(|A - X_{i_1}| + |B - Y_{i_1}|) + W_{i_2}(|A - X_{i_2}| + |B - Y_{i_2}|) + \ ... + W_{i_K}(|A - X_{i_K}| + |B - Y_{i_K}|) \]

What is the point $ P $ in the plane for which $ d_P $ is minimum? If there are multiple such points $ P $, we require the one with the smallest $ A $. If there is still a tie, then the one with the smallest $ B $ is required.

A number $ C \in \{1, 2\} $ is given. For $ C = 1 $, display the answer to Alex's first question for each of the $ Q $ rounds. For $ C = 2 $, display the answer to Alex's second question for each of the $ Q $ rounds.

# Input data

The first line of the file `geogra.in` contains the natural number $ C $, representing the task to be solved. The second line contains the natural numbers $ N $ and $ L $, representing the number of locations and, respectively, the studied characteristics of Alex. The descriptions of the $ N $ locations follow in order from $ 1 $ to $ N $, each on two lines. The description of a location $ i $ is given as follows:

The first line contains the natural numbers $ X_i $ and $ Y_i $. If $ C = 2 $, following these two values is the natural number $ W_i $. The values on the line are separated by spaces.
The second line contains $ Z_{i,1}, Z_{i,2}, ..., Z_{i,L} $, separated by spaces.

The next line contains the natural number $ Q $, representing the number of rounds in the game. The descriptions of the $ Q $ rounds follow in order from $ 1 $ to $ Q $, each on one line. The description of a round $ i $ is given through the sequence of values $ R_1, R_2, ..., R_L $ found by Alex in the respective round, with the values separated by spaces.

# Output data

The file `geogra.out` will contain $ Q $ lines. If $ C = 1 $, line $ i $ will contain the number of locations that respect the sequence $ R $ of information found by Alex in round $ i $. If $ C = 2 $, line $ i $ will contain two natural numbers $ A $ and $ B $, representing the coordinates of the searched point $ P $ for which $ d_P $ is minimum in round $ i $, where $ 1 \leq i \leq N $.

# Constraints and clarifications

* $ 1 \leq N, Q \leq 100\ 000 $;
* $ 1 \leq L \leq 30 $;
* $ 1 \leq X_i, Y_i \leq 1\ 000\ 000\ 000 $, for any $ 1 \leq i \leq N $;
* $ 1 \leq W_i \leq 10\ 000 $, for any $ 1 \leq i \leq N $;
* $ Z_{i, j} \in \{0, 1\} $, for any $ 1 \leq i \leq N $, $ 1 \leq j \leq L $;
* $ R_j \in \{-1, 0, 1\} $, for any $ 1 \leq j \leq L $;
* $ 1 \leq K \leq N $, for each of the $ Q $ rounds;
* There are no two locations designating the same point in the plan;
* It is guaranteed that Alex respects the same strategy, represented by the sequence $ T_1, T_2, ..., T_N $, in each of the $ Q $ rounds.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 9      | $ C = 1 $ and $ 1 \leq N, Q, L, X_i, Y_i \leq 10 $ |
| 2 | 11     | $ C = 1 $ and $ T_i = i $ for $ 1 \leq i \leq L $      |
| 3 | 17      | $ C = 1 $      |
| 4 | 9      | $ C = 2 $ and $ 1 \leq N, Q, L, X_i, Y_i, W_i \leq 10 $      |
| 5 | 7     | $ C = 2 $ and $ 1 \leq N, Q \leq 100 $ and $ 1 \leq X_i, Y_i \leq 10\ 000 $ |
| 6 | 7      | $ C = 2 $ and $ 1 \leq N, Q \leq 400 $ and $ 1 \leq X_i, Y_i \leq 250\ 000 $      |
| 7 | 7      | $ C = 2 $ and $ 1 \leq N, Q \leq 1\ 000 $      |
| 8 | 12      | $ C = 2 $ and $ W_i = 1 $      |
| 8 | 21      | $ C = 2 $      |

# Example 1

`geogra.in`
```
1
7 4
1 4
1 1 0 1
3 1
1 1 1 0
7 2
0 1 0 0
9 7
1 0 1 0
3 9
0 0 0 0
5 6
0 0 1 0
4 4
1 1 0 0
5
1 0 1 0
-1 0 -1 0
-1 -1 -1 -1
-1 1 -1 -1
1 1 -1 0
```

`geogra.out`
```
1
3
7
4
2
```

# Example 2

`geogra.in`
```
2
7 4
1 4 1
1 1 0 1
3 1 1
1 1 1 0
7 2 5
0 1 0 0
9 7 1
1 0 1 0
3 9 2
0 0 0 0
5 6 1
0 0 1 0
4 4 1
1 1 0 0
5
1 0 1 0
-1 0 -1 0
-1 -1 -1 -1
-1 1 -1 -1
1 1 -1 0
```

`geogra.out`
```
9 7
3 7
5 2
7 2
3 1
```

## Explanations

In these examples, Alex's strategy is $ T_1 = 2 $, $ T_2 = 4 $, $ T_3 = 1 $, $ T_4 = 3 $.

For instance, in round 2, Alex first finds the value $ R_2 $, then the value $ R_4 $, but due to running out of time, he fails to find the values $ R_1 $ and $ R_3 $. 

For round 1, the location that respects the sequence $ R $ found by Alex is 4. For $ C = 2 $, the requested point is $ P(9,7) $, and $ d_P = 0 $.

For round 2, the locations that respect the sequence $ R $ found by Alex are 4, 5, 6. For $ C = 2 $, the requested point is $ P(3,7) $, and $ d_P = 13 $.

For round 3, the locations that respect the sequence $ R $ found by Alex are 1, 2, 3, 4, 5, 6, 7. For $ C = 2 $, the requested point is $ P(5,2) $, and $ d_P = 53 $.

For round 4, the locations that respect the sequence $ R $ found by Alex are 1, 2, 3, 7. For $ C = 2 $, the requested point is $ P(7,2) $, and $ d_P = 18 $.

For round 5, the locations that respect the sequence $ R $ found by Alex are 2, 7. For $ C = 2 $, the requested point is $ P(3,1) $, and $ d_P = 4 $.

---