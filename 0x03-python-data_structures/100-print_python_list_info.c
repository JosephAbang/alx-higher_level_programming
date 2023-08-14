#include <Python.h>

/**
 * print_python_list_info - Print info of python list
 * @p: Struct pointer containing data
 * Return: void
 **/

void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p), i;
	int alloc = ((PyListObject *)p)->allocated;

	if (p == NULL || !PyList_Check(p))
	{
		return;
	}
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);

		if (PyLong_Check(item)) {
			printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
  		} else if (PyFloat_Check(item)) {
			printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
        	} else if (PyUnicode_Check(item)) {
			printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
        	} else if (PyTuple_Check(item)) {
           		printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
        	} else if (PyList_Check(item)) {
            		printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
        	} else if (PyBytes_Check(item)) {
            		printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
        	} else if (PyBool_Check(item)) {
			printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
		} else if (PyDict_Check(item)) {
			printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
		} else if (PyByteArray_Check(item)) {
			printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
		} else if (PySet_Check(item)) {
			printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
		}
		else {
			printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
       		}
	}
}
