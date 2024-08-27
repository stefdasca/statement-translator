## Task

In a village, there are $N$ houses in a circular order. The houses are numbered clockwise from $1$ to $N$. For example, if $N = 8$, then the village would look like this: Additionally, the village has $M$ streets, each connecting two houses and lying inside the circle. The streets do not intersect each other, but their endpoints can be the same. Since a festival is approaching, the villagers want to paint their houses. Unfortunately, this is not very simple because they do not want to have boring streets in their village. They consider a street boring if the houses at the street's endpoints are the same color. Now it's your turn! Because paint is expensive, the villagers want to use a minimum number of colors. Help them by writing a program that finds the minimum number of colors needed and finds a convenient way to paint the houses.

## Input data

The input file `circle.in` contains on the first line the natural numbers $N$ and $M$ - the number of houses and the number of streets in the village. Each of the next $M$ lines contains two numbers $u$ and $v$ - they signify that there is a street between the houses numbered $u$ and $v$.

## Output data

The output file `circle.out` will contain on the first line the number $K$ - the minimum number of colors needed. On the next line, it will contain $N$ numbers - the colors in which each house must be painted. The colors are numbered from $1$ to $K$. If there are multiple correct answers, you can display any of them.

## Constraints and clarifications

$ 2 \leq N \leq 5\ *\ 10^5$

$ 1 \leq M \leq 5\ *\ 10^5$

## Example

`circle.in`

```
6 5
1 2
2 3
1 4
3 4
6 5
```

`circle.out`

```
2
1 2 1 2 1 2
```