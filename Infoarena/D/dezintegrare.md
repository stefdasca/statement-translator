**Disintegration**

The renowned scientist Kendamovici discovered $K$ containers with radioactive substances in his lab's pantry. A scientist of his stature knows that radioactive substances decay over time according to the formula:

$$ N(t) = N_0 \cdot e^{-\lambda t} $$

Where:
- $N(t)$ - the number of particles at time $t$
- $N_0$ - the initial number of particles
- $\lambda$ - a constant that depends on the nature of the element

He now has a fantastic experiment idea! However, to execute it, he needs to know the answer to $Q$ questions of the form "Which container has the smallest number of particles at a given time $t$?". Knowing the initial number of particles and the specific constant for each container, help Kendamovici answer the given questions.

**ATTENTION** Since the initial number of particles is very large, it will be provided in logarithmic form in the input. Thus, a number $L_i$ will be given, with the property that $N_0 = 10^{L_i}$.

## Input data

The input file `dezintegrare.in` contains on the first line $K$ and $Q$, representing the number of containers in the lab pantry, and the number of questions Kendamovici needs to answer, respectively. The next $K$ lines will each contain two numbers, $L_i$ and $\lambda_i$, representing the constants for the $i$-th container. The following $Q$ lines will each contain a number $t_j$, representing a question from the scientist.

## Output data

The output file `dezintegrare.out` will contain $Q$ lines. Line $i$ will print the index of the container that represents the answer to the $i$-th question in the order from the input.

## Constraints and clarifications

$1 \leq K, Q \leq 100\ 000$

$0 \leq L_i \leq 15$, for $1 \leq i \leq K$

$0 \leq \lambda_i \leq 5$, for $1 \leq i \leq K$

$0 \leq t_j \leq 10\ 000$, for $1 \leq j \leq Q$

It is guaranteed that for each question in the input data, the answer is unique.

All numbers in the input are integers.

For any $1 \leq i < j \leq K$, the pair $(L_i, \lambda_i)$ is unique.

### Subtasks

Subtask 1 (20 points):
$1 \leq K, Q \leq 1000$

$0 \leq L_i \leq 15$

$0 \leq \lambda_i \leq 5$

Subtask 2 (another 20 points):
$1 \leq K, Q \leq 1000$

## Example

`dezintegrare.in`
```
3 2
3 7
1 1
7 6
0 1
2
1
```

`dezintegrare.out`
```
2
1
```