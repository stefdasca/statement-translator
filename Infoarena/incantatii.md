## Task

Madeline studies the psychology of members of a recently formed terrorist group. She knows that before each attack, the members participate in a series of satanic rituals, during which a series of incantations are recited. An incantation is a string of characters consisting of both lowercase and uppercase English letters, formed from 3 sequences: the introduction - consisting exclusively of lowercase letters; the body - consisting exclusively of uppercase letters; the ending - consisting exclusively of lowercase letters, being the introduction mirrored. Madeline has a list of all the incantations recited during the rituals from the group's formation to the present, in chronological order. However, to create psychological profiles of the members, Madeline needs the list of incantations sorted lexicographically. Madeline has provided you with the list of incantations in chronological order and has asked you to provide, by the end of the contest, the list sorted lexicographically.

## Input data

The input file `incantatii.in` contains the natural number $N$ on the first line, representing the number of incantations, and on the next $N$ lines, an incantation on each line.

## Output data

In the output file `incantatii.out` will contain $N$ lines with the $N$ incantations, in lexicographic order, one on each line.

## Constraints and clarifications

$1 \leq N \leq 1\,000\,000$

For 30% of the tests, it is guaranteed that $N \leq 1\,000$.

Uppercase letters are smaller, in lexicographic order, than lowercase letters.

Each of the 3 sequences of an incantation are non-empty and have a length of at most 3 characters.

In all incantations, at most 7 lowercase letters and 7 uppercase letters are used.

It is possible for some incantations to be recited multiple times.

The consequence of failing to meet Madeline's request is well known and need not be mentioned.

## Example

`incantatii.in` `incantatii.out`

```
4
zoaDFGaoz
yxxCEDxxy
zoCGoz
cyABCyc
```

```
cyABCyc
cyABCyc
yxxCEDxxy
zoCGoz
zoaDFGaoz
```

## Explanation

The incantations in the example use:

6 lowercase letters: $z$, $o$, $a$, $y$, $x$, $c$

7 uppercase letters: $D$, $F$, $G$, $C$, $E$, $A$, $B$.