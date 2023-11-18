# Python - Object-relational mapping

## Description

This project aims to bridge the realms of Databases and Python, introducing you to the usage of MySQL databases and Object Relational Mapping (ORM) with SQLAlchemy in Python.

In the first part, theproject utilizes the MySQLdb module to connect to a MySQL database and execute SQL queries. The second part explores SQLAlchemy, an ORM that abstracts storage usage in Python, eliminating the need for direct SQL queries. This allows for greater flexibility in changing storage types without rewriting the entire project.

## Tasks

Below is a table listing the tasks to be completed for this project:

| Task | Description |
|------|-------------|
| [0. Get all states](./0-select_states.py) | Lists all states from the hbtn_0e_0_usa database. |
| [1. Filter states](./1-filter_states.py) | Lists states with names starting with 'N' from hbtn_0e_0_usa database. |
| [2. Filter states by user input](./2-my_filter_states.py) | Displays values in the states table based on user input. |
| [3. SQL Injection...](./3-my_safe_filter_states.py) | Safely filters states by user input, preventing SQL injection. |
| [4. Cities by states](./4-cities_by_state.py) | Lists all cities from the hbtn_0e_4_usa database. |
| [5. All cities by state](./5-filter_cities.py) | Lists all cities of a specific state from hbtn_0e_4_usa database. |
| [6. First state model](./model_state.py) | Defines the State class and creates the Base instance using SQLAlchemy. |
| [7. All states via SQLAlchemy](./7-model_state_fetch_all.py) | Lists all State objects from hbtn_0e_6_usa using SQLAlchemy. |
| [8. First state](./8-model_state_fetch_first.py) | Prints the first State object from hbtn_0e_6_usa. |
| [9. Contains `a`](./9-model_state_filter_a.py) | Lists State objects containing the letter 'a' from hbtn_0e_6_usa. |
| [10. Get a state](./10-model_state_my_get.py) | Prints the id of a State object with a specific name from hbtn_0e_6_usa. |
| [11. Add a new state](./11-model_state_insert.py) | Adds the State object 'Louisiana' to hbtn_0e_6_usa. |
| [12. Update a state](./12-model_state_update_id_2.py) | Changes the name of a State object with id=2 to 'New Mexico'. |
| [13. Delete states](./13-model_state_delete_a.py) | Deletes all State objects with names containing the letter 'a' from hbtn_0e_6_usa. |
| [14. Cities in state](./model_city.py, ./14-model_city_fetch_by_state.py) | Defines City class and lists all City objects from hbtn_0e_14_usa using SQLAlchemy, organized by state. |
