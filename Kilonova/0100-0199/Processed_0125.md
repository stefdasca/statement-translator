Județul în care are loc Olimpiada Națională de Informatică de anul acesta este puțin ciudat. În județ există `N` orașe, numerotate de la `1` la `N`. Fiecare dintre cele `N` orașe ale județului este legat de **EXACT** alte `2` orașe, prin străzi bidirecționale. Și mai ciudat este faptul că, în cadrul acestui sistem stradal, nu este întotdeauna posibil să ajungi din orice oraș în oricare alt oraș mergând pe străzi. Oricum, locuitorii județului sunt mândri de acest sistem al lor și sunt de părere că nu mai există altul la fel. Dumneavoastră vreți să le demonstrați contrariul și pentru aceasta vreți să calculați câte sisteme stradale distincte cu proprietatea de mai sus există. Două sisteme sunt considerate distincte dacă există cel puțin o stradă între o pereche de orașe `i` și `j` în cadrul primului sistem, care nu există în cadrul celui de-al doilea.

# Task
Write a program that calculates how many distinct street systems exist modulo `1 000 000 007`.

# Input data
From the file `sistem.in` you will read the integer value `n`, representing the number of cities in the county.

# Output data
In the file `sistem.out` you will print an integer value, representing the number of distinct street systems, with the property that any city is directly connected by streets to exactly other `2` cities.

# Constraints
* `3 \leq n \leq 100 000`
* The constraints and the task have been modified
* For 16 points we have `n \leq 14`
* For another 16 points we have `n \leq 100`
* For another 16 points we have `n \leq 500`
* For another 16 points we have `n \leq 2000`

# Examples
`sistem.in`
```
4
```

`sistem.out`
```
3
```

`sistem.in`
```
6
```

`sistem.out`
```
70
```

`sistem.in`
```
776
```

`sistem.out`
```
552369242
```

Explanation
---

The `3` solutions are as follows:
\
~[sistem.png]