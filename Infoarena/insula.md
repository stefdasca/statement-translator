# The Island

One day, while visiting her grandmother, Adriana was searching for old books in the library as usual. Suddenly, she stumbled upon a book with the initials BA inscribed on it. Curious, Adriana opened the book and began to read. She discovered that in a very distant land, where everything is enchanted (including the pearls), some trees have a peculiar property: by simply uttering a magic formula, all the trees change the radius of their trunks. Upon further investigation, Adriana found that the land is, in fact, an island shaped like a circle. Moreover, she learned that the trees on the island are planted only at points with integer coordinates and only inside and on the edges of the island. On the last page, Adriana found a sketch of the country's map drawn in an orthogonal axis system. Convinced that something was missing, she drew herself at the center of the island and brought the pencil to her mouth, thinking: "How nice it would be to have such a place for myself. If I stood in the middle and uttered the magic formula a number of times, I would become invisible to any observer on the edge of the island". And while thinking, Adriana, the clever girl, managed to determine the minimum radius needed for the tree trunks so that she would become invisible. Can you do this as well?

## Task

Given the radius of the island, find the minimum radius $G$ that the trunks should have so that the center (and implicitly Adriana) cannot be seen from any point on the edge of the island.

## Input data

The first line of the input file `insula.in` contains the integer $T$, the number of tests. The following $T$ lines each contain a number $R_i$, the radius of the island.

## Output data

In the output file `insula.out` you will print $T$ lines, each containing the minimum radius $G$ for the respective test, with 3 precise decimals.

## Constraints and clarifications

$1 \leq T \leq 10$  

$1 \leq R_i \leq 100$  

After uttering the magic formula, the radius of each tree will increase by the same unit of length.

Initially, the trees are point-like (their radius tends to $0$).

The minimum radius $G$ implies that for any other radius $G' (G' < G)$, there is at least one point on the edge of the island from which Adriana can be seen if you look.

Being a small girl, Adriana neglects the crown of the trees, she is only interested in their trunks.

The center of the island will always be a point with integer coordinates where only Adriana is located.

At least one tree will be planted inside the island.

To avoid approximations (e.g., $0.09967$ being written as $0.100$), the result will be displayed according to the following model: write $($floor$(G\ast 1000)/1000.0)$.

Finding the book was not the work of fate, just the work of Arhirel the Blaur, who is still on the lookout.

## Example

`insula.in` 

$2 1 2$ 

`insula.out` 

$0.707 0.447$