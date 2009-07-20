point_divide = {
    "module_name": "point_and_vector",
    "class_name": "PointAndVector",
    "method_name": "point_divide",

    "doc_html": """
        Divides a 3-D point by a value
    """,

    "syntax_html": """
        Rhino.PointDivide (arrPoint, dblDivide)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D point to divide.
            """
        },
        1: {
            "name": "Scale",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The a non-zero value to divide.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 668,

    "params_com": {
        0: {
            "name": "vaPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDivide",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

