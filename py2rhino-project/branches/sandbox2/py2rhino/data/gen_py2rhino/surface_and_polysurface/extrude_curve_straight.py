extrude_curve_straight = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExtrudeCurveStraight",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "extrude_curve_straight",

    "doc_html": """
        Creates a surface by extruding a curve straight along two points that define a line.
    """,

    "syntax_html": """
        Rhino.ExtrudeCurveStraight (strCurve, arrStartPoint, arrEndPoint)
    """,

    "params_html": {
        0: {
            "name": "Curve",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the curve object to extrude.
            """
        },
        1: {
            "name": "StartPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A starting point.
            """
        },
        2: {
            "name": "EndPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A ending point.
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

    "id_com": 539,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaStart",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaEnd",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

