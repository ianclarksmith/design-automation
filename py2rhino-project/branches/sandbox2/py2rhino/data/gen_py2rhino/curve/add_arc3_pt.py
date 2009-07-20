add_arc3_pt = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "add_arc3_pt",

    "doc_html": """
        Adds a 3-point arc curve to the document.
    """,

    "syntax_html": """
        Rhino.AddArc3Pt (arrStart, arrEnd, arrPoint)
    """,

    "params_html": {
        0: {
            "name": "Start",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The starting point of the arc.
            """
        },
        1: {
            "name": "End",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The ending point of the arc.
            """
        },
        2: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A point on the arc.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 82,

    "params_com": {
        0: {
            "name": "vaPt1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPt2",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPt3",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

