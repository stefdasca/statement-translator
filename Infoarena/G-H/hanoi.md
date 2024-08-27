## Hanoi

The problem of the Towers of Hanoi is well-known: there are $3$ rods and $N$ disks, with each pair of disks having a different radius. Initially, the $N$ disks are placed on the first rod, ordered from bottom to top in descending order based on their radii. Thus, the disk with the largest radius is at the bottom while the disk with the smallest radius is at the top. The goal is to move the disks from the first to the last rod, performing the minimum number of moves. A move consists of choosing a rod that contains at least one disk and then moving the top disk to the top of any other rod. The only rule is that a disk cannot be placed on top of another disk with a smaller radius. There is a legend that in a monastery in Tibet, monks placed $N$ disks on the first rod and started to carry out moves in order to transfer them to the last rod. The legend says that when they finish, the world will end. Recently, it has been discovered that in fact, the monks used $M$ rods instead of $3$ and that the end of the world might be much closer. Determine the minimum number of steps required to move the $N$ disks from the first to the last rod, knowing that a total of $M$ rods can be used.

## Input data

The input file `hanoi.in` contains on the first line, separated by exactly one space, the numbers $N$ and $M$, with the meaning from the description.

## Output data

The output file `hanoi.out` contains a single line which contains the answer to the problem.

## Constraints

$3 \leq N \leq 250$  
$3 \leq M \leq 150$  

## Examples

`hanoi.in`  
$5 \ 4$  

`hanoi.out`  
$13$  

## Explanation

Below is a possible sequence with the minimum number of moves to transfer the disks from the initial rod to the final rod: $\dots$ A total of $13$ moves were performed.