unit_angle_tolerance = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "unit_angle_tolerance",

    "doc_html": """
        Returns or sets the document's angle tolerance parameter.  Angle tolerance is measured degrees.  See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": """
        Rhino.UnitAngleTolerance ([dblAngleTol])
    """,

    "params_html": {
        0: {
            "name": "AngleTol",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The angle tolerance in degrees.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblAngleTol is not specified, the current angle tolerance if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblAngleTol is specified, the previous angle tolerance if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 325,

    "params_com": {
        0: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

