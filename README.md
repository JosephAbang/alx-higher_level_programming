# Python - Hello, World (done by Joseph Abang)

This project started by testing my ability to use a shell script to run a python script. It then tested how efficient I am in manipulating string objects. I was able to do all the mandatory tasks and give an excellent attempt at the advanced tasks. The bytecode and compiling tasks were the most challenging as it required a high level of deep research. I ran so maby codes without getting the required output until i used a resource which pointed me to the solution. At the end of this readme, i have attached resources that came in handy in workng on this project.


## Function Prototypes:

Prototypes for functions written in this project:

| File                       | Prototype                             |
| -------------------------- | ------------------------------------- |
| `10-check_cycle.c`         | `int check_cycle(listint_t *list);`   |
| `102-magic_calculation.py` | `def magic_calculation(a, b):`        |

## Tasks :page_with_curl:

* **0. Run Python File**
  * [0-run](./0-run): A Bash script designed to execute a Python script file that is stored in the environment variable $PYFILE.

* **1. Run inline**
  * [1-run_inline](./1-run_inline): Bash script that runs a Python code saved in the
  environment variable `$PYCODE`.

* **2. Hello, print**
  * [2-print.py](./2-print.py): This python script that prints exactly `"Programming is
  like building a multilingual puzzle`, followed by a new line using the function `print`.

* **3. Print integer**
  * [3-print_number.py](./3-print_number.py): This is a python script that prints the integer stored
  in the variable `number`, followed by `Battery street`, followed by a new line.

* **4. Print float**
  * [4-print_float.py](./4-print_float.py): Python script that prints the float stored
  in the variable `number` with a precision of two digits.

* **5. Print string**
  * [5-print_string.py](./5-print_string.py): Python script that prints a string stored
  in the variable `str` three times, then a new line, then the first nine characters
  contained in `str`, followed by another new line.

* **6. Play with strings**
  * [6-concat.py](./6-concat.py): Python script that prints `Welcome to Holberton
  School!` using the variables `str1 = "Holberton"` and `str2 = "School"`.

* **7. Copy - Cut - Paste**
  * [7-edges.py](./7-edges.py): Python script that sets three string variables based
  on the string contained in the variable `word` as follows:
  * `word_first_3`: Contains the first three letters of the variable `word`.
  * `word_last_2`: Contains the last two letters of the variable `word`.
  * `middle_word`: Contains the value of the variable `word` without the first and last letters.

* **8. Create a new sentence**
  * [8-concat_edges.py](./8-concat_edges.py): Python script that prints `object-oriented
  programming with Python`, followed by a new line without creating new variables or
  string literals.

* **9. Easter Egg**
  * [9-easter_egg.py](./9-easter_egg.py): Python script that prints "The Zen of Python" by
  Tim Peters, followed by a new line.

* **10. Linked list cycle**
  * [10-check_cycle.c](./10-check_cycle.c): C function that checks if a linked list
  contains a cycle.
  * Returns `0` if there is no cycle and `1` if there is.
  * Helper files:
    * [linked_lists.c](./linked_lists.c): C functions handling linked lists for testing
    [10-check_cycle.c](./10-check_cycle.c) (provided by alx).
    * [lists.h](./lists.h): Header file containing definitions and prototypes for
    all types and functions used in [linked_lists.c](./linked_lists.c) and
    [10-check_cycle.c](./10-check_cycle.c).

* **11. Hello, write**
  * [100-write.py](./100-write.py): Python script that prints exactly `and that piece of
  art is useful - Dora Korpar, 2015-10-19`, followed by a new line to `stderr` using
  the function `write` from the `sys` module.
  * Exits with a status code of `1`.

* **12. Compile**
  * [101-compile](./101-compile): Python script that compiles a Python script file stored
  in the environment variable `$PYFILE` and saves it to an output file
  `$PYFILEc` (ex. `export PYFILE=my_main.py` => output filename: `my_main.pyc`).

* **13. ByteCode -> Python #1**
  * [102-magic_calculation.py](./103-magic_calculation.py): Python function matching exactly
  a bytecode.
