#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - pints a python list info from c
 * @p: Python object
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	long int list;

	list = PyList_Size(p);
	printf("[*] Size of the Python List = %ld", list);
}
