After conquering Tarsonis, Tassadar moved on to purify the planet Zerus. This planet is infested and has $N$ Zerg nests. The nests are numbered from $0$ to $N - 1$ and, every hour, nest $i$ produces $W_i$ zerglings. Initially, there were no zerglings on the planet.

A nest is either autonomous or vital to another nest. If an autonomous nest is destroyed, then the production of zerglings from that nest ceases and all nests vitally supported by it become autonomous. If a nest vitally supported by another nest is destroyed, it regenerates instantly, and the production of zerglings remains uninterrupted.

Tassadar can destroy a nest instantly using the purification laser on the ship "Spear of Adun." Before shooting, the laser must charge for an hour and discharges every time it fires. Initially, the laser is discharged.

Tassadar wants to permanently destroy all nests so that, in the end, there are a minimal number of zerglings.

Help Tassadar purify the planet!

# Input data

The input file `purification.in` contains on the first line the number $N$ of nests. The next line will contain $N$ numbers $W_i$, signifying the number of zerglings produced by nest $i$ in an hour. The next line will contain another $N$ numbers $F_i$, representing the nest that vitally supports nest $i$, or $-1$ if nest $i$ is autonomous.

# Output data

The output file `purification.out` will contain on the first line the minimum number of zerglings remaining on the planet after the permanent destruction of all nests.

# Constraints and clarifications

* $1 \leq N \leq 2\ 000$
* $0 \leq W_i \leq 500$
* It is guaranteed that all nests can be permanently destroyed
* For test cases worth $10$ points, $N \leq 10$
* For test cases worth another $10$ points, $N \leq 20$
* For test cases worth another $10$ points, $N \leq 50$
* For test cases worth another $10$ points, $N \leq 200$

# Example

`purification.in`
```
6
1 5 3 2 1 50
-1 0 0 1 1 -1
```

`purification.out`
```
95
```

## Explanation

The optimal order for destroying the nests is $(5, 0, 1, 2, 3, 4)$. Nest $5$ (autonomous) is destroyed after one hour, so it produces $1 \cdot 50$ zerglings. Nest $0$ (autonomous) is destroyed after two hours, so it produces $2 \cdot 1$ zerglings. Nest $1$ was initially vitally supported by nest $0$, but now it is autonomous and is destroyed after three hours, so it produces $3 \cdot 5$ zerglings. Nest $2$ is destroyed after four hours, so it produces $4 \cdot 3$ zerglings. Nest $3$ is destroyed after five hours, so it produces $5 \cdot 2$ zerglings. Nest $4$ is destroyed after six hours, so it produces $6 \cdot 1$ zerglings. After all nests have been destroyed and zergling production has completely ceased, the number of remaining zerglings is $1 \cdot 50 + 2 \cdot 1 + 3 \cdot 5 + 4 \cdot 3 + 5 \cdot 2 + 6 \cdot 1 = 95$.