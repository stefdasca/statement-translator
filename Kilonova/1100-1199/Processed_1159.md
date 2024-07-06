In one day, a colleague from the 10th grade came to me and proposed a logic game. He showed me the following figure:

~[logic1.png]

I numbered the segments on it, to make the notion of segment clearer. I have a pencil which is on the paper in the outer area and I have to draw curves on the paper, without lifting the pencil, so that I pass through all the segments (without extremities) exactly once. In the end, I should still be outside. My lines (curves) can intersect.
I started and tried several times, but I couldn't manage it.

~[logic2.png]

Now, when I grew older, I demonstrated that it cannot be done, but I saw that for other figures it can be done. For example, this one:

~[logic3.png]

I figured out why sometimes it works and sometimes it doesn't, but I want to see if you can figure it out. Therefore, I will give you a few figures and for each one you should answer with `YES` or `NO`, whether it is possible to draw a curve of the described type or not.

# Task

Write a program that answers `YES` or `NO` for the figures proposed by me.

# Input data

The input file `logic.in` has the following structure:

* The first line contains the number $T$ of figures
* The next $T$ groups of lines contain the data of the $T$ figures, as follows:
* The first line of the group contains the value of $N$ representing the number of rows and columns in the matrix.
* The next $N$ lines contain $N$ numbers separated by a space (integers between $0$ and $255$ inclusive), representing the elements of the matrix.

This matrix encodes the figure as follows:

We define an area as a continuous part of the matrix that contains the same number and is the maximum area with this property. In other words, two adjacent cells (differing by a single coordinate by one unit) containing the same number are considered to be joined. Thus, within the area, there will be no segments. These areas include the exterior of the matrix as a new area. In the matrix, there can be areas with the same number, but which are not connected and are considered two different areas.

The segments are straight line segments that separate two areas and are maximal in length (i.e., we cannot consider two segments one in the extension of the other, instead of one single segment). For example, the figure defined by:

```
3
1 1 2
1 2 2
1 1 2
```

looks like in the diagram below (I numbered the segments):

~[logic4.png]

It can be seen from the figure that between area $1$ and $2$ there are $5$ segments. Between $1$ and the exterior $3$ segments, and between $2$ and the exterior $3$ segments as well. Note that segment $10$ is composed of $3$ small segments, but we consider it as one single segment, according to the definition.

# Output data

The output file `logic.out` will contain $T$ lines, corresponding to each test. Each line will contain `YES` or `NO` depending on the respective test, whether it is possible to draw a line of the requested type or not.

# Constraints and clarifications

* $1 \leq T \leq 10$;
* $1 \leq N \leq 100$;

# Example

`logic.in`
```
2
2
1 2
3 4
4
1 1 2 2
1 1 2 2
3 4 4 1
3 4 4 1
```

`logic.out`
```
YES
NO
```

## Explanation

The two figures are the first $2$ examples.