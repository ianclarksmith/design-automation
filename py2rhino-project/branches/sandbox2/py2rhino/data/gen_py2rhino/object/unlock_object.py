unlock_object = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "unlock_object",

    "doc_html": """
        Unlocks a previously locked object.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    """,

    "syntax_html": """
        Rhino.UnlockObject (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to unlock.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or false indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 202,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

