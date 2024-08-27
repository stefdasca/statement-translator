## Task

You are at the after-party organized after the competition. You are at the bar conversing with your friend, Eudoxiu, also known as Doxuță. You are slightly frustrated because Doxuță's team defeated you today, although you know it was just luck, the tests were weak, and ultimately, a victory on penalties is not a real victory, right? The conversation veers towards observing people in the club and the relationships between them. So far, you have noticed that there are $N$ people and $M$ courtesy relationships between them, which are bidirectional (leaving reality here). You also notice that the people can be divided into two sets $A$ and $B$, such that people in $A$ court/are courted only by people in set $B$. Doxuță seizes the opportunity to brag that he can determine if there is a perfect matching between the $N$ people. Moreover, he mocks you - a suburban term he frequently abuses - saying you probably don't know how to find a perfect matching. Completely outraged by this claim, you proudly retort: "Boss, I can determine ALL perfect matchings". You calm down a bit and realize that you actually don't know how to do that, not even how to count how many perfect matchings there are. However, if you try hard, you think you can tell the parity of the number of perfect matchings. 

## Input data

The input file `afterparty.in` will contain on its first line the number of test cases $T$. There follow $T$ test cases, each adhering to the following structure: the first line contains the numbers $N$ and $M$, signifying the number of people and the number of courtesy relationships. The next $M$ lines each contain a pair of names $X \, Y$, signifying that $X$ and $Y$ court each other reciprocally. $X$ and $Y$ will be composed of lowercase and uppercase English letters and will have a maximum length of 20 characters.

## Output data

The output file `afterparty.out` will contain $T$ lines, each containing the answer for the corresponding test case: the message "Even" if the number of perfect matchings is even, and "Odd" otherwise.

## Constraints and clarifications

1 \leq $T$ \leq 100

1 \leq $N$ \leq 100

0 \leq $M$ \leq $N \ast (N - 1) / 2$

A perfect matching in a bipartite graph is a set of edges with the property that each node is the endpoint of exactly one edge.

## Example

`afterparty.in` 
```
2
6 4
Tu CubaLibre
Mihai Restanta
CubaLibre Doxuta
Doxuta Comisia
4 3
Doxuta Comisia
Doxuta Mafia
Doxuta PorCostel
```

`afterparty.out` 
```
Odd
Even
```

## Explanation

In the first example, there is a unique perfect matching. In the second example, although Doxuță is very well connected with all the celebrities at the competition, no perfect matching can be formed.