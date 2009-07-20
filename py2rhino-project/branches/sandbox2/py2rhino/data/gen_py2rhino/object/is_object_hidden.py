is_object_hidden = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "is_object_hidden",

    "doc_html": """
        Verifies that an object is hidden.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    """,

    "syntax_html": """
        Rhino.IsObjectHidden (strObject)
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

    "id_com": 47,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

