import multiprocessing
from distutils.command.build_ext import build_ext

from setuptools import Extension

from Cython.Build import cythonize


def build(setup_kwargs):
    setup_kwargs.update(
        {
            "ext_modules": cythonize(
                module_list=[
                    Extension(
                        "*",
                        ["minimal_cython_nthreads_example/*.py"],
                        define_macros=[("CYTHON_TRACE", "1")],
                    )
                ],
                language_level=3,
                nthreads=multiprocessing.cpu_count(),
                compiler_directives={
                    "linetrace": True,
                    # We don't have correct enough type information to enable this.
                    "annotation_typing": False,
                },
            ),
            "cmdclass": {"build_ext": build_ext},
        }
    )
