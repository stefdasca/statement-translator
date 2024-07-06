Displaying information using LEDs is a common practice today. Besides their low power consumption, LEDs offer a spectacular and attractive display. As aspiring computer scientists, it is useful for us to have a **binary clock** at our disposal. Such a clock has 8 columns of LEDs. Each digit in the hour display corresponds to a vertical column with a maximum of $4$ LEDs. Each hour digit is represented in binary, and the corresponding column of LEDs visualizes this representation, with the binary position $0$ being at the base of the column. Thus, the time `10:35:42.68` corresponds to the configuration:

~[ceas.png|align=center]

It is evident that the first column needs only $2$ LEDs, because this column visualizes only the values $0, 1$, and $2$. Similarly, columns $3$ and $5$ need only $3$ LEDs, as the values that need to be displayed are $0, 1, 2, 3, 4, 5$. In the other columns, the values $7, 8$, and $9$ will also be displayed, so $4$ LEDs are necessary.

# Task

Given the binary clock configuration at a certain moment and a period of time expressed in hundredths of a second, determine and display the clock configuration after that period of time passes.

# Input data

The input file `ceas.in` contains $5$ lines. The first $4$ lines contain the initial configuration of the clock, and the $5$-th line contains the time period $t$. For the clock configuration, the characters used are ` ` (space), `x`, and `o`. The character ` ` represents the position of a missing LED, the character `x` represents the position of an unlit LED, and the character `o` represents the position of a lit LED.

# Output data

The output file `ceas.out` contains the final configuration of the clock on the first $4$ lines in the format described above, using the same characters ` `, `x`, `o`. The $4$ lines start from column $1$.

# Constraints and clarifications

* $0 \leq t \leq 2 \cdot 10^9$;

# Example

`ceas.in`
```
 x x xxo
 xxooxox
xxoxxoox
oxooxxxx
123
```

`ceas.out`
```
 x x xox
 xxooxxx
xxoxxoxx
oxooxooo
```

## Explanation

The example represents the configuration for the hour mentioned in the problem text, `10:35:42.68`, and the time period $t$ is $123$ hundredths of a second. The final configuration represents the time `10:35:43.91`.