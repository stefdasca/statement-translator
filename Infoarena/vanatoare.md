# Hunting

On a well-known private hunting domain, the wild boar hunt has begun. The domain is linear and has a length of $T$ units. Thus, it can be considered as a segment on the $Ox$ axis of the coordinate system, between the coordinates $0$ and $T$. There are $N$ wild boars that need to be hunted. Each wild boar is characterized by a pair of natural numbers $(c_i, v_i)$, with $0 \leq c_i < v_i$, which has the following meaning: at moment $\ 0$ (which represents the beginning of the hunt) wild boar $i$ is located at coordinate $c_i$ on the axis and runs at a constant speed of $v_i$ meters per second. This means that at second $p$ ($p \geq 0$) the wild boar will be at coordinate $c_i + v_i * p$. Although the participants in the hunt are very wealthy, they are mindful of their resources and want to shoot the wild boars with the minimum number of hunters. A hunter positions himself at a natural coordinate within the domain (so a hunter can position himself at any coordinate between $0$ and $T$ inclusive) and will shoot all the wild boars that pass by him at integer moments of time. Specify the minimum number of hunters required to shoot all the wild boars, as well as the positions where they need to position themselves.

## Input data

The input file `vanatoare.in` contains on the first line the natural numbers $N$ and $T$, separated by a space. Each of the next $N$ lines contains the description of a wild boar. Thus, line $i+1$ will contain the pair of natural numbers $(c_i, v_i)$, with the significance from the description.

## Output data

The output file `vanatoare.out` will contain on the first line the minimum number $MIN$ of hunters needed to shoot the $N$ wild boars. The second line contains exactly $MIN$ natural numbers between $0$ and $T$, indicating the positions of the hunters.

## Constraints

$1 \leq N \leq 16$

$1 \leq T \leq 2\ 000\ 000\ 000$

For any pair in the input file, the relationship is met: 

$0 \leq c_i < v_i \leq 200\ 000\ 000$

It is considered that a hunter can shoot multiple wild boars simultaneously.

If there are multiple optimal solutions, any of them can be displayed.

## Example

`vanatoare.in`
```
3 10
3 5
1 3
2 3
```

`vanatoare.out`
```
2
7 8
```

## Explanation

The first hunter will shoot the second wild boar in the second second. The second hunter will shoot the first wild boar in the first second, and the third wild boar in the second second. Thus, all the wild boars are shot. The $3$ wild boars cannot be shot by a single hunter, so $2$ hunters represent the optimal solution.