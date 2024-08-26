## Task

At the freshmen ball, a student has captured the hearts of two classmates and cannot decide which one is the one. Thus, she continuously goes from one to the other. There is a distance $D$ between the two boys, which the girl traverses each time in a straight line, and when she reaches one of the boys, without lingering for a moment, she immediately sets off in the opposite direction to the other. The two boys each follow her to try to win her over, but unfortunately, they move much more slowly than she does. Nevertheless, at some point, the two will inevitably meet, and beyond that, we do not know what happens because the end of the world is triggered. Even though she has negligible dimensions, even in these final moments before the apocalypse, the student is interested in knowing the total distance she has traveled by continuously walking between the two classmates, to know how many calories she has consumed.

## Input data

The input file `balulbobocilor.in` contains:

- The first line contains a natural number $D$ representing the distance between the two boys.
- The next two lines each contain 3 natural numbers $V$, $H$, $G$, representing the speed at which each boy moves, as well as their height and weight.
- The last line contains a single number, the speed at which the girl moves.

## Output data

The output file `balulbobocilor.out` will contain:

- A single number, the total distance traveled by the girl until the end of the world. The result will be displayed with exactly 6 decimal places.

## Constraints and clarifications

- The student has negligible dimensions, meaning physically we can consider her point-like.
- The student will always be between the two boys, without deviating from the path that guarantees the minimum distance.
- Nothing prevents the three from moving constantly at the specified speeds.
- $0 < D < 1000000$
- $0 < G < 1000$
- $0 < H < 1000$
- $0 < \text{boys' speed} < \text{girl's speed} < 1000000$
- Distance and heights are expressed in meters.
- Speeds are expressed in $m/s$.
- Weights are expressed in Newtons.

## Example

`balulbobocilor.in`
```
4
1 1 2
1 1 2
2
```

`balulbobocilor.out`
```
4.000000
```