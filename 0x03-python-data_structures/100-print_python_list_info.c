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
	PyObject *item;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d:  %s\n", i, Py_TYPE(item)->tp_name);
	}
}
