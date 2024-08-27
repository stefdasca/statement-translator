# Turnuri2

In San Francisco, software companies, desiring to showcase their power, have built their headquarters in the form of very tall and very beautiful towers. Also, the city hall has decided to grant construction permits for these towers on the same street, so all the towers are lined up. Alexandra, who has just graduated from computer science school and received job offers from all these companies, has to choose which of these companies to work for. She has decided to make this choice based on the view she has from each company during lunch break. It is known that in each company, lunch breaks are taken on the roof, and from there Alexandra can see all the towers to the left or to the right up to the first one that is strictly taller than the tower she is on, inclusive.

## Task

Given $N$, the number of companies in San Francisco, and for each of the $N$ towers, its height $H_i$ and its beauty coefficient $K_i$. It is required to determine for each tower which is the most beautiful tower visible from its rooftop.

## Input data

The input file `turnuri2.in` contains on the first line the number $N$ as described above. On the next $N$ lines, there will be two numbers, $H_i$ and $K_i$, representing the height and beauty coefficient of the respective tower.

## Output data

The output file `turnuri2.out` will contain $N$ lines meaning that on the $i$-th line will be the beauty coefficient of the most beautiful tower visible from the rooftop of tower $i$.

## Constraints

$1 \leq N \leq 1\,000\,000$

$1 \leq H_i, K_i \leq 1\,000\,000\,000$

From the rooftop of tower $i$, tower $i$ is also visible

## Example

`turnuri2.in`
```
4
3 2
5 5
6 1
4 3
```

`turnuri2.out`
```
5
5
5
3
```

## Explanation

The first three towers can see tower 2, which has a beauty coefficient of $5$, being the most beautiful tower in the valley. However, the last tower cannot see this tower due to tower 3. The maximum beauty coefficient visible from its rooftop is itself, with a coefficient of $3$.