# Zip

A certain student at some university has a homework assignment for a certain subject to write an archiving program. The student aims to implement the following algorithm: The content of the file to be archived is divided into $M$ pieces, each having exactly $K$ bytes. For two consecutive pieces, the longest sequence of bytes at the end of the first piece that also appears at the beginning of the second piece is determined. The actual archiving is done by writing the pieces to the file in such a way that the sequences that appear both at the end of the current piece and at the beginning of the next piece appear only once. Due to an error in the program, other pieces of length $K$ have slipped between the pieces of the file, and the order of the pieces has also changed. Furthermore, if there were identical pieces in the original file, they may appear fewer times as a result of the error.

## Task

Archive the original file, knowing that it is made up of the pieces that lead to an optimal archiving in the sense that the resulting file after archiving has the minimal length.

## Input data

The first line of the input file `zip.in` contains three natural numbers: $N$ (the total number of pieces obtained by the student's program), $M$ (the number of pieces in the original file) and $K$ (the length in bytes of the pieces). The three numbers are separated by a space. The next $N$ lines each contain $K$ characters, forming the pieces obtained by the student.

## Output data

The output file `zip.out` will contain the length of the archived file.

## Constraints and clarifications

$1 \leq M \leq N \leq 100$

$1 \leq K \leq 100$

## Example

`zip.in`

5 2 4

rado

dora

arad

oboa

aaaa

`zip.out`

5

## Explanation

The original file was made up of the pieces `arad` and `rado`. The longest sequence that satisfies the conditions is `rad`, so the archived form of the file will be `arado`, having five bytes.