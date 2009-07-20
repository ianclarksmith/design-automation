add_ellipse3_pt = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "add_ellipse3_pt",

    "doc_html": """
        Adds a 3 point elliptical curve to the document.
    """,

    "syntax_html": """
        Rhino.AddEllipse3Pt (arrCenter, arrSecond, arrThird)
    """,

    "params_html": {
        0: {
            "name": "Center",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The center point of the ellipse.
            """
        },
        1: {
            "name": "Second",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The end point of the X-axis.
            """
        },
        2: {
            "name": "Third",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The end point of the Y-axis.
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

    "id_com": 680,

    "params_com": {
        0: {
            "name": "vaCenter",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSecond",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaThird",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

