add_text_dot = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "AddTextDot",
    "output_package_name": "geometry",
    "output_module_name": "add_text_dot",

    "doc_html": """
        Adds an annotation text dot to the document.
    """,

    "syntax_html": """
        Rhino.AddTextDot (strText, arrPoint)
    """,

    "params_html": {
        0: {
            "name": "Test",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        A character or text string.
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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

