extrude_curve_straight = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExtrudeCurveStraight",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "extrude_curve_straight",

    "doc_html": """
        Creates a surface by extruding a curve straight along two points that define a line.
    """,

    "syntax_html": {
        0: ("strCurve", "arrStartPoint", "arrEndPoint"),
    },

    "params_html": {
        0: {
            "name": "strCurve",
            "py_name": "curve",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve",
            "doc": """
        The identifier of the curve object to extrude.
            """
        },
        1: {
            "name": "arrStartPoint",
            "py_name": "start_point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartPoint",
            "doc": """
        A starting point.
            """
        },
        2: {
            "name": "arrEndPoint",
            "py_name": "end_point",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndPoint",
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

