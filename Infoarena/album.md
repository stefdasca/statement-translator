Album

## Task

In a high school, there are $N$ classes, and each class has exactly $K$ students. On the occasion of successfully passing the Baccalaureate exam (not without emotions), the school administration decided to take a series of photos with the protagonists of this wonderful generation. In a photo, the classes stand in a line one behind the other facing the camera. Since the students do not all have the same height, in some photos, some of them will be hidden behind taller ones, thus ruining the photo for the class they belong to. You are given an $N \times K$ matrix containing the heights of the students. Determine the minimum number of photos needed so that each class (out of the $N$) has at least one photo in which all its students are visible simultaneously. In any photo, the students of any class can be permuted among themselves in any order.

## Input data

The input file `album.in` contains on the first line two natural numbers $N$ and $K$, separated by a space, representing the number of classes in the high school and the number of students in each class (each class has exactly the same number $K$ of students). On the next $N$ lines, there are $K$ natural numbers separated by spaces, representing the heights of the students in that class.

## Output data

The output file `album.out` will contain on the first line a single natural number, representing the minimum number of photos that need to be taken so that each class has at least one photo in which all its students are visible simultaneously.

## Constraints and clarifications

$1 \leq N \leq 1000$  
$1 \leq K \leq 50$  
$1 \leq$ height of a student $\leq 1\ 000\ 000\ 000$  

A student is not visible if there is at least one other student in front of them with a height greater than or equal to theirs. Within a class, the students can be permuted in any order (they do not have to sit in the order given in the input file). Students can only be permuted if they are in the same class. On a row, there is only one class (students from 2 different classes cannot be in the same row).

## Example

`album.in` `album.out`  
```
3 2
1 2
3 4
5 2
2
```

## Explanation

A possible arrangement is: in photo 1, class 1 is in the first row, class 2 is in the second row, and class 3 is in the third row. All students from classes 1 and 2 will be visible simultaneously. In photo 2, class 3 will be placed in the first row, making its students visible and fulfilling all conditions. An illustrative image of this arrangement is (the photographer is in front of the first row): 
```
3. 2 5 | 2. 4 3
2. 3 4 | 1. 1 2
1. 1 2 | 3. 5 2
```
In the first photo, the classes line up in the order (1, 2, 3), in the second photo they line up in the order (3, 1, 2). It is observed that students from a class do not necessarily keep the order from the input file.