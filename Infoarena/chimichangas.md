# Chimichangas

Tired after filming his last movie, Deadpool decided to take a little break and open a restaurant in Canada. Deadpool is also the head chef and he can cook only one type of dish: the chimichanga. For those who don’t know what a chimichanga is (shame on you!), you can think of it as a fried burrito. Deadpool can cook $N$ unique types of chimichangas, each having a natural number of calories, at most equal to $C$. The restaurant has become very famous. Today there are $Q$ customers in line, and Deadpool wants to impress them. Each customer orders $K$ kinds of dishes and knows exactly how many calories they need to consume. More precisely, customer $i$ needs to consume $meal_i$ calories. Each customer would like to know in how many ways they can consume the required number of calories for their diet by eating exactly $K$ chimichangas (not necessarily of different types).

## Input data

The input file `chimichangas.in` will contain on the first line 2 natural numbers, $N$ and $K$. On the next line, there are $N$ distinct values, $calorie_i$, representing the number of calories in the $i$-th type of chimichanga. On the third line, the number of questions $Q$ is found. Then, for each customer $1 \leq i \leq Q$, the $i + 3$ line contains the number of calories required for their diet, $meal_i$.

## Output data

The output file `chimichangas.out` will contain $Q$ lines. Each line will contain a single number, the answer to the corresponding query. Because this number can be large, you are required to display the remainder when divided by $2999$.

## Constraints and clarifications

$1 \leq calorie_i \leq C$ for $1 \leq i \leq N$  
$1 \leq meal_i \leq W$ for $1 \leq i \leq Q$  
$1 \leq C \times K \leq 100\ 000$  
$1 \leq C \leq N$  
$0 \leq W \leq 1\ 000\ 000\ 000$  
$1 \leq Q \leq 200\ 000$  
Deadpool has an unlimited quantity of each type of chimichanga at his disposal. The order in which each customer eats is relevant, for example, $(1 + 2)$ is different from $(2 + 1)$. There will be no two types of chimichangas with the same number of calories. The values must be displayed modulo $2999$.

The tests will be grouped as follows:

## Additional constraints

1. 20 points: $N \leq 100$, $K \leq 10$, $W \leq 2\ 000$, and $C \leq 500$
2. 5 points: $K = 2$, $W \leq 60\ 000$, and $Q \leq 100$
3. 25 points: $C \times K \leq 10\ 000$ and $W \leq 50\ 000$
4. 20 points: $C \times K \leq 30\ 000$
5. 30 points: none

## Example

`chimichangas.in`  
```
3 4
1 2 5
3
5
4
8
```
`chimichangas.out`  
```
4
1
5
```

## Explanation

There are 4 ways to consume 5 calories: $(1 + 1 + 1 + 2)$, $(1 + 1 + 2 + 1)$, $(1 + 2 + 1 + 1)$, $(2 + 1 + 1 + 1)$. There is only one way to consume 4 calories: $(1 + 1 + 1 + 1)$. There are 5 ways to consume 8 calories: $(1 + 1 + 1 + 5)$, $(1 + 1 + 5 + 1)$, $(1 + 5 + 1 + 1)$, $(5 + 1 + 1 + 1)$, $(2 + 2 + 2 + 2)$.