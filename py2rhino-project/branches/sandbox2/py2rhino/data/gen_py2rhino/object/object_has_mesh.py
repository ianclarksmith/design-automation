object_has_mesh = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "object_has_mesh",

    "doc_html": """
        Verifies that an object has custom render mesh parameters.
    """,

    "syntax_html": """
        Rhino.ObjectHasMesh (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "Object",
            "type_string": "str",
            "doc": """
        The identifier of a meshable object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True of the object has custom render mesh parameters, False otherwise."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 867,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

