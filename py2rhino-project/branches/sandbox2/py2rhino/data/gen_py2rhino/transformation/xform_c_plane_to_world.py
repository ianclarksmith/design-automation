xform_c_plane_to_world = {
    "input_folder_name": "Transformation_Methods",
    "input_file_name": "XformCPlaneToWorld",
    "output_package_name": "transformation",
    "output_module_name": "xform_c_plane_to_world",

    "doc_html": """
        Transforms a point from construction plane coordinates to world coordinates.
    """,

    "syntax_html": """
        Rhino.XformCPlaneToWorld (arrPoint, arrPlane)
    """,

    "params_html": {
        0: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        A 3-D point in construction plane coordinates.
            """
        },
        1: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The construction plane.  The elements of a plane array are as follows:
		Elemenet
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
            "doc": "A 3-D point in world coordinates if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 131,

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

