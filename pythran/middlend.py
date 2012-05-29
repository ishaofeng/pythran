'''This module turns a python AST nto an optimized, pythran compatible ast'''
from passes import remove_comprehension, remove_nested_functions, remove_lambdas, normalize_tuples, parallelize_maps, normalize_return, normalize_method_calls

def refine(node):
    """refine node in place until it matches pythran's expectations"""
    # sanitize input
    normalize_method_calls(node)
    normalize_return(node)
    normalize_tuples(node)
    remove_comprehension(node)
    remove_nested_functions(node)
    remove_lambdas(node)

    # some optimizations
    parallelize_maps(node)

