# 0x0D. SQL - Introduction

## Overview

This project introduces you to SQL and MySQL. You will work on various tasks related to creating and managing databases, tables, and records in a MySQL server.

## Concepts

For this project, you are expected to understand the following concepts:

- Databases
- What is a database
- What's a relational database
- What does SQL stand for
- What's MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE, or DELETE data
- What are subqueries
- How to use MySQL functions

## Tasks

1. [List Databases](0-list_databases.sql)
   - Write a script that lists all databases on your MySQL server.

2. [Create a Database If Missing](1-create_database_if_missing.sql)
   - Write a script that creates the database "hbtn_0c_0" in your MySQL server, if it doesn't already exist.

3. [Delete a Database](2-remove_database.sql)
   - Write a script that deletes the database "hbtn_0c_0" in your MySQL server, if it exists.

4. [List Tables](3-list_tables.sql)
   - Write a script that lists all the tables in a specified database on your MySQL server.

5. [Create First Table](4-first_table.sql)
   - Write a script that creates a table named "first_table" in a specified database.

6. [Full Table Description](5-full_table.sql)
   - Write a script that prints the full description of the "first_table" in a specified database.

7. [List All Values](6-list_values.sql)
   - Write a script that lists all rows of the "first_table" in a specified database.

8. [Insert New Row](7-insert_value.sql)
   - Write a script that inserts a new row into the "first_table" in a specified database.

9. [Count Records with ID 89](8-count_89.sql)
   - Write a script that displays the number of records with an ID of 89 in the "first_table" of a specified database.

10. [Create Second Table](9-full_creation.sql)
    - Write a script that creates a table named "second_table" in a specified database and adds multiple rows.

11. [Select the Best](11-best_score.sql)
    - Write a script that lists all records with a score greater than or equal to 10 in the "second_table" of a specified database.
    - Results should display both the score and the name, ordered by score (highest score first).

12. [No Cheating](12-no_cheating.sql)
    - Write a script that updates the score of a record with the name "Bob" to 10 in the "second_table."
    - You are not allowed to use Bob's ID; only the name field can be used.

13. [Score Too Low](13-change_class.sql)
    - Write a script that removes all records with a score less than or equal to 5 in the "second_table."

14. [Average](14-average.sql)
    - Write a script that computes the average score of all records in the "second_table."
    - The result column should be named "average."

15. [Number by Score](15-groups.sql)
    - Write a script that lists the number of records with the same score in the "second_table."
    - Results should display the score and the number of records for that score, sorted by the number of records (descending).

16. [Say My Name](16-no_link.sql)
    - Write a script that lists all records in the "second_table."
    - Don't list rows without a name value.
    - Results should display the score and the name, listed by descending score.
