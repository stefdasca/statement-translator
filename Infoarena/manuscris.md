## Task

Ghoberscris = the "written" form of the Ghoberian language  
Ghoberian Language = the spoken language of the Ghoberians  
Ghoberians = the inhabitants of the country Ghobera  
In this problem, we are particularly interested in analyzing sentences from the Ghoberian language. Ghoberscris is a particularly impractical form of writing and has not survived to this day because only girls could differentiate so many colors. First, in Ghoberscris, words are not represented by graphical signs but by colors (the Ghoberians had many colors). Secondly, the sentence structure is irrelevant to its meaning. The meaning of a sentence is strictly determined by the words that compose it and the connections between them. Therefore, a sentence written in Ghoberscris has the form of a tree where each node represents a word (depending on its color). Unfortunately, the manuscripts that have survived were deteriorated by time and the colors on them have become indecipherable, but the structure of the sentence has been preserved. Given the structure of a sentence (in the form of a tree) and the number $k$ of distinct words/colors in the Ghoberian language, calculate the number of distinct meanings the sentence could have initially had. Two meanings are considered ghober-different if there is no renumbering of nodes that results in two identically colored trees.

More precisely: Two trees $G(V, E, c: V \to C)$ and $G'(V, E', c': V \to C)$ are considered "the same" (isomorphic) if there exists a bijective function $f: V \to V'$ such that $c'(f(v)) = c(v)$ for any $v \in V$ and $E' = \{(f(v), f(u)) | (v, u) \in E\}$ where $C = \{1, 2 \dots k\}$ and $V = \{1, 2 \dots n\}$.

## Input data

The input file `manuscris.in` contains on the first line two numbers, $n$ and $k$, representing the number of words in the given sentence and the number of words/colors in the Ghoberian language, respectively. On the next $n - 1$ lines, there will be two numbers, $a$ and $b$ with the meaning that there is a connection between the words $a$ and $b$ in the sentence.

## Output data

In the output file `manuscris.out`, on the first line, print the number of possible different meanings of the given sentence, modulo $10^9 + 7$.

## Constraints

$2 \leq N \leq 200000$

$2 \leq K \leq 1000000$

For tests worth 15 points 
$N \leq 7$ and $K = 2$

For other tests worth 5 points 
$N = 8$ and $K = 2$

For other tests worth 5 points 
$N = 9$ and $K = 2$

For other tests worth 5 points 
$N = 10$ and $K = 2$

## Example

`manuscris.in`
```
2 2
1 2
```

`manuscris.out`
```
3
```

`manuscris.in`
```
3 3
1 2
1 3
```

`manuscris.out`
```
18
```

`manuscris.in`
```
4 7
1 2
2 3
2 4
```

`manuscris.out`
```
588
```

`manuscris.in`
```
9 3
8 4
3 5
5 7
3 6
8 3
7 2
6 9
1 3
```

`manuscris.out`
```
10935
```

## Explanation

In the first example, there are three cases: 
1. Both nodes have color 1 
2. Both nodes have color 2 
3. One node has color 1, and the other has color 2