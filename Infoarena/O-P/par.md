# Pair

Ioana has just learned in school about round parentheses and correctly parenthesized strings. A string is correctly parenthesized if it is constructed according to the following rules: $<correctly \ parenthesized \ string> = <empty \ string>$ $<correctly \ parenthesized \ string> = "(" + <correctly \ parenthesized \ string> + ")"$ $<correctly \ parenthesized \ string> = <correctly \ parenthesized \ string> + <correctly \ parenthesized \ string>$ For example $ (()) $ and $ ()() $ are correctly parenthesized strings, but $ )() $ or $ (()($ are not correctly parenthesized. Andrei has given Ioana a string composed of $ N $ open or closed parentheses and she is now thinking of reversing some parentheses (changing an open parenthesis to a closed one or vice versa) so that the final string is correctly parenthesized. Help Ioana determine the minimum number of reversals that need to be performed so that the final string is correctly parenthesized.

## Input data

The input file par.in contains on the first line the natural number $ N $, having the meaning explained in the statement. The second line contains $ N $ characters representing the string of parentheses provided by Andrei.

## Output data

The output file par.out will contain a single number, representing the minimum number of reversals that need to be performed so that the final string is correctly parenthesized. If there is no solution, it will print the number $ -1 $.

## Constraints

$1 \leq N \leq 5000 $

## Example

`par.in` `par.out`
```
4
((()
1
```

## Explanation

The third parenthesis is reversed and the string becomes $ (()) $, which is a correctly parenthesized string.