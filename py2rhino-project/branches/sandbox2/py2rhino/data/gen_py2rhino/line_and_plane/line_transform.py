line_transform = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "LineTransform",
    "output_package_name": "line_and_plane",
    "output_module_name": "line_transform",

    "doc_html": """
        Transforms a line.
    """,

    "syntax_html": """
        Rhino.LineTransform (arrLine, arrXform)
    """,

    "params_html": {
        0: {
            "name": "Line",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        Two 3-D points identifying the starting and ending points of the line.
            """
        },
        1: {
            "name": "Xform",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        A valid 4x4 transformation matrix.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The resulting line if successful."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 897,

    "params_com": {
        0: {
            "name": "vaLine",
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

