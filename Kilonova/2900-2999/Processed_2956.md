```markdown
RAU-Gigel is passionate about graphics, so he thinks of giving you a gift for the 1st of June: a game with images. He creates a binary bitmap image of dimensions $N \times N$ pixels in a graphic editor. A binary bitmap image is a matrix of pixels, each pixel being a bit. Let's consider that the value $0$ (unset) means white and the value $1$ (set) means black. Then RAU-Gigel divides the image into four equal square images with side $N / 2$ which are denoted from 1 to 4 (1 is the image in the top-right corner, 2 is the image in the bottom-right corner, 3 bottom-left and 4 top-left). He repeats the procedure for each of the 4 obtained images, always halving the side and denoting the directions from 1 to 4, until he reaches one-pixel-sized images.

For simplicity, let's assume that $N$ is a power of $2$, let's say $K$. So, after $K$ successive image divisions, any pixel can be identified by a unique sequence consisting of the digits 1, 2, 3, and 4, of length $K$.

For example, if $N = 4$, then $K = 2$. We will have $2$ successive divisions:

~[p1.png|width=50em|align=center]

Initially, the image is completely white.

Now the game begins. RAU-Gigel thinks of 2 types of operations:
- Operation `1 x` changes the state of the pixel identified by the sequence $x$, as described above. If the pixel $x$ is not set, it sets it. If the pixel $x$ is already set, then it resets it;
- Operation `2 x`, where $x$ has the same meaning as above, is a query: if $x$ is set, respond with $0$. If $x$ is not set, determine the size of the largest completely white image, among those created by RAU-Gigel, that contains pixel $x$. The size is given by the number of contained pixels.

# Task
Given $N$ with the above significance and $M$, representing the number of operations and the $M$ operations of type 1 and 2, respond to the operations of type 2.

# Input data
The input file `pixeli.in` contains on the first line the natural numbers $N$ and $M$ separated by a space. The following $M$ lines contain a digit either $1$ or $2$ and a string, of the form `operation_type x`, representing the type of operation and the sequence $x$.

# Output data
The output file `pixeli.out` will contain the responses for the operations of type 2, each one on a new line.

# Constraints and clarifications
- $2 \le N \le 2\ 000\ 000\ 000$
- $1 \le M \le 10\ 000$
- In all tests, $N$ is a power of $2$.
- All sequences $x$ are correctly defined.
- For tests worth 30 points, $N \le 1\ 000$ and $M \le 50$.

# Example 1
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
~[p2.png|width=15em]

After the first 2 operations of type 1, the image will contain:
~[p3.png|width=15em]

The next 4 queries will refer, in order, to the pixels marked with `a`, `b`, `c`, `d` (the image below). Since `a` was set, the response is $0$. The largest white image, created by RAU-Gigel, that contains `b`, is the bottom-left corner with $4$ pixels (bolded). The same for `c`. In the case of pixel `d`, the response is $1$ (itself).
~[p4.png|width=15em]

Next is an operation of type 1 that resets the pixel marked with `a` (sequence $22$). The next 2 queries for `a` and `d` generate responses $4$ and $4$ respectively.

Finally, pixel `e` is reset too, and the last query, for `c`, will determine the response $16$, as the whole image is now completely white.

# Example 2
`pixeli.in`
```
8 9
1 111
1 222
2 222
2 333
2 444
2 242
1 222
2 222
2 242
```
`pixeli.out`
```
0
16
16
4
16
16
```
```