Miki and Livia are two witches who want to resolve a dispute. Naturally, they will conjure armies of zombies that will fight each other in their place. Each zombie $ z $ has two attributes: an attack level $ a_z $ and a resilience level $ r_z $.

The two have just initiated the first round, and Livia has conjured $ N $ zombies which she sent to attack. Miki, in turn, has conjured $ M $ zombies she will use to block Livia's attack. For each of the zombies she conjured, Miki can choose to send it to block one of Livia's unblocked zombies. She can leave some of Livia's zombies unblocked and does not need to send all $ M $ zombies to fight.

Then, the zombies fight each other: each blocked attacking zombie and the blocking zombie fight individually, launching simultaneous attacks. A zombie $ x $ will be eliminated by the attack of a zombie $ y $ if $ r_x < a_y $. Depending on the attack and resilience levels of the zombies in a fight, zero, one, or both could be eliminated as a result of the battle.

After the fights are concluded, Livia scores a number of points equal to the sum of the attack levels of her **unblocked** zombies. The blocked attacking zombies, the blocking zombies, and the unused zombies by Miki for blocking do not score points for any witch.

Then, Miki and Livia recall the zombies that are not eliminated, and the battle continues... however, we are only interested in the first round.

After seeing the zombies sent by Livia to attack, Miki thinks about strategically sending her zombies to block to fulfill one of the following objectives in the first attack round:

- **Objective 1**: Livia scores as few points as possible.
- **Objective 2**: Livia scores as few points as possible, without any of Miki's zombies being eliminated.
- **Objective 3**: Livia scores as few points as possible, preferring that the number of eliminated zombies of Miki to achieve this purpose is minimal.
- **Objective 4**: Miki eliminates as many of Livia's zombies as possible.
- **Objective 5**: Miki eliminates as many of Livia's zombies as possible, without any of Miki's zombies being eliminated.

Your goal is to help Miki block Livia's zombies accordingly to achieve the desired objective.

# Input data

The first line contains three integers $ O $, $ N $, and $ M $, representing the objective desired by Miki, the number of zombies sent by Livia to attack, and the number of zombies Miki has available.

The next $ N $ lines contain pairs of integers $ a $ and $ r $; the $ i $-th of these pairs represents the attack and resilience levels of the $ i $-th zombie sent by Livia to attack.

The next $ M $ lines contain pairs of integers $ a $ and $ r $; the $ i $-th of these pairs represents the attack and resilience levels of the $ i $-th zombie available to Miki.

# Output data

Print a single line containing $ M $ numbers separated by a space, $ x_1, x_2, \dots, x_M $, representing, for each $ i $ from 1 to $ M $, that Miki will use zombie $ i $ to block zombie $ x_i $ sent by Livia. If $ x_i $ is 0, it means Miki will not use zombie $ i $ to block any zombie. If there are multiple correct solutions, you may print any of them.

# Constraints and clarifications

- $ 1 \leq N, M \leq 500\,000 $
- $ 1 \leq O \leq 5 $
- The attack and resilience levels of all zombies are between $ 1 $ and $ 2\,000\,000\,000 $ inclusive.
- There are no two different zombies with equal attack levels.
- There are no two different zombies with equal resilience levels.
- There may be two different zombies for which the attack level of one is equal to the resilience level of the other.

| #  | Points          | Constraints                               |
|----|----------------|----------------------------------------|
| 1  | 2              | $ O = 1 $ and $ 1 \le N, M \le 5\,000 $  |
| 2  | 6              | $ O = 2 $ and $ 1 \le N, M \le 5\,000 $  |
| 3  | 7              | $ O = 3 $ and $ 1 \le N, M \le 5\,000 $  |
| 4  | 8              | $ O = 4 $ and $ 1 \le N, M \le 5\,000 $  |
| 5  | 13             | $ O = 5 $ and $ 1 \le N, M \le 5\,000 $  |
| 6  | 8              | $ O = 1 $  |
| 7  | 12             | $ O = 2 $  |
| 8  | 13             | $ O = 3 $  |
| 9  | 14             | $ O = 4 $  |
| 10 | 17             | $ O = 5 $  |

# Example 1

`stdin`
```
1 4 2
5 4
4 1
3 2
2 3
6 6
1 5
```

`stdout`
```
1 2
```

## Explanation

Miki wants to defend in such a way that Livia scores as few points as possible.

To do this, she sends her zombie 1 to block Livia's zombie 1, and her zombie 2 to block Livia's zombie 2.

Livia's zombies 3 and 4 are unblocked and score a total of $ 3 + 2 = 5 $ points, which is the minimum possible.

# Example 2

`stdin`
```
2 4 4
5 4
4 1
3 5
2 2
8 8
7 7
1 3
6 6
```

`stdout`
```
1 2 4 3
```

## Explanation

Miki wants to defend in such a way that Livia scores as few points as possible, and none of Miki's zombies are eliminated.

Miki blocks as follows:  
Zombie 1 of Miki blocks zombie 1 of Livia,  
Zombie 2 of Miki blocks zombie 2 of Livia,  
Zombie 3 of Miki blocks zombie 4 of Livia,  
Zombie 4 of Miki blocks zombie 3 of Livia.

Each blocking zombie has a resilience level higher than the attack level of the zombie it blocked, thus none of Miki's zombies are eliminated.

Livia scores 0 points - all her zombies are blocked.

# Example 3

`stdin`
```
3 4 3
5 6
4 1
3 3
2 2
6 5
7 7
1 4
```

`stdout`
```
2 1 3
```

## Explanation

Miki wants to defend in such a way that Livia scores as few points as possible, and the number of Miki’s zombies eliminated as a result of the battles to achieve this objective is minimal.

Miki blocks as follows:  
Her zombie 1 blocks Livia's zombie 2,  
Her zombie 2 blocks Livia's zombie 1,  
Her zombie 3 blocks Livia's zombie 3.

Blocking this way, Livia scores 2 points, and none of Miki’s zombies are eliminated; there are also other ways to block so Livia scores 2 points, but those are not valid answers because at least one of Miki's zombies would be eliminated.

# Example 4

`stdin`
```
4 4 3
5 6
4 1
3 3
2 2
6 5
7 7
1 4
```

`stdout`
```
3 2 0
```

## Explanation

Miki wants to defend in such a way as to eliminate as many of Livia's zombies as possible.

She will eliminate Livia's zombie 3 with her zombie 1, and Livia's zombie 2 with her zombie 2; there is no way of blocking that eliminates more of Livia's zombies.

# Example 5

`stdin`
```
5 4 3
5 6
4 1
3 3
2 2
6 5
7 7
1 4
```

`stdout`
```
3 2 0
```

## Explanation

Miki wants to defend in such a way as to eliminate as many of Livia's zombies as possible, and none of Miki's zombies are eliminated.

She will eliminate Livia's zombie 3 with her zombie 1, and Livia's zombie 2 with her zombie 2; none of Miki's zombies die in this way. There is no other way to block where Miki eliminates more of Livia's zombies, and none of Miki's zombies are eliminated.