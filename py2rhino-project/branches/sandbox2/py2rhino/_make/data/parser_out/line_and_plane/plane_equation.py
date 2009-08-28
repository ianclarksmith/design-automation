plane_equation = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "PlaneEquation",
    "output_package_name": "line_and_plane",
    "output_module_name": "plane_equation",

    "doc_html": """
        Returns the equation of  a plane. The standard equation of a plane with a non-zero normal vector is as follows:
		Ax + By + Cz + D = 0
    """,

    "syntax_html": {
        0: ("arrPlane"),
    },

    "params_html": {
        0: {
            "name": "arrPlane",
            "py_name": "plane",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Plane",
            "doc": """
        The plane. The elements of a plane array are as follows:
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
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing four numbers that represent the coefficients of the equation, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 642,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

