from distutils.core import setup, Extension

setup(
    name="pyatomic",
    version="0.0.1",
    ext_modules=[
        Extension("pyatomic", ["pyatomic.c"])
    ]
)