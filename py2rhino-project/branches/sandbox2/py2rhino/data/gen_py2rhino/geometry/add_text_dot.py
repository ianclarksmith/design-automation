add_text_dot = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "AddTextDot",
    "output_package_name": "geometry",
    "output_module_name": "add_text_dot",

    "doc_html": """
        Adds an annotation text dot to the document.
    """,

    "syntax_html": {
        0: ("strText", "arrPoint"),
    },

    "params_html": {
        0: {
            "name": "strTest",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Test",
            "doc": """
        A character or text string.
            """
        },
        1: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point identifying the origin point.
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

    "id_com": 320,

    "params_com": {
        0: {
            "name": "vaText",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

