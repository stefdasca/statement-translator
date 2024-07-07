
Bubu and Puffy have started gambling. Although it sounds strange, they are playing the famous game called Hangman. But because they got bored, now they want to play with you. They will give you a dictionary with `N` words formed only with lowercase letters of the alphabet, and then `T` secret words for which you will only know their lengths. You will need to "guess" each secret word, having at your disposal the functions:
```cpp
std::vector<int> ask(char ch);
bool guess(const std::string& word);
```

The `ask` function means that you ask if the letter `ch` appears in the secret word. The cost of this operation is `1`. The function returns the positions (indexed from `0`) where the letter appears in the secret word.

The `guess` function means a "guess" of the word. If the word matches the secret one, the cost of the operation is `0`. Otherwise, the cost of the operation is `3` + the number of invalid "guesses" previously made for the current word. The function returns true if the guessed word matches the secret word, false otherwise.

# Task
Given a dictionary with `N` words and `T` secret words for which only the lengths are read, write a program that obtains the minimum cost to "guess" all the words.

# Interaction
Your program will not read from or write to any file. Instead, it will have to implement the following functions:
```cpp
void init(int n, std::vector<std::string>& dict);
std::string solve(int len);
```
The `init` function will be called only once at the beginning of each test and will provide the number of words in the dictionary and the words in the dictionary.
The `solve` function will be called `T` times and will provide the number of letters of the current word you need to guess. The function will return the current secret word.
You do not need to implement the `main` function, but you can declare additional variables/functions. You can call the described `ask` and `guess` functions.

# Constraints and clarifications
* `1 \ \leq N \ \leq 70\ 000`
* `1 \ \leq T \ \leq 75`
* `5 \ \leq length\ of\ a\ word \ \leq 21`
* For `20%` of the tests `N \ \leq 25\ 000`
* The words in the dictionary contain only lowercase letters of the English alphabet and are similar to the explanatory dictionary of the Romanian language.
* All words have an equal chance of appearing in a test.
* The problem has been adapted.
* You need to include the file `spnzr.h`.

# Scoring
The score for a test will be 0 if one of the following situations occurs:
* Your program exceeds the maximum execution time/test;
* Your program does not follow the communication protocol;
* Your program does not "guess" all the `T` secret words.

The score for a test will be calculated based on a predefined score by the committee, according to a certain formula.

# Example of interaction
The function `init(2,{"banana","benene"})` is called by the committee.
The function `solve(6)` is called by the committee.

In `solve`:
The contestant calls `ask('n')`. The function returns `{2,4}`, the cost is `0+1=1`.
The contestant calls `ask('b')`. The function returns `{0}`, the cost is `1+1=2`.
The contestant calls `guess("benene")`. The function returns `false`, the cost is `2+3=5`.
The contestant calls `ask('a')`. The function returns `{1,3,5}`, the cost is `5+1=6`.
The contestant calls `guess("banana")`. The function returns `true`, the cost is `6+0=6`.
`solve` returns `"banana"`, the total cost is `6`.
