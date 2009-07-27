line_transform = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "LineTransform",
    "output_package_name": "line_and_plane",
    "output_module_name": "line_transform",

    "doc_html": """
        Transforms a line.
    """,

    "syntax_html": {
        0: ("arrLine", "arrXform"),
    },

    "params_html": {
        0: {
            "name": "arrLine",
            "py_name": "line",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Line",
            "doc": """
        Two 3-D points identifying the starting and ending points of the line.
            """
        },
        1: {
            "name": "arrXform",
            "py_name": "xform",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Xform",
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

