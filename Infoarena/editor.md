# Editor

An editor is considered that responds only to the pressing of six keys, namely those that have the symbols: $($, $)$, $[$, $]$, $*$ and $E$ printed on them. If one of the keys $($, $)$, $[$ or $]$ is pressed, then the respective character is displayed on the screen. If the $*$ key is pressed, the last displayed character is deleted (if no character is displayed, nothing happens). If the $E$ key is pressed, the editor will check if the string displayed on the screen is a correctly parenthesized string. A string is correctly parenthesized if it is constructed according to the rules:

$$
\text{correctly parenthesized string} = \text{empty string}
$$

$$
\text{correctly parenthesized string} = ( + \text{correctly parenthesized string} + )
$$

$$
\text{correctly parenthesized string} = [ + \text{correctly parenthesized string} + ]
$$

$$
\text{correctly parenthesized string} = \text{correctly parenthesized string} + \text{correctly parenthesized string}
$$

The concatenation of the strings $X$ and $Y$ is noted as $X+Y$. For example, $[][](())$ is a correctly parenthesized string, but $[](()][$ is not a correctly parenthesized string.

## Task

Given a sequence of key presses that ends with the E key and knowing that initially no character is displayed on the screen, you must decide if the string displayed on the screen after the key presses is a correctly parenthesized string.

## Input data

The first line of the `editor.in` file contains an integer $T$, representing the number of sequences of key presses that will follow. Each of the next $T$ lines describes a sequence of key presses.

## Output data

The `editor.out` file will contain exactly $T$ lines, one for each sequence of key presses described in the input file. On each line, you will print $:)$ (without quotes) if the string obtained from the corresponding sequence of key presses is correctly parenthesized, and $:( $ otherwise.

## Constraints and clarifications

$$1 \leq T \leq 30$$

no sequence of characters contains more than $60\ 000$ key presses

partial scores are not awarded

## Example

`editor.in`
```
3
E
[][][]E
**[]()*E
```

`editor.out`
```
:)
:)
:(
```