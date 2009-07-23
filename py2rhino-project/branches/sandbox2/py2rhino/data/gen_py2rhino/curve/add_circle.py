add_circle = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddCircle",
    "output_package_name": "curve",
    "output_module_name": "add_circle",

    "doc_html": """
        Adds a circle curve to the document.
    """,

    "syntax_html": {
        0: ("arrPlane", "dblRadius"),
    },

    "params_html": {
        0: {
            "name": "arrPlane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        The plane on which the circle will lie. The origin of the plane will be the center point of the circle.
            """
        },
        1: {
            "name": "dblRadius",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Radius",
            "doc": """
        The radius of the circle.
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

    "id_com": 83,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRadius",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

