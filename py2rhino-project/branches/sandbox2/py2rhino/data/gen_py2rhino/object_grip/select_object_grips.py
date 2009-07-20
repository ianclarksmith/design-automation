select_object_grips = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "select_object_grips",

    "doc_html": """
        Selects an object's grips. If the object's grips are not turned on, they will not be selected.
    """,

    "syntax_html": """
        Rhino.SelectObjectGrips (strObject)
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
            "doc": "The number of grips selected if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 501,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

