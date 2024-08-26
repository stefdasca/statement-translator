## Task

The sheep are training to jump over fences in people's dreams. They practice their landings because some people have complicated fences in their dreams: some tall, others wide, and some even comparable to the Great Wall of China, and they might even be surrounded by ditches filled with water where crocodiles dwell. The sheep must be very well trained to cope with these dreams. In the world of sheep, they have a whole complex for perfecting jumps, and we are interested in a pyramid. The sheep climb to the top of this pyramid and start descending on one of its faces. Along the descent, they can only remain on that face. The pyramid has $N$ cubes at its base, $N-1$ on the upper level, and so on up to the top where there is a single cube from which the sheep start their training. From this cube, they can jump to the left or to the right cube. However, this pyramid is quite old and over time $P$ cubes have deteriorated and it’s no longer safe to land on them.

Dubota the sheep is preparing to start her training. She stands at the top of the pyramid and analyzes the face on which to descend. Dubota is a quite clever sheep, and although beginner sheep can only jump to the lower level of the pyramid without getting hurt, Dubota can jump between $1$ and $M$ levels. So if she is at location $(i, j)$ then she can jump to the left to $(k, j)$ or to the right $(k, j + k - i)$ where $i < k$ and $k - i \leq M$. Dubota is interested to know in how many ways she can descend to the cubes at the base level. Her problem is that she got confused trying to calculate and asks for your help. Display the number of ways Dubota can descend starting from the top of the hill and ending in each of the locations at the base of the hill. Since the values can be very large, display them modulo $666013$.

## Input data

The input file `derdelus.in` will contain on the first line the values $N$, $M$ and $P$. The following $P$ lines will list the deteriorated cubes in the form of level and index. Levels are numbered from top to bottom starting with $1$ and ending with $N$ and on a level, the cubes are numbered from left to right.

## Output data

In the output file `derdelus.out` you must print $N$ values modulo $666013$ representing the number of ways Dubota can reach each of the cubes at the base level of the pyramid.

## Constraints and clarifications

$2 \leq N \leq 1000$  
$1 \leq M \leq N$  
$0 \leq P \leq \frac{N * (N + 1)}{2}$  
The starting position $(1, 1)$ cannot be broken.

## Example

`derdelus.in`  
```
4 2 2
3 2
2 2
```

`derdelus.out`  
```
3 2 2 1
```

## Explanation

```
* * 
# * 
# * * 
* * * * 
```

For the first box, the three possibilities are: $(1, 1) \to (3, 1) \to (4, 1)$; $(1, 1) \to (2, 1) \to (4, 1)$; $(1, 1) \to (2, 1) \to (3, 1) \to (4, 1)$. 

For the second box: $(1, 1) \to (3, 1) \to (4, 2)$; $(1, 1) \to (2, 1) \to (3, 1) \to (4, 2)$. 

For the third box: $(1, 1) \to (2, 1) \to (4, 3)$; $(1, 1) \to (3, 3) \to (4, 3)$. 

For the fourth box: $(1, 1) \to (3, 3) \to (4, 4)$.