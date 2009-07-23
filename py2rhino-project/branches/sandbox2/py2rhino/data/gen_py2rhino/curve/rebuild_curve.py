rebuild_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "RebuildCurve",
    "output_package_name": "curve",
    "output_module_name": "rebuild_curve",

    "doc_html": """
        Rebuilds a curve to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.
    """,

    "syntax_html": {
        0: ("strObject", "intDegree", "intPointCount"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The object's identifier.
            """
        },
        1: {
            "name": "intDegree",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Degree",
            "doc": """
        The new degree, which must be greater than 1. The default is 3.
            """
        },
        2: {
            "name": "intPointCount",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "PointCount",
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

