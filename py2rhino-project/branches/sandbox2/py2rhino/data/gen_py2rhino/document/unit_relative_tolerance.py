unit_relative_tolerance = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "unit_relative_tolerance",

    "doc_html": """
        Returns or sets the document's relative tolerance parameter.  Relative tolerance is measured in percent. See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": """
        Rhino.UnitRelativeTolerance ([dblRelTol])
    """,

    "params_html": {
        0: {
            "name": "RelTol",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The relative tolerance in percent.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblRelTol is not specified, the current relative tolerance if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblRelTol is specified, the previous relative tolerance if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 329,

    "params_com": {
        0: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

