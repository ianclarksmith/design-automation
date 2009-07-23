a_sin = {
    "input_folder_name": "Math_Methods",
    "input_file_name": "ASin",
    "output_package_name": "math",
    "output_module_name": "a_sin",

    "doc_html": """
        Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is number. The returned angle is given in radians in the range -PI/2 to PI/2.
    """,

    "syntax_html": {
        0: ("dblNumber"),
    },

    "params_html": {
        0: {
            "name": "dblNumber",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Number",
            "doc": """
        A number representing the sine of the angle you want and must be from -1 to 1.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "An angle, ?, measured in radians, if successful. Note, A positive return value represents a counterclockwise angle from the x-axis; a negative return value represents a clockwise angle. Use ToDegrees to convert from radians to degrees."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 756,

    "params_com": {
        0: {
            "name": "vx",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

