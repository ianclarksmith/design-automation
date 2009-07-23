is_vector_parallel_to = {
    "input_folder_name": "Point_and_Vector_Methods",
    "input_file_name": "IsVectorParallelTo",
    "output_package_name": "point_and_vector",
    "output_module_name": "is_vector_parallel_to",

    "doc_html": """
        Compares two vectors to see if they are parallel.
    """,

    "syntax_html": {
        0: ("arrVector1", "arrVector2"),
    },

    "params_html": {
        0: {
            "name": "arrVector1",
            "py_name": "vector1",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector1",
            "doc": """
        The 3-D vector.
            """
        },
        1: {
            "name": "arrVector2",
            "py_name": "vector2",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Vector2",
            "doc": """
        The 3-D vector to compare to.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The result of the comparison if successful. The possible results are as follows:"
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 660,

    "params_com": {
        0: {
            "name": "vaVec0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaVec1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

