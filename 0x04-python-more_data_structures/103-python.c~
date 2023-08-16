#include <stdio.h>
#include <Python.h>

/**
 * display_python_bytes_info - Displays bytes information
 *
 * @obj: Python Object
 * Return: No return
 */
void display_python_bytes_info(PyObject *obj) {
    char *byte_data;
    long int size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(obj)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)(obj))->ob_size;
    byte_data = ((PyBytesObject *)obj)->ob_sval;

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", byte_data);

    if (size >= 10)
        limit = 10;
    else
        limit = size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++) {
        if (byte_data[i] >= 0)
            printf(" %02x", byte_data[i]);
        else
            printf(" %02x", 256 + byte_data[i]);
    }

    printf("\n");
}

/**
 * display_python_list_info - Displays list information
 *
 * @obj: Python Object
 * Return: No return
 */
void display_python_list_info(PyObject *obj) {
    long int size, i;
    PyListObject *list;
    PyObject *item;

    size = ((PyVarObject *)(obj))->ob_size;
    list = (PyListObject *)obj;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        item = ((PyListObject *)obj)->ob_item[i];
        printf("Element %ld: %s\n", i, ((item)->ob_type)->tp_name);
        if (PyBytes_Check(item))
            display_python_bytes_info(item);
    }
}
