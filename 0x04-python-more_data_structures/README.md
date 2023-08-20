# Python - More Data Structures: Set, Dictionary

I delved into Sets and Dictionaries. Sets are collections of distinct elements, like a treasure chest without duplicates, offering quick checks for membership. Dictionaries, resembling enchanted books, store values under unique keys, enabling swift retrieval by key. Sets and Dictionaries excel in sorting, modifying, and accessing data, making them potent tools for efficient data manipulation. Whether summoning specific items or managing complex information, these structures provide key advantages, serving as guardians of fast performance in various scenarios.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File                           | Prototype                                                                                                 |
| ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| `0-square_matrix_simple.py`    | `def square_matrix_simple(matrix=[]):`                                                                    |
| `1-search_replace.py`          | `def search_replace(my_list, search, replace):`                                                           |
| `2-uniq_add.py`                | `def uniq_add(my_list=[]):`                                                                               |
| `3-common_elements.py`         | `def common_elements(set_1, set_2):`                                                                      |
| `4-only_diff_elements.py`      | `def only_diff_elements(set_1, set_2):`                                                                   |
| `5-number_keys.py`             | `def number_keys(a_dictionary):`                                                                          |
| `6-print_sorted_dictionary.py` | `def print_sorted_dictionary(a_dictionary):`                                                              |
| `7-update_dictionary.py`       | `def update_dictionary(a_dictionary, key, value):`                                                        |
| `8-simple_delete.py`           | `def simple_delete(a_dictionary, key=""):`                                                                |
| `9-multiply_by_2.py`           | `def multiply_by_2(a_dictionary):`                                                                        |
| `10-best_score.py`             | `def best_score(a_dictionary):`                                                                           |
| `11-mutiply_list_map.py`       | `def mutiply_list_map(my_list=[], number=0):`                                                             |
| `12-roman_to_int.py`           | `def roman_to_int(roman_string):`                                                                         |
| `100-weight_average.py`        | `def weight_average(my_list=[]):`                                                                         |
| `101-square_matrix_map.py`     | `def square_matrix_map(matrix=[]):`                                                                       |
| `102-complex_delete.py`        | `def complex_delete(a_dictionary, value):`                                                                |
| `103-python.c`                 | <ul><li>`void print_python_list(PyObject *p);`</li><li>`void print_python_bytes(PyObject *p);`</li></ul> |

## Tasks :page_with_curl:

* **0. Squared simple**
  * [0-square_matrix_simple.py](./0-square_matrix_simple.py): Python function that computes
  the square value of all integers of a matrix.
  * Returns a matrix of the same size as `matrix` where each value is the
  square of the input value.

* **1. Search and replace**
  * [1-search_replace.py](./1-search_replace.py): Python function that replaces all occurences
  of an element by another in a new list.

* **2. Unique addition**
  * [2-uniq_add.py](./2-uniq_add.py): Python function that adds all unique integers in
  a list (once for each integer).

* **3. Present in both**
  * [3-common_elements.py](./3-common_elements.py): Python function that returns a
  set of common elements in two sets.

* **4. Only differents**
  * [4-only_diff_elements.py](./4-only_diff_elements.py): Python function that returns a
  set of all elements present in only one set.

* **5. Number of keys**
  * [5-number_keys.py](./5-number_keys.py): Python function that returns the number of
  keys in a dictionary.

* **6. Print sorted dictionary**
  * [6-print_sorted_dictionary.py](./6-print_sorted_dictionary.py): Python function that
  prints a dictionary by ordered keys.

* **7. Update dictionary**
  * [7-update_dictionary.py](./7-update_dictionary.py): Python function that replaces or
  adds key/value pairs in a dictionary.

* **8. Simple delete by key**
  * [8-simple_delete.py](./8-simple_delete.py): Python function that deletes a key
  in a dictionary.

* **9. Multiply by 2**
  * [9-multiply_by_2.py](./9-multiply_by_2.py): Python function that returns a
  new dictionary with all values multiplied by 2.

* **10. Best score**
  * [10-best_score.py](./10-best_score.py): Python function that returns a key value
  with the biggest integer value.

* **11. Multiply by using map**
  * [11-mutiply_list_map.py](./11-multiply_list_map.py): Python function that returns a
  list with all values multiplied by a number using `map`.

* **12. Roman to Integer**
  * [12-roman_to_int.py](./12-roman_to_int.py): Python function that converts a roman
  numeral to an integer.

* **13. Weighted average!**
  * [100-weight_average.py](./100-weight_average.py): Python function that returns the
  weighted average of all integers in a list of tuples.

* **14. Squared by using map**
  * [101-square_matrix_map.py](./101-square_matrix_map.py): Python function that computes
  the square value of all integers of a matrix using `map`.

* **15. Delete by value**
  * [102-complex_delete.py](./102-complex_delete.py): Python function that deletes keys with
  a specific value in a dictionary.

* **16. CPython #1: PyBytesObject**
  * [103-python.c](./103-python.c): C functions that print basic information about
  Python lists and Python bytes objects.
