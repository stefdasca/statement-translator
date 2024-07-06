Un parc de formă dreptunghiulară este format din zone pietonale și piste de biciclete. Reprezentând harta parcului într-un sistem cartezian, cu coordonata colțului stânga-jos `(0,0)`, pistele de biciclete sunt reprezentate prin dungi orizontale sau verticale colorate cu gri, iar zonele pietonale au culoarea albă, ca în figura din dreapta.

Vizitatorii parcului se pot plimba liber pe zonele pietonale în orice direcție, însă pistele de biciclete se vor traversa, în linie dreaptă, paralel cu axele. În figura alăturată avem un parc de dimensiuni `10 x 8`, cu piste de biciclete verticale între `2` și `4` respectiv `5` și `8`, și orizontale între `0` și `1` respectiv între `2` și `4`. Gigel se află în punctul `A(1, 1)` și poate să ajungă pe drumul cel mai scurt la prietenul lui, în punctul `B(8, 7)` deplasându-se astfel: pornește din punctul `(1, 1)` și parcurge un traseu format din segmente cu extremitățile în punctele de coordonate `(1.5, 2) (1.5, 4) (2, 5) (4, 5) (5, 7)` și în final ajunge în punctul de coordonate `(8, 7)`.

Lungimea totală a drumului va fi aproximativ `11.4721359`.
\\
~[parc.png]

# Task
Given the dimensions of the park, the coordinates of Gigel, the coordinates of his friend, and the positions of the bike paths, calculate the minimum path length and the number of distinct minimum-length paths.

# Input data
The file `parc.in` contains on the first line two natural numbers `Xparc` and `Yparc` separated by a space, representing the dimensions of the park in the directions `Ox` and `Oy` respectively. The second line will contain four numbers separated by a space `xG, yG, xpr` and `ypr` representing Gigel's coordinates and his friend's coordinates. The third line will contain a natural number `m`, representing the number of vertical bike paths. The next `m` lines will contain pairs of values on the `Ox` axis that delimit a vertical bike path. The next line will contain a natural number `n`, representing the number of horizontal bike paths. The next `n` lines will contain pairs of values on the `Oy` axis that delimit a horizontal bike path.

# Output data
The file `parc.out` will contain on the first line the minimum length of the required path, a real number. The second line will contain the number of distinct minimum paths, a natural number.

# Constraints and clarifications
* `0 \leq xG, xpr \leq Xparc \leq 30\ 000, 0 \leq yG, ypr \leq Yparc \leq 30\ 000`;
* `0 < m, n < 2000`;
* the pairs of natural numbers that define a bike path are not ordered;
* horizontal, and vertical paths are not ordered in the input file;
* two bike paths of the same direction do not overlap;
* Gigel and his friend are in pedestrian zones (including their edges);
* two paths are distinct if they differ by at least one point;
* the number of distinct paths will not exceed `1\ 000\ 000\ 000`;
* the length of the path in the output file is a real number that will be accepted with a maximum error of `0.01`;
* scientific notation for displaying real numbers is not allowed;
* the first task is worth `40%` of the score, the second is worth `60%` of the score.

# Example

`parc.in`
```
10 8
1 1 8 7
2
5 8 
2 4
2
4 2
0 1
```

`parc.out`
```
11.472136
1
```

Explanations
---

- the minimum length of the path was calculated in the example above, the result can be printed with any number of decimals, the absolute difference from the official result should not differ by more than `0.01`
- there is only one path of minimum length