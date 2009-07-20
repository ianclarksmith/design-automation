is_object_reference = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "is_object_reference",

    "doc_html": """
        Verifies that an object is a reference object.  Reference objects are object that are not part of the current document.
    """,

    "syntax_html": """
        Rhino.IsObjectReference (strObject)
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

    "id_com": 271,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

