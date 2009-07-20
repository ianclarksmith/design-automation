next_object_grip = {
    "module_name": "object_grip",
    "class_name": "ObjectGrip",
    "method_name": "next_object_grip",

    "doc_html": """
        Returns the next grip index from a specified grip index of an object.
    """,

    "syntax_html": """
        Rhino.NextObjectGrip (strObject, intIndex [, intDirection [, blnSelect]])
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
        1: {
            "name": "Index",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The zero-based grip index from which to get the next grip index.
            """
        },
        2: {
            "name": "Direction",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The direction to get the next grip index, either 0=U or 1=V. The default value is 0. Note, this argument only applies when dealing with surfaces.
            """
        },
        3: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True (default), the next grip index found will be selected. Otherwise, it will not be selected.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The index of the next grip from the specified grip index."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 558,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDir",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

