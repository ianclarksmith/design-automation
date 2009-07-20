unselect_object_grips = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "unselect_object_grips",

    "doc_html": """
        Unselects an object's grips. Note, the grips will not be turned off.
    """,

    "syntax_html": """
        Rhino.UnselectObjectGrips (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of grips unselected if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 502,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

