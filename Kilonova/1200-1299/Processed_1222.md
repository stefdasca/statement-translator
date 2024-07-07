## Task

One of the oldest encryption methods, known as Caesar cipher, involves the following: given the 26 uppercase letters of the alphabet and a natural number $k$, called the key, each letter in the text to be encoded is replaced by the $k$-th letter following it in the alphabet, with spaces between words remaining unmodified. Thus, if the text "CODIFICARE CEZAR" is to be encoded with the key $k=5$, the encoded text will be "HTINKNHFWJ HJEFW". It can be observed that if the string of alphabet letters reaches the end, counting resumes from the beginning (circularly). However, this type of encryption is extremely easy to "crack." Let us then imagine another method of encryption.

Assuming, as in the previous case, that the text to be encoded contains only uppercase letters and spaces. For encryption, proceed as follows:
1. Spaces are removed.
2. The obtained text is divided into segments of 10 letters each, and the segments are placed one below the other; the last segment may be shorter.
3. A sequence of 10 natural numbers (10 keys) $k_1$, $k_2$, $\dots$, $k_{10}$ is chosen, and each column is encoded using the Caesar cipher with the key corresponding to the column ($k_1$ - column 1, $k_2$ - column 2, $\dots$).
4. The text is restored by putting the segments back in place and then replacing the spaces.

For example, if we need to encode the text "OLIMPIADA NATIONALA DE INFORMATICA DE LA GALATI," we will obtain, respectively, at the four steps:
1. ``OLIMPIADANATIONALADEINFORMATICADELAGALATI``
2. 
    ```
    OLIMPIADAN
    ATIONALADE
    INFORMATIC
    ADELAGALAT
    I
    ```
3. Let the chosen keys be ($k_1$, $k_2$, $\dots$, $k_{10}$) = ($1$, $2$, $1$, $3$, $1$, $4$, $1$, $5$, $0$, $6$)
    ```
    PNJPQMBIAT
    BVJRMEMFDK
    JPGRSQBYII
    BFFDBKBQAZ
    J 
    ```
4. ``PNJPQMBIATBVJRMEMFDKJPGRSQBYIIBFFOBKBQAZJ``
   ``PNJPQMBIA TBVJRMEMF DK JPGRSQBYIIB FF OB KBQAZJ``

# Task

Write a program to decode a text encoded in the manner described above.

# Input data

The input file `cezar.in` contains on the first line the encoded text. The second line of the file contains 10 natural numbers separated by a space representing the encoding keys.

# Output data

The output file `cezar.out` will contain on the first line the decoded text.

# Constraints and clarifications

* The length of the encoded text does not exceed $255$ characters.
* The used characters are uppercase letters of the alphabet and the space character.
* The keys have values between $0$ and $25$.
* The letters of the alphabet are, in order:
```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
```

# Example

`cezar.in`
```
PPLKNS NIUKUK 
1 2 3 4 5 6 7 8 9 10
```

`cezar.out`
```
ONIGIM GALATI 
