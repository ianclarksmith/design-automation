unlock_objects = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "unlock_objects",

    "doc_html": """
        Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    """,

    "syntax_html": """
        Rhino.UnlockObjects (arrObjects)
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to unlock.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects unlocked if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 306,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

