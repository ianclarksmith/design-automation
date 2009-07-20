add_leader = {
    "module_name": "dimension",
    "class_name": "Dimension",
    "method_name": "add_leader",

    "doc_html": """
        Adds an annotation leader to the document. Leader objects are planar. The array of 3-D points passed to this member should be co-planar.
    """,

    "syntax_html": """
        Rhino.AddLeader (arrPoints [, strView [, [strText]])
    """,

    "params_html": {
        0: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 3-D points.  The array must contain at least two points.
            """
        },
        1: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title of the view.  If a view title is specified,  arrPoints will be constrained to the view's construction plane. If a view title is not specified, arrPoints will be constrained to a plane fit through the array of points.
            """
        },
        2: {
            "name": "Text",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The leader's text string.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 321,

    "params_com": {
        0: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaText",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

