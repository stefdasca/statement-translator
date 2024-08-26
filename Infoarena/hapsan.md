## Hapsân

For a proper meal. Without a doubt, a restaurant that offers an "All You Can Eat" deal is a restaurant that must be visited. As often as possible. Dr. Hapsân, the character in this scenario, shares this opinion. A great enthusiast of sushi and of food offered in industrial quantities at a fixed price, Hapsân decides once again to visit the Japanese restaurant across the street, hoping that he will manage once more to cause financial damage through their offer, despite the material investment of $50$ RON. The restaurant will serve $N$ portions of sushi today on a self-service basis. More precisely, the portions of sushi will be served in the order they are created, and the client will choose at each step whether they want the current dish or not. Each dish is special, but some portions contain common ingredients (depending on the stock of ingredients throughout the day). To simplify the assumption, we will consider that there are $M$ distinct ingredients, numbered from $1$ to $M$, ingredient $i$ being part of the portions $\[A_i \dots B_i\]$. Of course, under these conditions some combinations are worse than others (for example, there may be sushi that does not contain meat!). A doctor in gourmet cuisine, Hapsân wishes to avoid any unpleasant incidents, so he has made a list of the so-called taste degrees of the $N$ types of sushi that are to be served. Hapsân wants to maximize in the end the correctness coefficient of the meal, defined as the sum of the taste degrees of the sushi he eats today. Nevertheless, Hapsân wants his meal to be as varied as possible and, in this sense, he will not accept to eat two portions of sushi that contain the same ingredient. Moreover, since he cannot stand the idea of "ruining his taste", he will accept to eat sushi $i$ after sushi $j$ (with $j < i$), only if the taste degree of sushi $i$ is strictly greater than that of sushi $j$. Since there are so many dishes available and very little decision time, you will have to help the famous doctor choose the sushi he opts to eat in the given order while respecting the specified conditions and display the maximum correctness coefficient of the meal he can achieve (of course, to demonstrate his inefficiency).

## Input data

The input file `hapsan.in` contains:
- The first line contains a natural number $N$, representing the number of sushi portions served today at the restaurant across the street.
- The second line contains $N$ natural numbers $S\[1 \dots N\]$ separated by a space, representing the taste degrees of the $N$ portions in the order they will be served.
- The third line contains a natural number $M$, representing the number of different ingredients throughout the day.
- The next $M$ lines contain two numbers $A\[i\], B\[i\]$, separated by a space, meaning ingredient $i$ was used for the sushi with order numbers from $A\[i\]$ to $B\[i\]$ inclusive.

## Output data

The output file `hapsan.out` contains a single natural number, representing the maximum correctness coefficient that can be obtained.

## Constraints

$1 \leq N, M \leq 200000$

$1 \leq S\[i\] \leq 200000$

$1 \leq A\[i\] \leq B\[i\] \leq N$

It is guaranteed that each sushi will consist of at least one ingredient.

It is estimated that in $50\%$ of cases, the restaurant wants to offer the highest quality service, so the sushi will be served in ascending order of taste degrees (i.e. $S\[i - 1\] \leq S\[i\]$).

Any resemblance to any real character is purely coincidental.

## Example

`hapsan.in`
```
4
3 5 6 4
2
1 3
3 4
```

`hapsan.out`
```
7
```

## Explanation

The maximum correctness coefficient is $7$, by choosing (in order) sushi portions $1$ and $4$.