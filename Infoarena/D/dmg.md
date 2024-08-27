# Dmg

Max Damage woke up one day on the top of his rocky cliff $\dots$ he looked into the distance and saw that the police had tracked him down. Escaping wouldn't be a problem, as he has a better car anyway, but Max wants to have a bit of fun. He knows that if he drives along a straight line, the police officers (who can be considered as points) will search for the minimal path to his direction of travel, even if it intersects with it long after Max has passed. So, Max wonders if he can make two policemen collide with each other (their paths would have opposite directions and intersect with Damage's path at the same time and place). Obviously, Max is not worried about damaging his car, so his path can also pass through the policemen; obviously, they are hit by Damage, so they no longer need to hit anyone else. Fortunately, Max has a board computer and sent us an email with the positions of the policemen. He is asking for a program to tell him how many ways he can achieve his goal.

## Task

How many trajectories that satisfy Max Damage's requirements exist and what are these?

## Input data

The first line of the file `dmg.in` contains an integer $N$ representing the number of policemen.
The following $N$ lines contain two real numbers with 8 decimal places, $X_i$, $Y_i$ representing the position of a policeman.

## Output data

The output file `dmg.out` will contain the number of possible trajectories for Max's car.
The following lines each contain three real numbers with 8 decimal places, $A$, $B$, and $C$, describing a trajectory of the equation $A \cdot X + B \cdot Y + C = 0$, which meets the conditions desired by Max.

## Constraints and clarifications

$2 \leq N \leq 1500$

$|X_i| \leq 1000,$

$|Y_i| \leq 1000$

Max Damage is not very "scientific" and will check if the line meets his conditions with a precision of $0.01$

For $25\%$ of the tests $N \leq 100$

What happens if two policemen are at the same point?

The policemen move at the same constant speed

## Example

`dmg.in`
```
2 
0 0 
10 0
```

`dmg.out`
```
2 
-10.00000000 -0.00000000 50.00000000 
0.00000000 -5.00000000 0.00000000
```

## Explanations

Max Damage can travel perpendicularly to the line $O_x$, and the two policemen will collide at position $(0,5)$, or he can travel along the line $O_x$ hitting the cars of the two policemen. Any other line does not meet Max's requirements.