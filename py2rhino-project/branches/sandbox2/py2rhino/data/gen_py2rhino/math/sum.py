sum = {
    "module_name": "math",
    "class_name": "Math",
    "method_name": "sum",

    "doc_html": """
        Returns the sum of an array of numbers.
    """,

    "syntax_html": """
        Rhino.Sum (arrNumbers)
    """,

    "params_html": {
        0: {
            "name": "Numbers",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of numbers to sum.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The sum of the array if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 770,

    "params_com": {
        0: {
            "name": "var",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

