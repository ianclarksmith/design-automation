line_plane = {
    "module_name": "line_and_plane",
    "class_name": "LineAndPlane",
    "method_name": "line_plane",

    "doc_html": """
        Returns a plane that contains the line.  The origin of the plane is at the start of the line.  If possible, a plane parallel to the world XY, YZ or ZX plane is returned.
    """,

    "syntax_html": """
        Rhino.LinePlane (arrLine)
    """,

    "params_html": {
        0: {
            "name": "Line",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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

