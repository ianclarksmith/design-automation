join_curves = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "join_curves",

    "doc_html": """
        Joins two or more curve object together to form one or more curves or polycurves.
    """,

    "syntax_html": """
        Rhino.JoinCurves (arrObjects [,blnDelete])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "str",
            "doc": """
        An array of strings identifying the curve objects to join.
            """
        },
        1: {
            "name": "Delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

