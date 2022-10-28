# minimal-cython-nthreads-example

Minimal example to show nthreads option of cythonize not working.

To see how only one process at a time is created use:
```
# in a separate terminal
watch -n 0.2 "ps aux|grep cc1"

poetry install
```

In the watch command window one will see 4 cc1 processs appear one after
another instead of in parallel like expected when setting `n_threads`.
