cull_duplicate_points = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "cull_duplicate_points",

    "doc_html": """
        Removes duplicates from an array of 3-D points.
    """,

    "syntax_html": """
        Rhino.CullDuplicatePoints (arrPoints [, dblTolerance)
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
        1: {
            "name": "Tolerance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The minimum distance between points.  Points that fall within this tolerance will be discarded.  If omitted, Rhino's internal zero tolerance is used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of 3-D points with duplicates removed if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful or on error."
        },
    },

    "id_com": 548,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaTolerance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

