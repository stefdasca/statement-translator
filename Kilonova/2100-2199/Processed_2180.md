```markdown
There was once a man so poor that his only possession was a number $n$ of equilateral triangles with side length $1$. These triangles had the property that they could be stuck together along one side, thus forming various flat geometric shapes. The emperor announced throughout the country that he would give half of his empire and his daughter’s hand in marriage to anyone who could form the most beautiful convex polygon using exactly $n$ equilateral triangles with side length $1$. Our man noticed that there are many ways convex polygons can be formed. However, he is not sure if he has correctly calculated the number of convex polygons, incongruent two by two, that can be constructed with his triangles. Now he fears that he has forgotten to count the one desired by the emperor and that he will thus lose the opportunity to escape poverty and especially to marry the beautiful princess.

# Task
Determine the number of convex polygons, incongruent two by two, that can be perfectly covered using a given number of equilateral triangles with side length $1$.

# Input data

The input file `equicover.in` contains on the first line the natural number $n$.

# Output data

The output file `equicover.out` will contain on the first line a natural number representing the number of convex polygons, incongruent two by two, that can be perfectly covered using $n$ equilateral triangles with side length $1$.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000 \ 000$;

# Example

`equicover.in`
```
16
```

`equicover.out`
```
5
```

## Explanation

The $5$ polygons are:

~[equicover.png]

The following polygons are congruent to one of the $5$:

~[equicover2.png]
```