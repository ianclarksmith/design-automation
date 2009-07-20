match_object_attributes = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "match_object_attributes",

    "doc_html": """
        Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
    """,

    "syntax_html": """
        Rhino.MatchObjectAttributes (strTarget [, strSource])
    """,

    "params_html": {
        0: {
            "name": "Target",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the target object.
            """
        },
        1: {
            "name": "Targets",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the target objects.
            """
        },
        2: {
            "name": "Source",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the source object.  If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of objects whose attributes were modified if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 781,

    "params_com": {
        0: {
            "name": "vaTarget",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSource",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

