object_description = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "object_description",

    "doc_html": """
        Returns a short text description of an object.
    """,

    "syntax_html": """
        Rhino.ObjectDescription (strObject)
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
            "type": "string",
            "doc": "A short text description of the object is successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 470,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

