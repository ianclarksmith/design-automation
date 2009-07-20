simplify_curve = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "SimplifyCurve",
    "output_package_name": "curve",
    "output_module_name": "simplify_curve",

    "doc_html": """
        Simplify curve replaces the curve with a geometrically equivalent polycurve. The polycurve will have the following properties:
		1.  All the polycurve segments are lines, polylines, arcs, or NURBS curves.
		2.  The NURBS curves segments do not have fully multiple interior knots.
		3.  Rational NURBS curves do not have constant weights.
		4.  Any segment for which IsCurveLinear or IsArc is True is a line, polyline segment, or an arc.
		5.  Adjacent co-linear or co-circular segments are combined.
		6.  Segments that meet with G1-continuity have there ends tuned up so that they meet with G1-continuity to within machine precision.
    """,

    "syntax_html": """
        Rhino.SimplifyCurve (strObject [, intFlags])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The curve object's identifier.
            """
        },
        1: {
            "name": "Flags",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The simplification methods to use. By default, all methods are used (intFlags = 0). The possible options are as follows:
		Value
		Description
		0
		Use all methods.
		1
		Do not split NURBS curves at fully multiple knots.
		2
		Do not replace segments with IsCurveLinear = True with line curves.
		4
		Do not replace segments with IsArc = True with arc curves.
		8
		Do not replace rational NURBS curves with constant denominator with an equivalent non-rational NURBS curve.
		16
		Do not adjust curves at G1-joins.
		32
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

    "id_com": 573,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFlags",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

