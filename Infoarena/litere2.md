# Letters2

After the bus ride and drinks outing, Antonio is about to show his passion for foreign languages, Antonia's favorites. He has learned from reliable sources that Antonia is interested in even the most insignificant details of a foreign language, such as understanding the connections between words. Antonio knows that if he strives to understand these connections, Antonia will understand the connection between the two of them.

## Task

A text is given, consisting of words, separated by at least one space. Each word contains only lowercase letters of the English alphabet. Two words belong to the same group if they are made up of the same letters, repeated any number of times. It is required to calculate the number of distinct groups that can be formed from the words in the text, as well as the words that belong to each group.

## Input data

The input file $litere2.in$ contains the text in the unknown language understood by Antonia. The text consists of words separated by at least one space. Each word contains only lowercase letters of the English alphabet. At the end of the text, the character "." (period) will be found.

## Output data

The output file $litere2.out$ will contain, on the first line, a natural number $N$, representing the number of groups in the text. The following $N$ lines represent the composition of each group as follows: each line will contain the words that belong to a group, separated by a single space.

## Constraints and clarifications

$1 \leq L \leq 1\ 000\ 000,$ where $L$ is the length of the text.

Both the groups and the words within each group can be displayed in any order. Antonio recommends reading the single line from the input file with $gets$ or $fgets$.

## Example

$litere2.in$
```
nina face nani.
```
$litere2.out$
```
2
face
nina nani
```

$litere2.in$
```
ab aab ba bb b.
```
$litere2.out$
```
2
ab aab ba
bb b
```