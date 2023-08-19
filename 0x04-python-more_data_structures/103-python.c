#include <Python.h>
#include <string.h>

/**
 * print_python_list - Prints info about a python list
 * @p: list
 * Return: void
 **/

void print_python_list(PyObject *p)
{
	Py_ssize_t l_alloc = ((PyListObject *)p)->allocated;
	Py_ssize_t l_size = ((PyVarObject *)p)->ob_size;
	ssize_t i = 0;
	PyObject *elem;

	printf("[*] Print list info\n");
	printf("[*] Size of the Python List = %ld\n", l_size);
	printf("[*] Allocated = %ld\n", l_alloc);
	while (i < l_size)
	{
		elem = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, elem->ob_type->tp_name);
		i++;
	}
}


/** print_python_bytes - Prints info about a python bytes
 * @p: list
 * Return: void
 **/

void print_python_bytes(PyObject *p)
{
	Py_ssize_t b_size = ((PyVarObject *)p)->ob_size;
	ssize_t i = 0;
	char *str = ((PyBytesObject *)p)->ob_sval;
	/*PyObject *bytes = PyBytes_FromString(str);*/

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("   size: %ld\n", b_size);
		printf("   trying string: %s\n", str);

		b_size = b_size < 10 ? b_size + 1: 10;
		printf("   first %ld bytes: ", b_size);
		/*printf("%s", PyBytes_AS_STRING(p));*/
		while (i < b_size)
		{
			printf("%02hhx ", str[i]);
			i++;
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
