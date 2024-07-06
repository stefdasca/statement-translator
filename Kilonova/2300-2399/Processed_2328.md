Ștefan trebuie să verifice dacă Ana, sora lui mai mică, a înțeles corect conceptul de triunghi echilateral și îi propune o temă. În prima zi Ana trebuie să deseneze un triunghi echilateral $T_0$ cu latura $1$. A doua zi ea trebuie să deseneze un triunghi echilateral cu latura $2$ și, apoi, în fiecare zi trebuie să deseneze un nou triunghi echilateral având latura mai mare cu $1$ decât latura triunghiului din ziua precedentă.

Ana, atentă, observă că fiecare triunghi este format din triunghiuri elementare $T_0$ și etichetează zilnic aceste triunghiuri elementare de la vârf către bază și de la stânga către dreapta, ca în figura de mai jos. Ea observă de asemenea că triunghiurile elementare pot fi grupate pe niveluri, astfel: triunghiul $1$ — nivelul $1$; triunghiurile $2$, $3$, $4$ — nivelul $2$; triunghiurile $5$, $6$, $7$, $8$, $9$ — nivelul $3$; etc.

~[img.png|width=40em]

# Task

Ștefan are câteva întrebări pentru Ana și vă roagă să o ajutați. Scrieți un program care, pentru un număr natural $n$ dat, să determine:
1. Câte triunghiuri elementare $T_0$ au fost desenate în $n$ zile.
2. În ce zi a fost desenat și pe ce nivel se află al $n$-lea triunghi elementar $T_0$ desenat de Ana.
3. Câte triunghiuri elementare $T_0$ sunt etichetate cu numere prime în primele $n$ zile.

# Input data

Fișierul `triunghi.in` conține pe prima linie task $1$, $2$ sau $3$, iar pe a doua linie un număr natural $n$.

# Output data

Fișierul `triunghi.out` va conține o singură linie pe care va fi scris:
* task $1$: numărul de triunghiuri elementare $T_0$ desenate în $n$ zile;
* task $2$: ziua și nivelul pe care se află al $n$-lea triunghi elementar $T_0$, separate printr-un spațiu;
* task $3$: câte triunghiuri elementare $T_0$ sunt etichetate cu numere prime în cele $n$ zile.

# Constraints and clarifications

* $1 \leq n \leq 2 \\ 000$
* Fiecare task valorează câte $30$ de puncte.

# Example 1

`triunghi.in`
```
1
3
```

`triunghi.out`
```
14
```

## Explanation

Task is $1$. There are $14$ elementary triangles $T_0$ drawn.

# Example 2

`triunghi.in`
```
2
5
```

`triunghi.out`
```
2 2
```

## Explanation

Task is $2$. The $5$th triangle $T_0$ is drawn on day $2$, at level $2$.

# Example 3

`triunghi.in`
```
2
6
```

`triunghi.out`
```
3 1
```

## Explanation

Task is $2$. The $6$th triangle $T_0$ is drawn on day $3$, at level $1$.

# Example 4

`triunghi.in`
```
3
2
```

`triunghi.out`
```
2
```

## Explanation

Task is $3$. In the first $2$ days, there are $2$ elementary triangles labeled with prime numbers.

# Example 5

`triunghi.in`
```
3
3
```

`triunghi.out`
```
6
```

## Explanation

Task is $3$. In the first $3$ days, we have $0+2+4 = 6$ elementary triangles labeled with prime numbers.