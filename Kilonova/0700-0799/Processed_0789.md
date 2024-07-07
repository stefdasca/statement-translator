
Jean-Luc Picard, the captain of the spaceship Enterprise, noticed that $n$ Borg ships have appeared near his ship. The distances between them and the Enterprise are $d_1, d_2, \dots, d_n$. The Borg ships do not move relative to each other or to the Enterprise. The positions in space of the $n$ Borg ships and the position of the Enterprise are distinct pairwise (no two ships occupy the same point in three-dimensional space).

At one point, all $n$ Borg ships simultaneously launch an attack, each launching a projectile in the direction of the Enterprise. The walls of the Enterprise are resistant to such attacks, but the captain decides to destroy as many projectiles as possible using the laser weapon. The $n$ projectiles travel at constant speeds $v_1, v_2, \dots, v_n$ expressed in meters per second. Captain Jean-Luc Picard has a laser weapon at his disposal with which he can destroy one projectile at a time. The weapon can be oriented instantly towards any Borg ship. The laser can perform any number of shots starting from the moment the attack is initiated, but after each shot it needs $t$ seconds to recharge. During this time, no other shot can be fired. Orienting the laser towards a specific projectile does not consume time. Also, the time between firing and destroying the targeted projectile is zero. The captain never misses his target, and projectiles that manage to hit the Enterprise do not prevent Captain Picard from continuing to shoot at other moving projectiles.

# Task

Determine the maximum number of projectiles that can be destroyed with the laser weapon.

# Input data

The input file `startrek.in` contains on the first line the natural numbers $n$ and $t$, representing the number of Borg ships, respectively the time required to recharge the laser weapon with energy. The second line contains $n$ natural numbers $d_1 \ d_2 \ \dots \ d_n$ representing the distances of the Borg ships from the Enterprise. The third line contains $n$ natural numbers $v_1, v_2, \dots, v_n$ representing the speeds of the $n$ projectiles.

# Output data

The output file `startrek.out` will contain a natural number $p$, representing the maximum number of destroyed projectiles.

# Constraints and clarifications

* $2 \leq n \leq 4 \ 000$;
* $1 \leq d_1, d_2, \dots, d_n \leq 10 \ 000$;
* $1 \leq v_1, v_2, \dots, v_n$;
* $t \leq 1 \ 000$;
* If the moment a projectile is supposed to hit the ship coincides with the moment the laser weapon is fired at it, it is considered that the Enterprise destroys that projectile.
* If the speed of a projectile is $v$, then in the time $t$, it travels a distance $d = v \cdot t$

# Example 1

`startrek.in`
```
3 4
4 3 6
2 1 1
```

`startrek.out`
```
2
```

## Explanation

Projectile 1 is destroyed, then projectile 2 hits the Enterprise, then projectile 3 is destroyed.

# Example 2

`startrek.in`
```
4 2
2 5 8 5
1 3 2 5
```

`startrek.out`
```
3
```

## Explanation

Projectile 4 is destroyed, then projectile 2 hits the Enterprise, then projectile 1 is destroyed, and then projectile 3 is destroyed.
