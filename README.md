# Python Password Generator

### Personal project to try to understand Python's "secrets" and random modules.
This imperfect project started as a way to try to understand how the "secrets" module works.

It is based on the [famous xkcd comic](https://xkcd.com/936/) about password strength.

---

Workflow in the main script works as follows:
1. First the script asks for a number of words to concatenate.
2. It will randomly choose that amount of words from the list, and append a number after every word.
3. Then asks for a "joiner", a character that will be inserted between the words.
4. It will append that joiner after the number.
5. Following that it asks if you want to randomly capitalize some characters in the generated string.
6. Then it prints either: a version without capitalized letters or with them.
7. Finally, it asks if you want to know the entropy of it, and displays it accordingly.

---
 
### WiP:

---

### TODO:
1. Write unit tests for the script.
2. Add more options:
   2. All letters capitalized.

---

### WON'T DO:
1. First letter capitalizer.

---

### DONE:
1. Password generator. 
2. Random capitalizer.
3. All caps.
4. Entropy visualizer.

---
2024 - paubcdev