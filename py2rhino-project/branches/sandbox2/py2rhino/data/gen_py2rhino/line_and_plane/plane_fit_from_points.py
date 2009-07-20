plane_fit_from_points = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "plane_fit_from_points",

    "doc_html": """
        Returns a plane that was fit through an array of 3-D points.
    """,

    "syntax_html": """
        Rhino.PlaneFitFromPoints (arrPoints)
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points.
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

    "id_com": 725,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

