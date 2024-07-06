```markdown
# Task
The given `main.cpp` code reads itself, performs the XOR operation between the characters in the file, and displays the result.

Change a single character in the source code such that the result remains the same.

Access the program [here](self_xor.cpp) or from the "Attachments" section on the side.

## XOR Operation

XOR is an operation between two values that is performed on the bits of those values.

For example, `std::cout << ('a' ^ 'C');` displays $34$.

This is because the ASCII codes for `a` and `C` are $97_{(10)}$ and $67_{(10)}$ respectively.

Their binary representation is $01100001_{(2)}$ and $01000011_{(2)}$.

The XOR operation applied between the two is given by applying it to each pair of bits in the same position, the result being $00100010_{(2)}$, which is $34_{(10)}$.

~[xor.png]

Two important properties are:
- Commutativity: `a ^ b == b ^ a`
- Self-annihilation: `a ^ a == 0`

# Input data

No input is given. The cpp file reads itself.

# Output data

A number is displayed.

# Constraints and clarifications
- You must replace exactly one character in the source.
- When running, it should display the same number as before the modification.
- The contest code has been slightly modified.
- To check if you haven't mistakenly added/removed any character, the submitted source code must be 398 B in size.
```