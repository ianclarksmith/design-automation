object_top_group = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "object_top_group",

    "doc_html": """
        Returns the top most group name that an object is assigned.  This function primarily applies to objects that are members of nested groups.
    """,

    "syntax_html": """
        Rhino.ObjectTopGroup (strObject)
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
            "doc": "The top most group name of the object if successful"
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 197,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

