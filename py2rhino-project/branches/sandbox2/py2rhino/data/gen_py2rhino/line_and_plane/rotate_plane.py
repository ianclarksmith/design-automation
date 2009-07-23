rotate_plane = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "RotatePlane",
    "output_package_name": "line_and_plane",
    "output_module_name": "rotate_plane",

    "doc_html": """
        Rotates a plane.
    """,

    "syntax_html": {
        0: ("arrPlane", "dblAngle", "arrAxis"),
    },

    "params_html": {
        0: {
            "name": "arrPlane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        The plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
            """
        },
        1: {
            "name": "dblAngle",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Angle",
            "doc": """
        The rotation angle in degrees.
            """
        },
        2: {
            "name": "arrAxis",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Axis",
            "doc": """
        A non-zero 3-D vector identifying the axis of rotation.
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

    "id_com": 630,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDegrees",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

