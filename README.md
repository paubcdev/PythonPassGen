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
7. It asks if you want to know the entropy of it, and displays it accordingly.
8. Finally, asks if you want to know the hash of the password, according to 3 standards (SHA2-256, SHA3-256 and BLAKE2b).

---
 
### WiP:

---

### TODO:
1. Write unit tests for the script.

---

### WON'T DO:
1. First letter capitalizer.

---

### DONE:
1. Password generator. 
2. Random capitalizer.
3. All caps.
4. Entropy visualizer.
5. Hashing passwords 3 methods: SHA2-256, SHA3-256 & BLAKE2b.

---
2024 - paubcdev