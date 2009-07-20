plane_closest_point = {
    "input_folder_name": "Line_and_Plane_Methods",
    "input_file_name": "PlaneClosestPoint",
    "output_package_name": "line_and_plane",
    "output_module_name": "plane_closest_point",

    "doc_html": """
        Returns the point on a plane that is closest to a test point.
    """,

    "syntax_html": """
        Rhino.PlaneClosestPoint (arrPlane, arrPoint [, blnReturnPoint])
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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
        1: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D point to test.
            """
        },
        2: {
            "name": "ReturnPoint",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If omitted or True, then the point on the plane that is closest to the test point is returned. If False, then the parameter of the point on the plane that is closest to the test point is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If blnReturnPoint is omitted or True, then the 3-D point if successful. If blnReturnPoint is False, then an array containing the U,V parameters of the point if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 629,

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
        2: {
            "name": "vaReturnPt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

