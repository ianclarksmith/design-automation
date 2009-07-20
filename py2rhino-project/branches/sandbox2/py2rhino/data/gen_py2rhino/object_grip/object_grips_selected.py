object_grips_selected = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "object_grips_selected",

    "doc_html": """
        Verifies that an object's grips are turned on and at least one grip is selected.
    """,

    "syntax_html": """
        Rhino.ObjectGripsSelected (strObject)
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

    "id_com": 498,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

