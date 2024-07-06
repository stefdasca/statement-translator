Emil has a special mouse with two scroll wheels. On each scroll wheel, he can attach a circular rubber band with frequently used characters in 3D format. Pressing the scroll wheel vertically at its highest point will generate the character at the pressed point. Thus, different texts can be edited using only the mouse. The order in which the characters are printed affects the typing speed and energy consumption in the text editing process. The effort to move from one character to the next or to the previous one consumes an amount of energy equal to one unit. Pressing the wheel does not consume energy. Emil wants to find out the minimum amount of energy he needs to consume to construct a given text.

# Input data

The input file `birot.in` contains the following:

The first line contains the string of characters printed on the rubber band on the first scroll wheel.  
The second line contains the string of characters printed on the rubber band on the second scroll wheel.  
The third line contains the text that must be constructed using the mouse.

# Output data

The output file `birot.out` will contain the number representing the minimum amount of energy required to construct the given text.

# Constraints and clarifications

* The lengths of the first two strings are equal and $ \leq 90 $;
* In each of the first two strings, the characters are distinct;
* The first two strings are made up of the same characters, possibly arranged in a different order;
* The length of the string that needs to be constructed is at most equal to $ 10 \ 000 $;
* Any character in the string to be constructed is found in each of the first two strings;
* The characters that can appear in the given text and on the rubber bands are printable characters, including the space character;
* Initially, each wheel is positioned so that the first character of its respective string is at the topmost position;
* The rubber bands are positioned on the wheels so that pushing the wheels forward traverses the characters in a circular order, in the order given in the read strings.

# Example

`birot.in`
```
abo-r
ao-br
bar-ba-ra
```

`birot.out`
```
7
```

## Explanation

| command | wheel $1$ | wheel $2$ | text created | energy |
| ------- | ---------- | ---------- | ---------- | ------- |
| at first | `abo-r` | `ao-br` |  | $0$ |
| back wheel $1$ | `bo-ra` | `ao-br` |  | $1$ |
| press wheel $1$ | `bo-ra` | `ao-br` | `b` | |
| press wheel $2$ | `bo-ra` | `ao-br` | `ba` | |
| forward wheel $2$ | `bo-ra` | `rao-b` | `ba` | $2$ |
| press wheel $2$ | `bo-ra` | `rao-b` | `bar` | |
| forward wheel $2$ | `bo-ra` | `brao-` | `bar` | $3$ |
| forward wheel $2$ | `bo-ra` | `-brao` | `bar` | $4$ |
| press wheel $2$ | `bo-ra` | `-brao` | `bar` | |
| press wheel $1$ | `bo-ra` | `-brao` | `bar-b` | |
| forward wheel $1$ | `abo_r` | `-brao` | `bar-b` | $5$ |
| press wheel $1$ | `abo_r` | `-brao` | `bar-ba` | |
| press wheel $2$ | `abo_r` | `-brao` | `bar-ba` | |
| forward wheel $1$ | `rabo-` | `-brao` | `bar-ba-` | $6$ |
| press wheel $1$ | `rabo-` | `-brao` | `bar-ba-r` | |
| back wheel $1$ | `abo-r` | `-brao` | `bar-ba-r` | $7$ |
| press wheel $1$ | `abo-r` | `-brao` | `bar-ba-ra` | |