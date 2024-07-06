At a carpentry workshop, $n$ stool-type chairs are made, which will be painted in two colors: red and white. The red color is coded by the value $1$, and the white color is coded by the value $0$. A stool is a simple chair, without a backrest, in cubic shape, made by assembling $6$ identical plates ($4$ of the plates will form the side faces of the chair and the other $2$ will form the bases of the chair). In the workshop, to build each chair, $6$ plates are taken, numbered from $1$ to $6$ and one, two, three, or at most four plates are chosen to be painted red while the remaining plates are painted white. The 6 plates of the chair are assembled as follows:

~[taburet.png|align=right]

- plate number $1$ will be the base of the chair;
- plate number $2$ will be the front plate;
- plate number $3$ will be the left plate;
- plate number $4$ will be the back plate;
- plate number $5$ will be the right plate;
- plate number $6$ will be the upper base of the chair

For example, if plates $1$, $2$, and $6$ are chosen and painted red, a chair will be made as in the adjacent figure. When all $n$ stool-type chairs are done, it is observed that, although the way of choosing the red-painted plates was different, many stools look the same. Two stools look the same and are of the same type if there is a way to position each of them such that from any side we look at them, their faces are colored in the same way.

# Task

Knowing the way in which each plate forming a stool was painted, write a program that will determine how many types of stools were made and what is the largest number of stools of the same type.

# Input data

The file `taburet.in` contains on the first line a natural number $n$ representing the number of made stools and on the next $n$ lines $6$ natural numbers (with values of $0$ or $1$) separated by a space, representing the way the plates were painted, in ascending order of the numbers written on them.

# Output data

The file `taburet.out` will contain on the first line a natural number representing how many types of stools were made and on the second line, the largest number of stools of the same type.

# Constraints and clarifications

* $1 \leq n \leq 10 \ 000$
* After assembling any stool, the numbers on the plates are no longer visible.

# Example

`taburet.in`
```
6 
1 0 1 0 0 0 
1 0 1 0 1 0
1 1 0 0 0 1
0 0 1 0 1 0
0 0 0 0 0 1
0 1 1 0 0 0
```

`taburet.out`
```
4
2
```

## Explanation

6 stools were made, and they were painted red as follows:

- for stool $1$: plates $1$ and $3$;
- for stool $2$: plates $1$, $3$, and $5$;
- for stool $3$: plates $1$, $2$, and $6$;
- for stool $4$: plates $3$ and $5$;
- for stool $5$: plate $6$;
- for stool $6$: plates $2$ and $3$;

The first and last stool are of the same type. Also, the second and third stools are of the same type. Four types of stools were made, and there are at most two stools of the same type.