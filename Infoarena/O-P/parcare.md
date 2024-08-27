# Parking

To make money, Cezar got a job as a parking lot manager during the summer. The parking lot is a square made of concrete blocks, also square, with a side length of one meter. The parking lot has only one exit on the northern side, while the rest is surrounded by walls that cars cannot pass through. The cars in the parking lot are rectangles with a width of $1m$ and a length greater than or equal to $2m$. They are oriented north-south or east-west. When he got the job, Cezar didn't think this job would cause him problems, but today he is in a delicate situation: a customer asked him to remove his car from the parking lot. Cezar has the keys to all the cars, but he is not a very good driver: he cannot take turns, he can only go forward and backward. He tried for an hour to get the car out of the parking lot but did not succeed and thought to ask for your help. He made a map of the parking lot: he represented asphalt portions with '.', the parking lot walls with '#', and the cars with consecutive uppercase letters of the Latin alphabet. The car that needs to be removed from the parking lot is represented by 'A'.

## Task

He asks you to write a program to get the car out of the parking lot in less than $100$ moves. He considers a move as moving a car, in a certain direction, with an integer number of meters.

## Input data

The first line of the file `parcare.in` contains an integer $N$ representing the size of the map. The next $N$ lines contain $N$ characters each representing the map encoding.

## Output data

The first line of the file `parcare.out` will contain the number of moves $M$ by which the problem was solved. The next $M$ lines will contain $3$ characters representing a move. The first represents the letter associated with the car to be moved, the second the direction in which it will be moved ($N$ - north, $S$ - south, $E$ - east, $W$ - west), and the third the number of blocks by which it will be moved. Instead of the move by which the car `A` leaves the parking lot, `Exit` will be printed.

## Constraints

$7 \leq N \leq 9$

There are at most $10$ cars in the parking lot.

The second line of the input file will contain a character '.' (the exit).

If a car has a certain letter of the alphabet then there is exactly one car assigned to each letter smaller than that respective letter.

No two cars have the same letter.

It is impossible for another car to leave the parking lot before the car 'A'.

The existence of a solution is guaranteed.

Any solution with fewer than $100$ moves will receive the maximum score.

## Examples

`parcare.in`:

```
8
###.####
#..BBBC#
#..A..C#
#..A..C#
#.....C#
#.....C#
#......#
########
```

`parcare.out`:

```
3
CS1
BE1
Exit
```

`parcare.in`:

```
8
###.####
#HHH.G.#
#....GF#
#.EEE.F#
#..A..F#
#B.A...#
#BCCCDD#
########
```

`parcare.out`:

```
8
BN1
CV1
DV1
FS2
GS3
EE2
HE3
Exit
```