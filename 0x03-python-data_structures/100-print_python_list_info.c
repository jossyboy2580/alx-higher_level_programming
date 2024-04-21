#include "lists.h"
#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	if (p)
	{
		printf("P is a real object");
	}
}
