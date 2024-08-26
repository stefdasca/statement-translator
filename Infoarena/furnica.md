## The Ant

An ant finds itself in a square-shaped ant mound, composed of rooms that are also square-shaped. One day, the ant departs from its room and begins to wander through the mound. Each day, it will move from the room it is in to an adjacent room, through which it may have passed on a previous day. An adjacent room is defined as a square that shares a side with the square (room) in which the ant is currently located. The ant does not stay in the same room for two consecutive days. The initial position of the ant is either in the center of the mound or in the top-left corner, as in the figure:

Given the number of days that have passed since the beginning of the ant's journey and its initial position (center or top-left), determine the minimum number of rooms in the mound where the ant must be searched to ensure it will be found. The number of rooms along the sides of the mound is considered to be much larger than the number of days the ant wanders.

## Input data

The first line of the file `furnica.in` contains a character: $"C"$, if the initial position of the ant is in the center of the mound, or $"S"$, if it is in the top-left corner. The second line contains the number $t$ of days that have passed since the beginning of the walk.

## Output data

The file `furnica.out` will contain, on the first (and only) line, the minimum number of rooms in the mound where the ant must be searched to ensure it will be found (in one of them).

## Constraints and clarifications

$$0 \leq t \leq 30\,000$$

## Examples

`furnica.in`  
```
S 
17 
```
`furnica.out`  
```
90 
```
`furnica.in`  
```
C 
16 
```
`furnica.out`  
```
289 
```