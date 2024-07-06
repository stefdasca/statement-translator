Fermierul Ion deține un teren de formă pătrată, împărțit în $N \times N$ pătrate de latură unitate, pe care cultivă cartofi. Pentru recoltarea cartofilor fermierul folosește un robot special proiectat în acest scop. Robotul pornește din pătratul din stânga sus, de coordonate $(1,1)$ și trebuie să ajungă în pătratul din dreapta jos, de coordonate $(N,N)$. Traseul robotului este programat prin memorarea unor comenzi pe o cartelă magnetică. Fiecare comandă specifică direcția de deplasare (sud sau est) și numărul de pătrate pe care le parcurge în direcția respectivă. Robotul strânge recolta doar din pătratele în care se oprește între două comenzi.

Din păcate, cartela pe care se află programul s-a deteriorat și unitatea de citire a robotului nu mai poate distinge direcția de deplasare, ci numai numărul de pași pe care trebuie să-i facă robotul la fiecare comandă. Fermierul Ion trebuie să introducă manual, pentru fiecare comandă, direcția de deplasare.

# Task

Write a program that determines the maximum amount of potatoes that the robot can harvest, assuming that Ion manually specifies the direction for each command. The program should also determine the path that results in the maximum harvest.

# Input data

The input file `sudest.in` contains the following structure:
* The first line contains the natural number $N$, representing the size of the land plot.
* The next $N$ lines contain $N$ natural numbers, separated by spaces, representing the amount of potatoes in each unit square.
* The line $N+2$ contains a natural number $K$ representing the number of commands on the magnetic card.
* The line $N+3$ contains $K$ natural numbers $C_1, \dots, C_K$, separated by spaces, representing the number of steps the robot must take per command.

# Output data

The output file `sudest.out` will contain the maximum amount of potatoes harvested by the robot on the first line. The following $K+1$ lines will contain, in order, the coordinates of the unit squares that make up the path for the maximum harvest, with one unit square per line. Coordinates on the same line will be separated by a space. The first square of the path will have the coordinates `1 1`, and the last will have the coordinates `N N`. If there are multiple paths obtaining the maximum harvested amount, one of them will be displayed.

# Constraints and clarifications

* $5 \leq N \leq 100$;
* $2 \leq K \leq 2 \cdot N - 2$;
* $1 \leq C_1, \dots, C_K \leq 10$;
* The amount of potatoes in a unit square is a natural number between $0$ and $100$;
* For each set of input data, it is guaranteed that there is at least one path available;
* It is considered that the robot collects potatoes from both the starting square $(1,1)$ and the ending square $(N,N)$;
* $50\%$ of the score will be given for correctly determining the maximum harvested amount; $100\%$ will be given for both the correct maximum amount harvested and the correct path.

# Example

`sudest.in`
```
6
1 2 1 0 4 1
1 3 3 5 1 1
2 2 1 2 1 10
4 5 3 9 2 6
1 1 3 2 0 1
10 2 4 6 5 10
5
2 2 1 4 1
```

`sudest.out`
```
29
1 1
3 1
5 1
6 1
6 5
6 6
```

## Explanation

Another possible path is:
```
1 1
1 3
1 5
2 5
6 5
6 6
```
but its cost is $1+1+4+1+5+10=22$.