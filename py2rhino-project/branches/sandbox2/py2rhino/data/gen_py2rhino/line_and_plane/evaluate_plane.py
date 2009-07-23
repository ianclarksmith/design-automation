evaluate_plane = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "EvaluatePlane",
    "output_package_name": "line_and_plane",
    "output_module_name": "evaluate_plane",

    "doc_html": """
        Evaluates a plane at a U,V parameter.
    """,

    "syntax_html": {
        0: ("arrPlane", "arrParameter"),
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
            "name": "arrParameter",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Parameter",
            "doc": """
        An array containing the U,V parameter to evaluate.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 3-D point if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 751,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParameter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

