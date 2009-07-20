rebuild_curve = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "rebuild_curve",

    "doc_html": """
        Rebuilds a curve to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.
    """,

    "syntax_html": """
        Rhino.RebuildCurve (strObject [, intDegree [, intPointCount]])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "Degree",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The new degree, which must be greater than 1. The default is 3.
            """
        },
        2: {
            "name": "PointCount",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The new point count, which must be bigger than the intDegree.  With closed curves, the minimum point count is 3.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 814,

    "params_com": {
        0: {
            "name": "vaCrv",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDegree",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPointCount",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

