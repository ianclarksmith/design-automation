unit_absolute_tolerance = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitAbsoluteTolerance",
    "output_package_name": "document",
    "output_module_name": "unit_absolute_tolerance",

    "doc_html": """
        Returns or sets the document's absolute tolerance parameter.  Absolute tolerance is measured in drawing units. See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": """
        Rhino.UnitAbsoluteTolerance ([dblAbsTol])
    """,

    "params_html": {
        0: {
            "name": "AbsTol",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The absolute tolerance in drawing units.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblAbsTol is not specified, the current absolute tolerance if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblAbsTol is specified, the previous absolute tolerance if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 324,

    "params_com": {
        0: {
            "name": "vaTol",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

