# Tribute

The Great Galactic Empire rules a number of $N$ solar systems that owe tribute and have a varied wealth of resources. Each solar system owes a certain percentage of its income to the Emperor in the form of a tribute (taxes) for the services provided, especially for facilitating trade. The Emperor would like to collect as much tribute as possible from the solar systems, but he faces the following problem. According to the treaties signed with the solar systems, there are a number of $M$ trade unions consisting of solar systems, and each union has an agreed maximum amount of tribute that all systems in the union must collectively pay to the Emperor. If a country is part of many trade unions, it can be forced to contribute to the tributes paid by any of these, within the maximum tribute amount owed by that country. Countries that are not part of any trade union are exempt from tribute. Knowing the tribute values calculated for each country based on their income, as well as the maximum tribute values established by the treaties with each union, help the Emperor decide what is the maximum value of the tribute he will receive from all the solar systems. Obviously, no trade union will pay an amount greater than that established by the treaty with the Galactic Empire, but the Emperor can decide the contribution of each solar system in the respective union to the union's total sum.

## Input data

The input data is read from the file `tribut.in`. The first line contains the number of tests, $T$. Then, for each test, the following information is read: The first line of a test contains two integers separated by space: $N$ - the number of solar systems and $M$ - the number of trade unions. The next line contains $N$ integers separated by space, representing the maximum tribute that can be paid by each solar system based on their income ($tribut[i], 1 \leq i \leq N$). After that, there are $M$ lines for each trade union. Each line begins with two integers: the first contains the number of solar systems that are part of the union - $P$, and the second the maximum tribute paid by all the countries in the union according to the treaty signed with the Galactic Empire ($tribut[j], 1 \leq j \leq M$). Following are the $P$ solar systems in the current union indexed between 1 $\dots$ N.

## Output data

The output file is `tribut.out` which will contain a line for each test. Each line must contain a single number, which is the maximum value of the tribute that will be received from all the solar systems that are part of a trade union.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N, M \leq 100$

$0 \leq tribut[i], tribut[j] \leq 10000$

## Example

`tribut.in` `tribut.out` 

```plaintext
2 
4 4 
2 1 1 1 
2 2 1 2 
2 1 3 4 
2 2 1 3 
2 0 2 4 
2 2 
1 3 
2 0 
4 9 6 5 
0 2 0 2 0 2 0 3 3 4 1 2 3 
3 0 
4 5 6 3 0 
7 8 9 3 6 1 4 7 
3 0 
2 5 8 3 0 
3 6 9 5 9 
```

## Explanation

In the first case, we have 4 solar systems and 4 trade unions, and the maximum tribute that can be obtained by the Emperor is 5. The first union contributes 2: system 1 with 1 and system 2 with 1. The second union contributes 1 paid by system 4. The third union contributes 2: system 1 with 1 and system 3 with 1. The fourth union does not contribute anything. In the second case, there are only 2 trade unions that can contribute with tribute, the others have signed treaties that protect them from tribute. One possible solution to distribute the tribute among unions is: the first union can contribute 3, and the fourth 6.
