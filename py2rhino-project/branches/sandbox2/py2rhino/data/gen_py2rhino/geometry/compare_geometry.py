compare_geometry = {
    "module_name": "geometry",
    "class_name": "Geometry",
    "method_name": "compare_geometry",

    "doc_html": """
        Compares two objects to determine if they are geometrically identical.
    """,

    "syntax_html": """
        Rhino.CompareGeometry (strObject1, strObject2)
    """,

    "params_html": {
        0: {
            "name": "Object1",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the first object to compare.
            """
        },
        1: {
            "name": "Object2",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the second object to compare.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if the objects are geometrically identical, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 598,

    "params_com": {
        0: {
            "name": "vaObj1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaObj2",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

