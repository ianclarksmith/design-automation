line_plane = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "LinePlane",
    "output_package_name": "line_and_plane",
    "output_module_name": "line_plane",

    "doc_html": """
        Returns a plane that contains the line.  The origin of the plane is at the start of the line.  If possible, a plane parallel to the world XY, YZ or ZX plane is returned.
    """,

    "syntax_html": {
        0: ("arrLine"),
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
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The plane if successful.  The elements of a plane array are as follows:"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 898,

    "params_com": {
        0: {
            "name": "vaLine",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

