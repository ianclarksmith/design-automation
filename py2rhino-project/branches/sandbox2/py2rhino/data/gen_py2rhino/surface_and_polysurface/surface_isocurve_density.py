surface_isocurve_density = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "SurfaceIsocurveDensity",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "surface_isocurve_density",

    "doc_html": """
        Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve is a curve of constant U or V value on a surface. Rhino uses isocurves and surface edge curves to visualize the shape of a NURBS surface.
    """,

    "syntax_html": """
        Rhino.SurfaceIsocurveDensity (strObject [, intDensity])
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
            "name": "Density",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The isocurve wireframe density.  The possible values are as follows:
		Value
		Description
		-1
		Hides surface isocurves.
		0
		Display boundary and knot wires.
		1
		Display boundary and knot wires and one interior wire if there are no interior knots.
		>= 2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The intDensity is not specified, then the current isocurve density if successful."
        },
        1: {
            "type": "number",
            "doc": "The intDensity is specified, then the previous isocurve density if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 361,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDensity",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

