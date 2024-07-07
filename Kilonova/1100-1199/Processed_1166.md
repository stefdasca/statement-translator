
Mircea and Vasilică want to send messages that others cannot understand. They read about spies and ways to write messages and, finally, they imagined a way to encrypt a message that uses a “key word�.

By choosing a key word made only of distinct letters, they count its letters and divide the message into groups of length equal to the number of letters in the key word, placing them one below the other.

Of course, it may happen that the last group is incomplete, so they fill it with spaces.

Then they number the letters of the key word in the order they appear in the English alphabet. Finally, they rewrite the message таким образом that it corresponds to the column under the letter numbered with $1$, followed by the column under the letter numbered with $2$, etc., replacing the spaces with the character `*` (asterisk).

Example:

* key word: `criptam`
* message to be encrypted: `Incercam sa lucram cu coduri si criptari.`
* the key word `criptam` has $7$ letters
* numbering: $2635714$, because we have in order
$$
\begin{CD}
   {\huge a} @. b @. {\huge c} @. d @. e @. f @. g @. h @. { \huge i} @. j @. k @. l @. {\huge m} @. n @. o @. {\huge p} @. \ \ \ \  q \ \ @. {\huge r} @. s @. {\huge t} @. u @. v @. w @. x @. z @. y \\
 @V{\small cript}{\LARGE a}{\small m}VV @. @VV{\LARGE c}{\small riptam}V @. @. @. @. @. @V{\small cr}{\LARGE i}{\small ptam} VV @. @. @. @V{\small cripta}{\LARGE m}VV @. @. @V{ \small cri}{\LARGE p }{\small tam }VV @. @V{\small c}{\LARGE r}{\small iptam}VV @. @VV{\small crip}{\LARGE t}{\small am}V @. @. @.\\
   1 @. @. 2 @. @. @. @. @. @. 3 @. @. @. @. 4 @. @. @. 5 @. @. 6 @. @. 7 @. @. @. @. @. @. \\
   @. @. @. @. @. @. @. @. @. @. @. @. @. @. @. @. @. @. @. @. @. @. @.\\
\end{CD}
$$
* division into groups: `Incerca`, `m sa lu`, `cram cu`, `coduri`, ` si cri`, `ptari. ` $→$ `Incerca`, `m*sa*lu`, `cram*cu`, `coduri`, `*si*cri`, `ptari.*`
* encoding:

$$

\begin{array}{}

\begin{array}{}

\begin{array}{|c|c|c|c|c|c|c|}
\hline
I &n &c &e &r &c &a \\
\hline
\end{array}

\ \

\begin{array}{|c|c|c|c|c|c|c|}
\hline
m &* &s &a &* &l &u \\
\hline
\end{array}

\ \

\begin{array}{|c|c|c|c|c|c|c|}
\hline
c &r &a &m &* &c &u \\
\hline
\end{array}

\ \

\begin{array}{|c|c|c|c|c|c|c|}
\hline
* &c &o &d &u &r &i \\
\hline
\end{array}

\ \

\begin{array}{|c|c|c|c|c|c|c|}
\hline
* &s &i &* &c &r &i \\
\hline
\end{array}

\ \

\begin{array}{|c|c|c|c|c|c|c|}
\hline
p &t &a &r &i &. &* \\
\hline
\end{array}

\end{array}

\end{array}


\rightarrow 

\begin{array}{|c|}

2 \\
\begin{array}{|c|}
\hline
I \\
\hline
m \\
\hline
c  \\
\hline
* \\
\hline
* \\
\hline
p \\
\hline
\end{array}
\ \

6 \\
\begin{array}{|c|}
\hline
n \\
\hline
* \\
\hline
r \\
\hline
c \\
\hline
s \\
\hline
t \\
\hline
\end{array}
\ 

3 \\
\begin{array}{|c|}
\hline
c \\
\hline
s \\
\hline
a  \\
\hline
o \\
\hline
i \\
\hline
a \\
\hline
\end{array}
\ 

5 \\
\begin{array}{|c|}
\hline
e \\
\hline
a \\
\hline
m  \\
\hline
d \\
\hline
* \\
\hline
r \\
\hline
\end{array}
\ 

7 \\
\begin{array}{|c|}
\hline
r \\
\hline
* \\
\hline
*  \\
\hline
u \\
\hline
c \\
\hline
i \\
\hline
\end{array}
\ 

1 \\
\begin{array}{|c|}

\hline
c \\
\hline
l \\
\hline
c \\
\hline
r \\
\hline
r \\
\hline
. \\
\hline
\end{array}
\ 

4 \\
\begin{array}{|c|}
\hline
a \\
\hline
u \\
\hline
u  \\
\hline
i \\
\hline
i \\
\hline
* \\
\hline
\end{array}

\end{array}

\rightarrow 
\begin{array}{}

\ \ 
\begin{array}{}
1 \\
\begin{array}{|c|}
\hline
c \\
\hline
l \\
\hline
c \\
\hline
r \\
\hline
r \\
\hline
. \\
\hline
\end{array}
\end{array}

\ 

\begin{array}{}
2 \\
\begin{array}{|c|}
\hline
I \\
\hline
m \\
\hline
c  \\
\hline
* \\
\hline
* \\
\hline
p \\
\hline
\end{array}
\end{array}

\ 

\begin{array}{}
3 \\
\begin{array}{|c|}
\hline
c \\
\hline
s \\
\hline
a  \\
\hline
o \\
\hline
i \\
\hline
a \\
\hline
\end{array}
\end{array}

\ 

\begin{array}{}
4 \\
\begin{array}{|c|}
\hline
a \\
\hline
u \\
\hline
u  \\
\hline
i \\
\hline
i \\
\hline
* \\
\hline
\end{array}
\end{array}

\ 

5 \\
\begin{array}{|c|}
\hline
e \\
\hline
a \\
\hline
m  \\
\hline
d \\
\hline
* \\
\hline
r \\
\hline
\end{array}
\end{array}

\ 

6 \\
\begin{array}{|c|}
\hline
n \\
\hline
* \\
\hline
r \\
\hline
c \\
\hline
s \\
\hline
t \\
\hline
\end{array}
\end{array}

\ 

7 \\
\begin{array}{|c|}
\hline
r \\
\hline
* \\
\hline
*  \\
\hline
u \\
\hline
c \\
\hline
i \\
\hline
\end{array}
\end{array}

\ \ 
\rightarrow
\ \ 
\text{clcrr.Imc**pcsaoiaauuii*eamd*rn*rcstr**uci}
$$



# Task

Decode the message sent by Mircea to Vasilică given a key word and an encrypted message.


# Input data

The input file `criptare.in` contains on the first line the encrypted message and on the second line the key word.


# Output data

The input file `criptare.out` contains on the first line the decrypted message.


# Constraints and clarifications

* the length of the message is minimum $20$ and maximum $1\ 000$ characters
* the key word has a minimum of $5$ and a maximum of $20$ characters
* the key word contains only lowercase letters of the alphabet


# Example

`criptare.in`
```
clcrr.Imc**pcsaoiaauuii*eamd*rn*rcstr**uci
criptam
```

`criptare.out`
```
Incercam sa lucram cu coduri si criptari.
```
