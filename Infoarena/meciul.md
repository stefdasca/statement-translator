# Costel Pig and the Match

Oberyn Martell and Gregor Clegane are dueling in a "trial-by-combat". The fight is particularly important because Tyrion Lannister's life is at stake. Oberyn and Gregor measure their strength in the way only the best fighters in Westeros could compete, a Starcraft match. The one overseeing the battle is none other than Costel Pig. Oberyn and Gregor both play as Terrans, and they both meet in the middle of the map with an army of marines. Unfortunately, as we all know, pigs cannot distinguish colors very well, so Costel Pig does not really understand what is happening. All he sees are marines, and from time to time, he sees two marines shooting at each other. Moreover, there is a chance that Costel Pig's eyes deceive him, and sometimes he just thinks that two marines are shooting at each other. People are starting to wonder if Costel Pig is the right person to oversee this important battle. It is our mission to dispel these doubts. You will be given $M$ observations made by Costel Pig. An observation consists of Costel Pig seeing marine $x$ and marine $y$ shooting at each other. We know that two marines from the same team (either Oberyn's or Gregor's) can never shoot at each other. Your mission is to give a verdict for each observation, stating whether it is correct or not. An observation made by Costel Pig is correct if, considering this observation and all previous correct observations, there is a way to split the marines into "Oberyn's team" and "Gregor's team" such that no two marines from the same team have attacked each other. "Elia Martell !!! You rushed her! You cheesed her! You killed her SCV s !"

## Input data

The input file `meciul.in` will contain on the first line the number of tests $T$. A test has the following structure: the first line contains the numbers $N$ and $M$, and the next $M$ lines contain a pair $(x, y)$ describing an observation made by Costel Pig.

## Output data

The output file `meciul.out` will contain a line with the verdict for each observation made by Costel Pig. The line will contain "YES" if the observation does not contradict the previous correct observations. Otherwise, the answer will be "NO".

## Constraints

$2 \leq N \leq 100000$

$1 \leq M \leq 100000$

$1 \leq x, y \leq N$, $x \neq y$ for any observation

## Example

`meciul.in`

```
1
3 3
1 2
2 3
1 3
```

`meciul.out`

```
YES
YES
NO
```

## Explanation

Piggy Azalea.