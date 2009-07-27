unit_angle_tolerance = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitAngleTolerance",
    "output_package_name": "document",
    "output_module_name": "unit_angle_tolerance",

    "doc_html": """
        Returns or sets the document's angle tolerance parameter.  Angle tolerance is measured degrees.  See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": {
        0: ("dblAngleTol"),
    },

    "params_html": {
        0: {
            "name": "dblAngleTol",
            "py_name": "angle_tol",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "AngleTol",
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

