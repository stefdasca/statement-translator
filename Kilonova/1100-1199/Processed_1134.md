Impresarul unei formații de muzică trebuie să primească oferte de spectacole și eventual anulări de spectacole din diferite orașe. Orașele sunt codificate prin numerele $1, 2, \dots, n$ și fiecare oraș poate organiza cel mult un spectacol. Impresarul ține legătura cu organizatorii de spectacole din aceste orașe și actualizează în permanență datele obținute. Prin fax el primește $m$ mesaje, care pot fi de unul din cele două tipuri: $D \ nr$ sau $N \ nr$.

Cu semnificațiile: pentru primul mesaj se dorește organizarea unui concert în orașul $nr$, iar pentru al doilea mesaj se dorește anularea spectacolului din orașul $nr$. Un mesaj este format din exact două linii.

Se cere:
1. Să se afișeze orașele în care va concerta formația de muzică (pe aceeași linie cu un spațiu între ele).
2. Să se afișeze orașul (sau orașele dacă sunt mai multe, pe aceeași linie cu un spațiu între ele) în care organizatorii sunt cei mai nedeciși (adică au anulat și propus organizarea de spectacol în orașul lor de cele mai multe ori).
3. Să se afișeze numărul de orașe care nu au trimis nici un mesaj impresarului.


# Input data

The first line of the input file `turneu.in` contains two integers, $n$ și $m$, representing the number of cities and the number of messages.

The next $m$ lines contain pairs of the form $D \ nr$ or $N \ nr$ with the meaning from the statement.

# Output data

The first line of the output file `turneu.out` will contain the cities where the music band will perform (on the same line with a space between them), in ascending order.
The second line will contain the cities with a maximum number of changes, in ascending order of their order number.
The third line will contain the number of cities that did not send any message to the impresario.

# Constraints and clarifications

* $1 \leq n, m \leq 100 \ 000$;
* The tests and constraints have been revised.
* It is guaranteed that a concert is not canceled if it was not organized, and also that a concert which has already been announced is not announced again.

# Example 1

`turneu.in`
```
5 6
D 2
D 3
N 3
D 3
D 5
N 2
```

`turneu.out`
```
3 5 
3 
2
```

