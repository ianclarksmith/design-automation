add_point = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "AddPoint",
    "output_package_name": "geometry",
    "output_module_name": "add_point",

    "doc_html": """
        Adds a point object to the document.
    """,

    "syntax_html": {
        0: ("arrPoint"),
    },

    "params_html": {
        0: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 68,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

