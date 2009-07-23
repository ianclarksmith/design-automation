text_object_plane = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "TextObjectPlane",
    "output_package_name": "geometry",
    "output_module_name": "text_object_plane",

    "doc_html": """
        Returns or modifies the plane used by a text object.
    """,

    "syntax_html": {
        0: ("strObject", "arrPlane"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "arrPlane",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        The new construction plane.  The elements of a plane array are as follows:
		Value
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
            "doc": "If a plane is not specified, the current plane if successful."
        },
        1: {
            "type": "array",
            "doc": "If a plane is specified, the previous plane if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 476,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPlane",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

