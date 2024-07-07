Gigel, a specialist in computer graphic editing, is facing a problem. He needs to arrange four photographs, available in electronic format, on a presentation page so that the page area is completely "covered" by the four photographs without any overlap. Gigel can modify the initial dimensions of the photographs but without deforming the images. To achieve this, he must keep the initial aspect ratio of the photographs unchanged, even if he has to enlarge or reduce the photographs to completely cover the page area without overlapping them. The order of placing the photographs does not matter; they can be translated anywhere within the page, but rotation operations are not allowed.

# Task

Determine the final dimensions for each photograph, knowing the dimensions of the page as well as the initial dimensions of the photographs.

# Input data

The input file: `foto.in` has the following structure:

* Line $1$ contains the positive integers $l$ and $h$ separated by a space, representing the length and the height of the page, respectively.
* Lines $2 \dots 5$ contain pairs of positive integers $x \\ y$ separated by a space, representing the length and the height of each photograph (on line $i+1$ the photograph $i$).

# Output data

The output file: `foto.out` has the following structure:

* Lines $1 \dots 4$ contain the positive integers $a \\ b$ separated by a space, representing the final dimensions: length, and height for each photograph (on line $i$ for photograph $i$).

# Constraints and clarifications

* $1 \leq l, h, x, y \leq 2 \ 000$;
* If there are multiple solutions, only one will be printed.
* For the chosen input data, there always exists a solution.

# Example

`foto.in`
```
140 140
24 12
4 13
10 14
4 2
```

`foto.out`
```
20 10
40 130
100 140
20 10
