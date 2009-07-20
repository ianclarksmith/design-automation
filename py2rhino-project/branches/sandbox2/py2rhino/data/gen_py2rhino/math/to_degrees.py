to_degrees = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "ToDegrees",
    "output_package_name": "math",
    "output_module_name": "to_degrees",

    "doc_html": """
        Converts an angle specified in radians to degrees.
    """,

    "syntax_html": """
        Rhino.ToDegrees (dblRadians)
    """,

    "params_html": {
        0: {
            "name": "Radians",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The angle in radians
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The angle in degrees if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 664,

    "params_com": {
        0: {
            "name": "vaRadians",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

