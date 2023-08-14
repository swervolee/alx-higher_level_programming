#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - pints a python list info from c
 * @p: Python object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int size, i;
	PyListObject *list;
	PyObject *item;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
/*
void print_python_list_info(PyObject *p)
{
	long int list;

	list = PyList_Size(p);
	printf("[*] Size of the Python List = %ld", list);
}
*/
