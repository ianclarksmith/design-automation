make_curve_non_periodic = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "MakeCurveNonPeriodic",
    "output_package_name": "curve",
    "output_module_name": "make_curve_non_periodic",

    "doc_html": """
        Makes a periodic curve non-periodic.  Non-periodic curves can develop kinks when deformed.
    """,

    "syntax_html": {
        0: ("strObject", "blnDelete"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "blnDelete",
            "py_name": "delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete input curve.  If omitted, the input curve will not be deleted (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If blnDelete is False, the identifier of the new object if successful."
        },
        1: {
            "type": "string",
            "doc": "If blnDelete is True, the identifier of the modified object if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 925,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

