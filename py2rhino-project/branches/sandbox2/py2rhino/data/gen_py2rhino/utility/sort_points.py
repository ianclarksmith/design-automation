sort_points = {
    "module_name": "utility",
    "class_name": "Utility",
    "method_name": "sort_points",

    "doc_html": """
        Sorts an array of 3-D points.
    """,

    "syntax_html": """
        Rhino.SortPoints (arrPoints [, blnAscending [, blnOrder]])
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
            "name": "Ascending",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The sorting mode, either ascending or descending.  If omitted, the points are sorted ascending (True).
            """
        },
        2: {
            "name": "Order",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "bln",
            "doc": """
        The component sort order, where:
		Value
		Component Sort Order
		0 (default)
		X, Y, Z
		1
		X, Z, Y
		2
		Y, X, Z
		3
		Y, Z, X
		4
		Z, X, Y
		5
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of sorted 3-D points if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 551,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaAscending",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaOrder",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

