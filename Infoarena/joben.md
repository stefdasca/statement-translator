# Joben

Marcel has $T$ pairs of strings containing lowercase letters of the English alphabet. He also has a magic hat that can perform one of the following two operations:
- permutation: the characters of the string introduced in the hat are permuted. For example, if the string $abb$ is introduced, it can become $abb$, $bab$, or $bba$.
- transformation: for each character in the set $\{'a', \dots, 'z'\}$ a character from the same set $\{'a', \dots, 'z'\}$ is chosen, such that any two different letters correspond to different characters. Each character in the string introduced in the hat is replaced with its corresponding character. For example, transformations $abcca -> zdffz$ and $rdbarb -> rbdkrd$ are valid, while transformations $abcca -> zdfgz$ and $abcde -> ghhij$ are not valid.

## Task

For each of the $T$ pairs of strings, determine if the second string can be obtained from the first string by performing any number of operations with the hat.

## Input data

The input file `joben.in` contains on the first line the integer $T$. The following $2*T$ lines describe the pairs of strings, one string per line. For any $1 \leq i \leq T$, the strings constituting pair $i$ are contained on lines $2*i$ and $2*i+1$ of the file.

## Output data

The output file `joben.out` will contain $T$ lines. On line $i$ $(1 \leq i \leq T)$, print the message $DA$ if for the $i$-th pair the second string can be obtained from the first string after any number of hat operations, otherwise $NU$ if not.

## Constraints and clarifications

$1 \leq T \leq 100$  
The length of any string does not exceed $100000$ characters.  
Two strings belonging to the same pair have the same number of characters.

## Example

`joben.in`
```
2
esarfa
iepure
morcov
pepene
```

`joben.out`
```
DA
NU
```

## Explanation

In the first test, one possible solution is $esarfa -> aserfe -> aesfre -> iepure$, consisting of two transformations and one permutation. 
For the second test, there is no sequence of operations that can transform the string $morcov$ into the string $pepene$.