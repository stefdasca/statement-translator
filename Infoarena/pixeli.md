## Task

RAU-Gigel is passionate about graphics, so he's thinking about an image game. He creates a binary bitmap image of size $N \times N$ pixels in a graphic editor. A binary bitmap image is a pixel matrix, with each pixel being a bit. Let's consider that the value 0 (unset) means white and the value 1 (set) means black (in reality, it's exactly the opposite!). Then, RAU-Gigel divides the image into four equal square images of side $N / 2$ which he labels from 1 to 4 (1 is the top-right corner image, 2 is the bottom-right one, 3 is the bottom-left one, and 4 is the top-left one). He repeats this process for each of the 4 obtained images, and so on, always halving the side and labeling the sections from 1 to 4 until he reaches images of one pixel in size. For simplicity, let's assume $N$ is a power of 2, say $2^K$. Therefore, after $K$ successive image divisions, any pixel can be identified by a unique string formed from the digits 1, 2, 3, and 4 of length $K$. For example, if $N = 4$, then $K = 2$. The initial image has 16 pixels. We will have 2 successive divisions:

After the first division, we get 4 reduced-to-half images (each with 4 pixels):
4 1
3 2

After the second division, we get 16 one-pixel images:
44 41   14 11
43 42   13 12
34 31   24 21
33 32   23 22

Initially, the image is completely white. Now the game begins. RAU-Gigel is thinking about 2 types of operations:
Operation 1 $x$ changes the state of the pixel identified by the string $x$, as described above. If the pixel $x$ is not set, it sets it. If the pixel $x$ is already set, it resets it.
Operation 2 $x$, where $x$ has the same meaning as above, is a query: if $x$ is set, respond with 0. If $x$ is not set, determine the size of the largest completely white image, among those created by RAU-Gigel, which contains the pixel $x$. The size is given by the number of pixels it contains. Given $N$ as described above and $M$, representing the number of operations and the $M$ operations of types 1 and 2, respond to the type 2 operations.

## Input data

The input file `pixeli.in` contains on the first line the natural numbers $N$ and $M$ separated by a space. The next $M$ lines each contain a digit 1 or 2 and a string, in the form type_operation $x$, representing the type of operation and the string $x$.

## Output data

The output file `pixeli.out` will contain the responses to the type 2 operations, one per line.

## Constraints and clarifications

$2 \leq N \leq 2000000000$

1 $\leq M \leq$ 10000

In all tests, $N$ is a power of 2

All strings $x$ are correctly defined

For tests worth 30 points $N \leq$ 1000 and $M \leq$ 50

## Example

`pixeli.in`
```
4 11
1 11
1 22
2 22
2 33
2 44
2 24
1 22
2 22
2 24
1 11
2 44
```

`pixeli.out`
```
0
4
4
1
4
4
16
```

## Explanation

Initially, the image is white:
```
0 0   0 0
0 0   0 0
0 0   0 0
0 0   0 0
```
After the first 2 type 1 operations, the image will contain:
```
0 0   0 1
0 0   0 0
0 0   0 0
0 0   0 1
```
The next 4 queries will refer, in order, to the pixels marked with $a$, $b$, $c$, $d$ (the image below). As $a$ was set, the response is 0. The largest white image, created by RAU-Gigel, containing $b$ is the bottom-left corner with 4 pixels. The same applies for $c$. In the case of pixel $d$, the response is 1 (itself).
```
c 0   0 e
0 0   0 0
0 0   d 0
b 0   0 a
```
Next is a type 1 operation that resets the pixel marked with $a$ (string 22). The next 2 queries for $a$ and $d$ generate the responses 4 and 4, respectively. Finally, the pixel $e$ is reset, and the last query, for $c$, will determine the response 16, with the entire image now being completely white.