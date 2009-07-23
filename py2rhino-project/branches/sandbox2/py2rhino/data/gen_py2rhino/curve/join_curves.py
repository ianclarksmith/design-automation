join_curves = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "JoinCurves",
    "output_package_name": "curve",
    "output_module_name": "join_curves",

    "doc_html": """
        Joins two or more curve object together to form one or more curves or polycurves.
    """,

    "syntax_html": {
        0: ("arrObjects", "blnDelete"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        An array of strings identifying the curve objects to join.
            """
        },
        1: {
            "name": "blnDelete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete input objects after joining.  The default is not to delete objects (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created curve objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 111,

    "params_com": {
        0: {
            "name": "vaObjects",
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

