xform_world_to_c_plane = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformWorldToCPlane",
    "output_package_name": "transformation",
    "output_module_name": "xform_world_to_c_plane",

    "doc_html": """
        Transforms a point from world coordinates to construction plane coordinates.
    """,

    "syntax_html": {
        0: ("arrPoint", "arrPlane"),
    },

    "params_html": {
        0: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point in world coordinates.
            """
        },
        1: {
            "name": "arrPlane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        The construction plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The construction plane's origin (3-D point).
		1
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Required.  The construction plane's Y axis direction (3-D vector).
		3
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "A 3-D point in construction plane coordinates if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 132,

    "params_com": {
        0: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

