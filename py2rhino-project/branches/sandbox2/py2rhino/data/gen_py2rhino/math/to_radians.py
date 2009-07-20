to_radians = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "ToRadians",
    "output_package_name": "math",
    "output_module_name": "to_radians",

    "doc_html": """
        Converts an angle specified in degrees to radians.
    """,

    "syntax_html": """
        Rhino.ToRadians (dblDegrees)
    """,

    "params_html": {
        0: {
            "name": "Degrees",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The angle in degrees
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The angle in radians if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 665,

    "params_com": {
        0: {
            "name": "vaDegrees",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

