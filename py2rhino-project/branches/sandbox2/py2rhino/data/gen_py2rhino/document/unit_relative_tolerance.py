unit_relative_tolerance = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitRelativeTolerance",
    "output_package_name": "document",
    "output_module_name": "unit_relative_tolerance",

    "doc_html": """
        Returns or sets the document's relative tolerance parameter.  Relative tolerance is measured in percent. See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": {
        0: ("dblRelTol"),
    },

    "params_html": {
        0: {
            "name": "dblRelTol",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "RelTol",
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

