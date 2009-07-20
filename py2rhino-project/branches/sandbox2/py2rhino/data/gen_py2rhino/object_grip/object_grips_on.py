object_grips_on = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "object_grips_on",

    "doc_html": """
        Verifies that an object's grips are turned on.
    """,

    "syntax_html": """
        Rhino.ObjectGripsOn (strObject)
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
            "type": "boolean",
            "doc": "True of False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 497,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

