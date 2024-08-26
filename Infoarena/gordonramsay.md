Gordon Ramsay

After recent results, Semicerc was so ashamed that they decided to open a restaurant together with Giotozila, who is collecting money for a more resistant trash can. Like any business, owning a restaurant is not easy. You must ensure that ingredients are always available in the refrigerators to satisfy as many customers as possible (implicitly to make as much money as possible). Additionally, you must ensure that the ingredients are always fresh so that you are not responsible for food poisoning or other illnesses. In this fictional world, the day lasts $N$ hours, and every hour a customer comes, whose dish you know in advance. The menu of this restaurant contains $K$ dishes. We consider that each dish consists of a single ingredient. Each ingredient is defined by cost, profit, and resistance. The cost of an ingredient is the amount of money paid to buy one unit of a certain ingredient, the profit is the amount of money earned if you sell the dish corresponding to an ingredient, and the resistance represents the number of hours in which the ingredient is fresh. For the procurement of ingredients, the restaurant owns a blatmobil that comes every $t$ seconds starting from hour $0$, so at moments $0$, $t$, $2 * t$, $3 * t$, $4 * t$, $\dots$, $q * t$ where $q * t < N$. It comes with fresh ingredients from the 24/7 store, namely $x_1$ units of the first ingredient, $x_2$ units of the second ingredient, $\dots$, $x_K$ of the $K$-th ingredient. Thus, every time the blatmobil comes, the owners must pay $x_1 * cost_1 + x_2 * cost_2 + \dots + x_K * cost_K JC$ (Junior Coins). For sanitary reasons, the ingredients that were in the refrigerator before will be thrown away. A working day functions as follows: every hour a customer comes who orders a dish; if the refrigerator contains the necessary ingredient for the dish, it will be served with that dish, the customer will be happy, and will leave $profit_fel JC$, otherwise, they will leave dissatisfied and leave no $JC$.

## Task
Your goal is to find $t$, $x_1$, $x_2$, $\dots$, $x_K$ with the significance from the statement so that you obtain maximum profit.

## Input data
The input file `gordonramsay.in` will contain on the first line the numbers $N$ and $K$ representing the number of hours in a day and the number of dishes on the menu, respectively. The second line will contain an array of $N$ numbers which represent the orders of each person. The next $K$ lines will contain triplets of numbers, the $i$-th line, $1 \leq i \leq K$, containing the numbers $cost_i$, $profit_i$, and $resistance_i$.

## Output data
The output file `gordonramsay.out` will contain on the first line the maximum profit obtained, on the second line the number $t$ with the significance from the statement, and on the third line $K$ numbers $x_1$, $x_2$, $\dots$, $x_K$ with the significance from the statement.

## Constraints and clarifications
$1 \leq cost_i$, $profit_i$, $resistență_i \leq 10^9$

$1 \leq i \leq N$

The first customer comes at hour $0$, the second at hour $1$, $\dots$, the $N$-th at hour $N - 1$

The numbers in the output must be natural numbers

$1 \leq t \leq N$

$0 \leq x_i \leq N$

$1 \leq i \leq K$

A food item brought at moment $i$ can be used to satisfy any customer coming to the restaurant in the interval $[i, i + \min(t, resistance\_food))$

If there are multiple solutions that yield the maximum profit, any solution can be displayed.

Subtask Rotten (Penal code for violating sanitary standards) - 10 points (tests 1-2): $N * K \leq 100$

Subtask Raw (Food poisoning) - 15 points (tests 3-5): $N * K \leq 500$, $N \leq 100$

Subtask Burnt (Disgusting) - 15 points (tests 6-8): $N * K \leq 2 \ 10^4$, $N \leq 4000$

Subtask Well done (almost OK, let's say) - 30 points (tests 9-14): $N * K \leq 2 \ 10^5$

Subtask Medium rare (Perfect) - 30 points (tests 15-20): $N * K \leq 2 \ 10^6$

## Example

`gordonramsay.in`
```
12 3
2 1 1 1 2 1 1 1 2 3 1 1
2 8 5
7 15 11
2 3 2
```

`gordonramsay.out`
```
70
4
3 1 0
```

## Explanation

The blatmobil brings supplies 3 times (at moments $0$, $4$, $8$), so Semicerc and Giotozila will pay $3 * (cost_1 * x_1 + cost_2 * x_2 + cost_3 * x_3) = 3 * (2 * 3 + 7 * 1 + 2 * 0) = 39 JC$. From the first ingredient, we will have 3 pieces that will be valid at all moments in the interval $[0, 4) $ (it would have been the interval $[0, 5)$, but at moment $4$ the blatmobil comes again and the refrigerator is emptied), 3 pieces that will be valid at all moments in the interval $[4, 8)$ and 3 pieces that will be valid at all moments in the interval $[8, 12)$. With the first 3 pieces, we can satisfy the orders at moments $1, 2, 3$, with the next 3 pieces the orders $5, 6, 7$, and with the last 3 pieces, we satisfy the orders $10, 11$, in total 8 orders. From the second ingredient, we will have one piece valid in the interval $[0, 4)$, one piece valid in the interval $[4, 8)$, and one piece valid in the interval $[8, 12)$. With all these pieces we satisfy all orders at moments $0$, $4$, $8$, in total 3 orders. The total profit, therefore, is $8 * profit_1 + 3 * profit_2 + 0 * profit_3 - 39 = 8 * 8 + 3 * 15 + 0 - 39 = 70 JC$.

Note: If we had $x_3 = 1$, we would have had one piece valid in the interval $[0, 2)$ (after 2 hours, the third food item expires), one piece valid in the interval $[4, 6)$, and one piece valid in the interval $[8, 10)$.