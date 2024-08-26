X and 0

Multiple configurations of the game X and 0 are given. Considering that from these configurations the two players play optimally, determine if the player who places X has a guaranteed winning strategy.

## Task

## Input data

The input file $xsizero.in$ contains multiple configurations for a X and 0 board. Each configuration is a $3×3$ matrix containing the characters '.', 'X', and '0'. '.' signifies an empty cell, 'X' and '0' have their well-known meanings. The configurations are given in the file one after another without separators. In none of the configurations will there be $3$ aligned 'X' or '0' symbols.

## Output data

In the output file $xsizero.out$, for each test, print on a separate line the message "Test #$x$: result", where $x$ is the test number starting from $1$, and result can have the following values:

- $invalid$, if the configuration is not valid
- $win$, if 'X' wins
- $lose$, if '0' wins
- $draw$, if the game ends in a draw

## Constraints and clarifications

- The number of configurations in the input file is not specified

## Example

$xsizero.in$

    ...
    ...
    ...

    X.0
    XX.0
    .0.

    XX.
    ...
    ...

$xsizero.out$

    `Test #1: draw`
    `Test #2: win`
    `Test #3: invalid`