is_object_locked = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "is_object_locked",

    "doc_html": """
        Verifies that an object is locked.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    """,

    "syntax_html": """
        Rhino.IsObjectLocked (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 48,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

