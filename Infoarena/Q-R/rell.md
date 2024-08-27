## Task

"The whole damned Alliance needs to hear what we've been through. There may not be much time left." In the magical land of the Jade Forest, our hero Rell faces an unexpected ambush by monkeys. Each monkey has a certain number of health points. A monkey is considered defeated when its health points reach $0$. It is known that our hero has $3$ abilities at his disposal to attack a monkey: The strong ability which deals $A1$ health points of damage and takes $T1$ seconds to regenerate. The stronger ability which deals $A2$ health points of damage and takes $T2$ seconds to regenerate. The strongest ability which deals $A3$ health points of damage and takes $T3$ seconds to regenerate. Each of the hero's abilities has a preparation time of $1$ second. For example, if Rell uses the strong ability at second $T$, it will deal $A1$ health points of damage at second $T + 1$. More precisely, if Rell attacks a monkey which has $X$ health points at second $T$ with the strong ability, that monkey will remain with $\text{max}(X - A1, 0)$ health points at second $T + 1$, and our hero will be able to use the strong ability again only at second $T + T1 + 1$. Everyone knows that raccoons are very curious creatures by nature. Our raccoon, named Socks, is no exception to this rule. He asks Rell $Q$ questions in the following manner: What is the minimum time in which you can defeat a monkey with $X$ health points? To prove his mastery in martial arts, Rell will do everything in his power to, at the end of the battle, report not only the minimum time record to Socks but also to have the sum $A1 * K1 + A2 * K2 + A3 * K3$ minimized, where $K_i$ is the number of remaining seconds for the $i$-th ability to regenerate from the moment the monkey is defeated. Answer Socks' questions! For each question, display the minimum time in which Rell can defeat the monkey, and from all the ways in which Rell can achieve this minimum time, find the way with the minimum sum $A1 * K1 + A2 * K2 + A3 * K3$, and display it! Upon completion of this quest, you will gain: $100$ points of experience 

## Input data

The input file `rell.in` contains on the first line the natural numbers $A1, A2, A3$, separated by a space. 
The second line contains the natural numbers $T1, T2, T3$, separated by a space. 
The third line contains the number $Q$. 
Each of the following $Q$ lines contains a single natural number $X$, with the meaning from the statement. 

## Output data

The output file `rell.out` will contain $Q$ lines, each line $i$ containing two natural numbers. The first number represents the minimum time in which Rell can defeat the monkey, and the second number represents the minimum sum that Rell can have at the end of the battle with that minimum time. 

## Constraints

$1 \leq A1, A2, A3 \leq 50$ 

$1 \leq T1, T2, T3 \leq 50$ 

$1 \leq Q \leq 100$ 

$1 \leq X \leq 100$ 

Rell cannot use multiple abilities at the same time! 

## Example

`rell.in`  
```
1 2 3
1 2 3
20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
```

`rell.out`  
```
1 1
1 4
1 9
2 7
2 10
3 6
4 3
4 7
5 3
5 9
6 7
6 9
7 6
7 10
8 6
9 3
9 9
10 7
10 9
11 6
```

## Explanation

For a monkey with $1$ health point, Rell has 3 ways to defeat it in the minimum time of $1$ second: 
- He will use the strongest ability. When the monkey is defeated, we will have: $K1 = 0, K2 = 0, K3 = 3$. 
- He will use the stronger ability. When the monkey is defeated, we will have: $K1 = 0, K2 = 2, K3 = 0$. 
- He will use the strong ability. When the monkey is defeated, we will have: $K1 = 1, K2 = 0, K3 = 0$. 
Rell will choose the third option because the resulting sum is minimal.