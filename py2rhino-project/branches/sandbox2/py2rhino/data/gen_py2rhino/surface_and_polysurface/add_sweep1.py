add_sweep1 = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddSweep1",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_sweep1",

    "doc_html": """
        Adds a surface created through profile curves that define the surface shape and one curve that defines a surface edge. For more details on this method, see the Rhino help file for the Sweep1 command.
		Note, this method does not perform any curve sorting or direction matching on the input shape curves. This is the responsibility of the script writer.
		For best results:
		* The shape curves should all be oriented in the same direction.
		* The starting point of each shape curve should either intersect with or be close to the rail curve.
		* The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.
    """,

    "syntax_html": """
        Rhino.AddSweep1 (strRail, arrShapes [, arrStartPt [, arrEndPt [, blnClosed [, intStyle [, vaStyleArg [, intSimplify [, vaSimplifyArg]]]]]]])
    """,

    "params_html": {
        0: {
            "name": "Rail",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the rail curve.
            """
        },
        1: {
            "name": "Shapes",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_str",
            "doc": """
        An array of strings identifying one or more shape, or cross section, curves.
            """
        },
        2: {
            "name": "StartPt",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D starting point of the surface.
            """
        },
        3: {
            "name": "EndPt",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The 3-D ending point of the surface.
            """
        },
        4: {
            "name": "Closed",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        If True, then create a closed surface, continuing the surface past the last curve around to the first curve. This option is only available after you select two cross-section curves.  The default value is False.
            """
        },
        5: {
            "name": "Style",
            "opt_or_req": "Optional",
            "type": "Integer",
            "type_string": "int",
            "doc": """
        The sweep style, where 0 = Freeform and 1 = Roadlike. The default value is 0 = Freeform.
            """
        },
        6: {
            "name": "StyleArg",
            "opt_or_req": "Optional",
            "type": "Variant",
            "type_string": "va",
            "doc": """
        If intStyle = 1 (Roadlike), then this argument is a 3-D vector identifying the planar up direction for the sweep.
            """
        },
        7: {
            "name": "Simplify",
            "opt_or_req": "Optional",
            "type": "Integer",
            "type_string": "int",
            "doc": """
        Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild. The default value is 0 = Do Not Simplify.
            """
        },
        8: {
            "name": "SimplifyArg",
            "opt_or_req": "Optional",
            "type": "Variant",
            "type_string": "va",
            "doc": """
        If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance.  If intSimplify = 2 (Rebuild), then this argument is a number specifying the number of control points to rebuild the shape curves.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the new surface objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 893,

    "params_com": {
        0: {
            "name": "vaRail",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaCurves",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaStartPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaEndPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaClosed",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        5: {
            "name": "vaStyle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        6: {
            "name": "vaStyleArg",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        7: {
            "name": "vaSimplify",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        8: {
            "name": "vaSimplifyArg",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

