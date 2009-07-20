enable_object_grips = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "enable_object_grips",

    "doc_html": """
        Enables or disables an object's grips. For curves and surfaces, these are also called control points.
    """,

    "syntax_html": """
        Rhino.EnableObjectGrips (strObject [, blnEnable])
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
        1: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True (default), the specified object's grips will be turned on. Otherwise, they will be turned off.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True of False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 499,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaEnable",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

