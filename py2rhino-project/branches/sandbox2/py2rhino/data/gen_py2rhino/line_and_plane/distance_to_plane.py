distance_to_plane = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "DistanceToPlane",
    "output_package_name": "line_and_plane",
    "output_module_name": "distance_to_plane",

    "doc_html": """
        Returns the distance from a 3-D point to a plane.
    """,

    "syntax_html": {
        0: ("arrPlane", "arrPoint"),
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
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        The 3-D point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The distance if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 628,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

