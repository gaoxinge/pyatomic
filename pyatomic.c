#include "Python.h"
#include <stdatomic.h>

PyObject *f1(PyObject *self, PyObject *args) {
    PyLongObject *ob = (PyLongObject *) args;
    ob->ob_digit[0]++;
    Py_RETURN_NONE;
}

PyObject *f2(PyObject *self, PyObject *args) {
    PyLongObject *ob = (PyLongObject *) args;
    atomic_fetch_add(ob->ob_digit, 1);
    Py_RETURN_NONE;
}

PyObject *f3(PyObject *self, PyObject *args) {
    PyObject *ob = PyList_GET_ITEM(args, 0);
    long a = PyLong_AsLong(ob);
    a++;
    PyList_SET_ITEM(args, 0, PyLong_FromLong(a));
    Py_DECREF(ob);
    Py_RETURN_NONE;
}

PyObject *f4(PyObject *self, PyObject *args) {
    PyObject *ob = PyList_GET_ITEM(args, 0);
    long a = PyLong_AsLong(ob);
    atomic_fetch_add(&a, 1);
    PyList_SET_ITEM(args, 0, PyLong_FromLong(a));
    Py_DECREF(ob);
    Py_RETURN_NONE;
}

static PyMethodDef methods[] = {
    {"f1", f1, METH_O},
    {"f2", f2, METH_O},
    {"f3", f3, METH_O},
    {"f4", f4, METH_O},
    {NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "pyatomic",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_pyatomic(void) {
    return PyModule_Create(&module);
}