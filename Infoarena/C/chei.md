## Keys

You have multiple keys on a ring. Some are round (encoded with the character 'a'), others are square (encoded with the character 'b'), $\dots$, others are in the shape of a hashtag (encoded with the character 'z'). Otherwise, the keys have nothing on them to distinguish them, which is a problem. Sometimes this problem can be mitigated by the arrangement of the keys on the ring. For example, if the keys on the ring are exactly "abaa". We can say something like: "Okay, the apartment key is the only square one, the garage key is the round one that is not adjacent to the square one, and with the other two round ones it’s kind of bad, I will always have to try both of them in the worst-case (when I want to open Sorin's apartment or Sorin's cellar, for example). Since the keys move in the pocket, the ring can rotate circularly or can be turned inside out.

## Task

Given a string of characters that describes the arrangement of the keys on the ring at any given instance, count how many pairs of keys have the property that I cannot distinguish them even after analyzing the arrangement of the other keys.

## Input data

The input file `chei.in` contains a string of characters. It contains only lowercase letters of the English alphabet and ends with the character `\n`, signifying the end of the line. Each character corresponds to a type of key, depending on its shape.

## Output data

The output file `chei.out` contains the number of key pairs that cannot be distinguished.

## Constraints

$1 \leq N \leq 100\ 000$, where $N$ is the number of keys.

For 22\% of the score, $N \leq 100$

For 35\% of the score, $N \leq 2\ 000$

For 51\% of the score, $N \leq 4\ 000$

## Example

`chei.in`
```
abaa
```

`chei.out`
```
1
```