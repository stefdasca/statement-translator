# Task
Amicii Aronius și Disconsius nu prea au nimic important de făcut, așa că își petrec zilele făcând diverse activități. Astfel, au construit o piramidă de înălțime *N* în grădină și au scris un cuvânt pe ea, repetându-l până când completează toată piramida. Astfel, ei încep din vârf și scriu toate literele cuvântului în ordine, de la stânga la dreapta, pe linia respectivă. Literele rămase din cuvânt se scriu în continuare pe următoarea linie, însă schimbând sensul scrierii(dacă linia precedentă a avut scriere de la stânga la dreapta, linia curentă va avea scriere de la dreapta la stânga) și continuând să completeze linia, scriind din nou cuvântul de la capăt(sensul scrierii se menține).

~[Capture1.PNG]

Piramida a fost completată cu cuvântul `JANJETINA`.

Disconsius a ales acum $K$ linii ale piramidei, cu indicii $a_i (1 \le i \le K)$, și a ales o literă $c_i (1 \le i \le K) $ pentru fiecare linie. Apoi i-a pus lui Aronius $K$ întrebări complicate: „De câte ori litera $c_i$ apare pe linia $a_i$?�.
Aronius nu este la fel de deștept ca tine și ești singurul care îl poate ajuta să îi răspundă lui Disconsius (dacă nu va ști răspunsul întrebărilor, Disconsius se va supăra și nu va mai fi prieten cu el). Scrieți un program care să răspundă la întrebările lui Disconsius, pentru înălțimea piramidei și cuvântul date. Aronius se bazează pe voi să îi rezolvați această problemă.

**Note: Input data is read from the keyboard, and output data is displayed on the console.**

# Input data
The first line of input contains the natural number $N$.  
The second line of input contains a word which is composed only of uppercase English letters.  
The third line of input contains the natural number $K$, the number of lines chosen by Disconsius.  
Each of the following $K$ lines contains the pair $a_{i} \ c_{i} (1 \le a_i \le N; c_i$ is an uppercase English letter$)$, representing Disconsius' questions.

# Output data
Print on $K$ lines a number for each line, representing how many times $c_i$ appears on line $a_i$.

# Constraints and clarifications
- $1 \le N \le 10^{18} $
- $1 \le K \le 50\ 000 $
- The length of the word does not exceed $10^6$ characters.
- For tests worth 50 points, $N \le 1000$.
- For tests worth 70 points, the length of the word does not exceed $10^5$.
- For the remaining 30 points, there are no other restrictions.

# Example 1
  `stdin`
  ```
  6
JANJETINA
5
1 J
1 A
6 N
6 I
5 E
  ```

  `stdout`
  ```
1
0
2
1
1
  ```

# Example 2

`stdin`
  ```
  5
A
5
1 A
2 A
3 A
4 A
5 B
  ```

  `stdout`
  ```
1
2
3
4
0
  ```

# Example 3

`stdin`
  ```
3
AB
3
2 A
2 B
3 B
  ```

  `stdout`
  ```
1
1
2
  