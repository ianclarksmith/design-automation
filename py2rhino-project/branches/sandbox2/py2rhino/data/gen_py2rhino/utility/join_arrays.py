join_arrays = {
    "input_folder_name": "Utility_Methods",
    "input_file_name": "JoinArrays",
    "output_package_name": "utility",
    "output_module_name": "join_arrays",

    "doc_html": """
        Joins two one-dimensional arrays in to a single one-dimensional array.
    """,

    "syntax_html": """
        Rhino.JoinArrays (arr1, arr2)
    """,

    "params_html": {
        0: {
            "name": "Array1",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The first one-dimensional array.
            """
        },
        1: {
            "name": "Array2",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The second one-dimensional array.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A one-dimensional array containing the elements of both input arrays if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 547,

    "params_com": {
        0: {
            "name": "vaFirst",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSecond",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

