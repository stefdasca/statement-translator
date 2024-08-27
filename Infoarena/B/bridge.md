Bridge

Fat-Frumos embarked on a quest to find his love, the emperor's daughter, Simona, who was kidnapped by the evil dragon and taken to its cave. He prepared intensely for the battle, but he didn't know that the dragon had a surprise for him and thus lured him onto a bridge. On the bridge, Fat-Frumos can move by stepping (moving one plank to the right), jumping (moving $2$ planks to the right), standing still (staying on the same plank), or teleporting (see teleporting plank). However, the bridge is a bit peculiar, being composed of $4$ types of planks as follows: $0$ - good plank (you can stand, step, jump, or teleport on such a plank, and it can be reached in any way) $1$ - brittle plank (same as a good plank, but it can only be reached by stepping) $2$ - missing plank (if Fat-Frumos reaches such a plank, he will become the main course for the crocodiles under the bridge) $3$ - teleporting plank (you can reach such a plank in any way, and it will teleport our hero to another plank called the destination plank)

## Task

Fat-Frumos needs to coordinate his movements as efficiently as possible on the bridge, so he asks you to answer $M$ questions of the form "In how many ways can I reach plank $X$ in $K$ steps?"

## Input data

The first line of the file `bridge.in` will contain $2$ numbers $N$ and $M$ representing the number of planks and the number of questions, respectively. The next line will contain $N$ numbers between $0$ and $3$ representing the configuration of the bridge, corresponding to the above. The following lines will list the destination planks for each teleporting plank in the order they appear on the bridge, and finally, the next $M$ lines will each contain $2$ numbers $X$ and $K$ that define a question of the type "In how many ways can I reach plank $X$ in $K$ steps?"

## Output data

The output file `bridge.out` will contain $M$ lines representing the answer for each question from the input file in order.

## Constraints and clarifications

$1 < N < 4001$  
$1 < M < 30001$  
The maximum number of steps in a question will not exceed $4000$  
If plank $x$ is teleporting and has plank $y$ as its destination, then we will have the relation $x < y$  
Multiple teleporting planks can have the same destination plank  
When Fat-Frumos reaches a teleporting plank, he will be teleported to the destination plank regardless of whether he wants to or not (he cannot stand still, jump, or step from it)  
Teleporting is considered a step  
The number of ways to reach a missing plank or a teleporting plank that has a missing or brittle plank as its destination is $0$  
Fat-Frumos cannot move backwards (in one step, he will move $0 \, \, , \, \, 1$, or $2$ planks to the right or be teleported if the plank has this property)  
Initially, Fat-Frumos is outside the bridge, where he cannot stand still; on the first step, he will either step on the first plank or jump to the second if possible  
The first plank is never missing  
A teleporting plank can be reached in the same way as a good plank  
If a teleporting plank does not have a missing or brittle plank as its destination, the number of ways to reach it in $K$ steps is not necessarily $0$ (see example)

## Example

`bridge.in`  
$5 \, \, 3$  
$0 \, \, 0 \, \, 3 \, \, 1 \, \, 2$  
$4$  
$4$  
$4$  
$2 \, \, 3$  
$3 \, \, 2$  
$0 \, \, 3$

`bridge.out`  
$0$  
$3$  
$0$