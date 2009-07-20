extrude_curve_tapered = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "ExtrudeCurveTapered",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "extrude_curve_tapered",

    "doc_html": """
        Creates a surface by extruding a curve to a taper. Unlike Lofts and Sweeps, the initial orientation of the profile curve is maintained through the extrusion.
    """,

    "syntax_html": """
        Rhino.ExtrudeCurveTapered (strCurve, dblDistance, arrDirection, arrBasePoint, dblAngle [, intCornerType])
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
            "name": "Distance",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The extrusion distance.
            """
        },
        2: {
            "name": "Direction",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D vector that specifies the extrusion direction.
            """
        },
        3: {
            "name": "BasePoint",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D point that specifies the base point of the extrusion.
            """
        },
        4: {
            "name": "Angle",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The angle of the extrusion.
            """
        },
        5: {
            "name": "CornerType",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
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

