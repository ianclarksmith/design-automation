extrude_curve_tapered = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExtrudeCurveTapered",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "extrude_curve_tapered",

    "doc_html": """
        Creates a surface by extruding a curve to a taper. Unlike Lofts and Sweeps, the initial orientation of the profile curve is maintained through the extrusion.
    """,

    "syntax_html": {
        0: ("strCurve", "dblDistance", "arrDirection", "arrBasePoint", "dblAngle", "intCornerType"),
    },

    "params_html": {
        0: {
            "name": "strCurve",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Curve",
            "doc": """
        The identifier of the curve object to extrude.
            """
        },
        1: {
            "name": "dblDistance",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Distance",
            "doc": """
        The extrusion distance.
            """
        },
        2: {
            "name": "arrDirection",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Direction",
            "doc": """
        A 3-D vector that specifies the extrusion direction.
            """
        },
        3: {
            "name": "arrBasePoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "BasePoint",
            "doc": """
        A 3-D point that specifies the base point of the extrusion.
            """
        },
        4: {
            "name": "dblAngle",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Angle",
            "doc": """
        The angle of the extrusion.
            """
        },
        5: {
            "name": "intCornerType",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "CornerType",
            "doc": """
        The corner type of the extrusion, where:
		Value
		Description
		0 (Default)
		No corner
		1
		Sharp - Offsets and extends curves with a straight line until they intersect.
		2
		Round - Offsets and fillets curves with an arc of radius equal to the offset distance.
		3
		Smooth - Offsets and connects curves with a smooth (G1 continuity) curve.
		4
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created surface objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 914,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDistance",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDirection",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaBase",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaAngle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        5: {
            "name": "vaCornerType",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

