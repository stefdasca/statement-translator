**Task**  
Ion has learned about Pascal's triangle in his mathematics class. Each row of this triangle has its first and last element equal to 1. An element in the triangle is calculated as the sum of the two elements directly above it. The rows are numbered starting from 0, so for example, row 2 contains: 1 2 1. It is a well-known fact that the value of element \( j \) (with indexing of the elements starting from 0) on line \( i \) can also be calculated using the formula:  
\[
\frac{i!}{(i-j)! \cdot j!}
\]  
(Where \( i! \) denotes the product \( 1 \cdot 2 \cdot \dots \cdot i \)).

**Task**  
Help Ion calculate how many numbers in row \( R \) are divisible by \( D \).

**Input data**  
The input file `pascal.in` contains on the first line the numbers \( R \) and \( D \).

**Output data**  
The output file `pascal.out` will contain on the first line the required number.

**Constraints and clarifications**  
- \( 0 \leq R \leq 5\ 000\ 000 \)
- \( 2 \leq D \leq 6 \)  
Observation: \( 0 \neq 1 \)