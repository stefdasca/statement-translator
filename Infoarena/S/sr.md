# String Repair

Ionel really enjoys playing with letters so, every day before going to school, he leaves a word written on the desk. His older brother, Gigel, wanting to play a prank, decided that while Ionel is at school, he would remove certain characters from the word. Given a character string $A$ (of length $N$), representing the initial word, and another character string $B$ (of length $M$) that represents the word after Gigel's evil intervention, Ionel asks you to find out which positions in the initial string were not deleted.

## Input data

The input file `sr.in` will contain on the first line the string $A$, and on the second line $B$.

## Output data

In the output file `sr.out`, you will print, on the first line, a set of $M$ indices in ascending order with the required property.

## Constraints and clarifications

$1 \leq M \leq N \leq 100\,000$

The numbering of positions in strings starts from $1$

It is guaranteed that there will always be a solution for the test data

Any correct solution can be printed

The strings $A$ and $B$ will consist only of lowercase English letters

## Example

`sr.in`
```
anaaremere
anaaer
```

`sr.out`
```
1 2 3 4 6 9
```