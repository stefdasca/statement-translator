You just bought a new computer from some very obscure sources on which you want to play “*Minecraft*�. Unfortunately, the computer is not what you imagined and does not even meet the specifications you found on the internet. Nevertheless, you want to see if you can find some utility in your purchase or at least learn how it works.

Your computer features `12` registers and a set of four instructions.

Before you can tackle major projects, you want to start with something simpler, namely calculating the product of two numbers, using the assembly language described below.

# Assembly Language
* The first line of the program will contain the instruction for declaring registers. This is in the form: `registers <register1> <register2> ... <registerN>`  
This instruction declares the registers that will be used later in the program. These will be initialized with the value `0`. The register names `X, Y`, and `Out` are reserved by the system and must not appear in this instruction. This instruction can only appear once *at the beginning of the program*. Register names can be any string of characters that do not contain white spaces or the newline character. The program will only be allowed to use the declared registers or the three system reserved registers.  
*Attention!* Upper and lower case letters are distinct, so registers named `a` and `A` are two different registers.  
The registers `X` and `Y` will be initialized with the numbers to be multiplied, and the register `Out` will be initialized with `0`.
* A label has the form `label:` and represents a location in the program among the instructions, representing a code area from which execution continues in case of a `jeq` instruction, which will be explained later. Label names must follow the same rules as those for register names.
* There are three types of instructions:
1) `inc <register>` – this instruction increments the value stored in the given register by one;
2) `dec <register>` – this instruction decrements the value stored in the given register by one; if the register value is `0`, the instruction has no effect;
3) `jeq <register1> <register2> <label>` – this instruction compares the values stored in the two given registers; in case of equality, execution continues from the first instruction after the given label, otherwise execution continues from where it left off.
Instructions are executed one by one, in the order they appear in the file, or, in the case of the `jeq` instruction, from the first instruction after the given label in case of equality.
* A line beginning with `#` is treated as a comment and will be ignored.

Unfortunately, when you unpacked the computer, you dropped it. Because of this, the `inc` and `dec` instructions do not work correctly. Thus, when these instructions are executed, there is a `50%` chance that the given register will not be incremented or decremented and will remain unchanged, while execution continues with the next instruction.

Execution ends after the last line is executed and there is no instruction following in the execution flow.

Each non-empty line may contain only a comment, an instruction, or a label, but not more than one at a time. Additional spaces or empty lines added for indentation purposes are ignored.

# Constraints
* `0 \leq X, Y \leq 1000`
* The program is allowed to declare a maximum of `12` registers
* Let `T` be the number of successfully executed `inc`, `dec`, and `jeq` instructions (including dec operations that have no effect). `T` can be at most `100 000 000`
* The program is allowed to modify the registers `X` and `Y`, but the product to be calculated should be that of the initial values of the two registers
* The contestant will read nothing from `stdin` and will output the program to `stdout`
* Note: You can select "Output Only" as the language to submit only the program or declare a string in C++ across multiple lines as follows:
```cpp
std::string longString = R""""( 
line1
line2
)"""" ;
```

## Subtask 1 (10 points)
* `Y = 1`
## Subtask 2 (20 points)
* `Y = 2`
## Subtask 3 (15 points)
* `Y \leq 30`
## Subtask 4 (55 points)
* `X, Y \geq 30`. See the scoring method

# Scoring
The score obtained on the last subtask will be from `15` to `55` points, depending on the number of successfully executed instructions (the number `T` defined in the constraints).

Any solution where `T` is less than `13.5(XY + X + Y + 1)` earns `55` points.

Otherwise, let `factor` be defined as $factor = \frac{T}{XY + X + Y + 1}$. Thus, the score obtained will be $max(\frac{15.0}{55.0}, e^{-\left(\frac{factor}{13.5}-1\right)^{0.75}})$.

# Example

`stdout`

```
registers a b
# This is a comment
inc a
inc b
jeq a b label1
inc a
label1:
inc b
```

Explanations
---
**Note:** This example program does not solve anything. It is given just to familiarize you with the syntax and way of working. We will assume that the instructions `inc a` and the first `inc b` instruction are always executed, while the second `inc b` instruction is not. In reality, the same instruction may or may not be executed.

The test used will be `X = 15` and `Y = 20`.

The first instruction declares the registers `a` and `b`.

The next instruction executed will be the one on line `4` (`inc a`). The value of `a` will become `1`.

The next instruction executed will be the one on line `5` (`inc b`). The value of `b` will become `1`.

The next instruction executed will be the one on line `6` (`jeq a b label1`). Since the values of `a` and `b` are equal, the execution thread will continue with the instruction on line `9`.

The instruction on line `9` will not be executed. At this point, since there is no further instruction, the program has finished.

Finally, the value of the `Out` register is `0`. This answer is obviously incorrect, as it does not calculate the product of `X` and `Y`. To score points on this test, the answer in `Out` should be `15 * 20 = 300`.

The number of successfully executed instructions is `3`.