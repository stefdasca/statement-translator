Georgică is a great proofreader for the Romanian language and literature. A work consists of words (sequences of English alphabet letters in both uppercase and lowercase), separated by a single space. Georgică knows that an important part of his proofreading job is replacing forbidden words with beep.

## Task

Given a string representing a work that needs to be corrected and a forbidden word, replace all occurrences of the forbidden word in the work with beep.

## Input data

The input file `beep.in` contains on the first line the forbidden word, and on the second line the string representing the work that needs to be corrected.

## Output data

The output file `beep.out` will contain on a single line a string representing the corrected work.

## Constraints and clarifications

$1 \leq N \leq 1\ 000$, where $N$ is the length of the string.  
$1 \leq K \leq 1\ 000$, where $K$ is the length of the forbidden word.

## Example

`beep.in`
```
monthly
Infoarena Monthly se tine monthly Infoarena Monthly se tine
```

`beep.out`
```
Infoarena beep se tine beep Infoarena beep se tine
```

`beep.in`
```
e
Este oare e sau ee Sau E Sau e
```

`beep.out`
```
Este oare beep sau beep beep Sau E Sau beep
```