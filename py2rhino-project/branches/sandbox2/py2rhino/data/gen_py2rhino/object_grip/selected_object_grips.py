selected_object_grips = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "selected_object_grips",

    "doc_html": """
        Returns an array of grip indices identifying an object's selected grips.
    """,

    "syntax_html": """
        Rhino.SelectedObjectGrips (strObject)
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
            "type": "array",
            "doc": "An array of zero-based grip indices identifying the selected grips."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 560,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

