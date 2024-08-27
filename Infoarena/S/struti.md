## Ostriches

Patratel has dropped out of school and, since he found out they are very profitable, he has started a business with ostriches. To launch his business, he first needs to buy land in the region. The region is rectangular and has dimensions of $M$ km $ \times N$ km, being divided into $1 \times 1$ km zones. Each zone has a known altitude, specified on the map in meters above sea level. Thus, all altitudes are non-negative integers. The land that Patratel wants to buy in this region must also be rectangular and have sides parallel to the region's sides. Additionally, the land cannot be chosen randomly. Since he has studied the behavior of ostriches, he realized that they are quite picky animals. The difference in altitude of a land is defined as the difference between the maximum altitude and the minimum altitude of $1 \text{ km }^2$ zones included in the land. For the ostriches to develop optimally, the difference in altitude of the chosen land must be as small as possible. Patratel receives $P$ offers that he needs to analyze. An offer consists of a pair of natural numbers $(DX \ DY)$, meaning that Patratel can choose land anywhere in the region with sides of dimensions $DX$ and $DY$ (not necessarily in this order). For each offer, Patratel would like to know the minimum altitude difference of a land with the sides specified in the offer.

## Task

Determine the minimum altitude difference for each offer.

## Input data

The first line of the file `struti.in` contains $M$, $N$, and $P$, the dimensions of the region and the number of offers, separated by a space. Each of the following $M$ lines contains $N$ non-negative natural numbers, specifying the altitude of the respective zone. The next $P$ lines describe an offer, consisting of two natural numbers $DX$ and $DY$, with the meanings described in the task.

## Output data

The file `struti.out` contains $P$ lines, with line $i$ containing $MIN$ and $NR$, the minimum altitude difference for the $i$-th offer and the number of possible lands with this minimum difference.

## Constraints and clarifications

$3 \leq M, N \leq 1 \ 000 $

$P \leq 10$

$1 < DX, DY \leq \min(M, N)$

Each selected land must be completely included in the region

All altitudes are given in meters and do not exceed $8 \ 000$

Points for a test are awarded only if the output file is entirely correct

## Example

`struti.in`
```
4 4 2
1 4 3 2
5 4 8 9
3 8 5 8
2 0 6 4
2 2
3 2
```

`struti.out`
```
5 4
4 4
```

## Explanations

The four lands that can be selected for the first offer are highlighted:
$$
\begin{array}{cccc}
\mathbf{1} & \mathbf{4} & 3 & 2 \\
\mathbf{5} & \mathbf{4} & 8 & 9 \\
3 & 8 & 5 & 8 \\
2 & 0 & 6 & 4 \\
\end{array}
\,
\begin{array}{cccc}
\mathbf{1} & 4 & \mathbf{3} & 2 \\
\mathbf{5} & 4 & \mathbf{8} & 9 \\
3 & 8 & 5 & 8 \\
2 & 0 & 6 & 4 \\
\end{array}
\,
\begin{array}{cccc}
1 & \mathbf{4} & 3 & 2 \\
5 & \mathbf{4} & 8 & 9 \\
\mathbf{3} & \mathbf{8} & 5 & 8 \\
2 & 0 & 6 & 4 \\
\end{array}
\,
\begin{array}{cccc}
1 & 4 & 3 & 2 \\
5 & 4 & 8 & 9 \\
3 & 8 & 5 & 8 \\
\mathbf{2} & \mathbf{0} & 6 & 4 \\
\end{array}
$$