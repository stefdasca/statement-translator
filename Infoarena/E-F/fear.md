## Fear

The tests for this problem are not well-constructed enough to correctly distinguish inefficient or incorrect solutions. Enter here if you want to help improve the quality of the tests for this problem! Although Max Damage has long since left the city, his reputation remains untarnished, and the residents are still afraid of his possible return. Of course, no one is more afraid than the chief of police. Therefore, Damage thought of testing how deeply he remains in the chief's conscience. He has a map of the city, which consists of $N$ intersections and $M$ bidirectional streets, allowing movement from one intersection to any other. Initially, our hero is at the city gate (intersection number $1$) and wants to send the rumor of his return to the chief of police's house (intersection number $N$). Unfortunately, on a street, fear does not spread on its own, but cannot exceed a certain real value (calculated for that street based on the number of residents, average age, life expectancy, etc.). Even though there are bidirectional streets, fear cannot spread in both directions simultaneously. Furthermore, the fear that "exits" an intersection can spread across each of the incident streets, but the product of the fear values on each street does not exceed the fear value in the intersection. Also, the fear value in an intersection is numerically equal to the product of the fear values entering it from each incident street. Knowing this, help Max Damage determine the maximum value of fear that can reach intersection $N$.

## Task

## Input data

The first line in the `fear.in` file contains $N$ and $M$. The following $M$ lines contain 3 numbers each: $A$, $B$, and $C$, representing that on a street between cities $A$ and $B$, fear can spread with a maximum value of $C$.

## Output data

The result is printed in `fear.out` on a single line with 4 decimals.

## Constraints

$1 \leq N \leq 200$  
$1 \leq M \leq 19\,900$  
$1 \leq C \leq 200.256$  
$1 \leq maximum\ fear\ factor\ in\ an\ intersection \leq 2\,147\,483\,647$  
Fear can no longer spread from intersection $N$ (to keep things simple)  

## Example

`fear.in`  
3  
3  
1 2 5.3  
1 3 7  
2 3 4.5  

`fear.out`  
31.5  

`fear.in`  
4  
4  
1 4 10  
2 4 5  
2 3 5  
3 4 5  

`fear.out`  
10  

## Explanation

For the first example, from $1$ to $3$, fear is transmitted with the value $7$, from $1$ to $2$ with the value $5.3$, and from $2$ to $3$ with the value $4.5$, $7*4.5 = 31.5$. For the second example, although if Damage sends fear through the cycle 4 3 2 4, we would get a fear factor greater than $10$, but we must stop at $4$.