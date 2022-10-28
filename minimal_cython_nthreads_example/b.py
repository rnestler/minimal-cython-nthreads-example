from minimal_cython_nthreads_example.a import fun_a

def fun_b(params: list[float]) -> float:
    params.append(1.0)
    return fun_a(params)
