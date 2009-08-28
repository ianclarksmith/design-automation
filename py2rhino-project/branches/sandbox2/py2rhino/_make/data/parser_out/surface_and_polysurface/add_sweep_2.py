add_sweep_2 = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "AddSweep2",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "add_sweep_2",

    "doc_html": """
        Adds a surface created through profile curves that define the surface shape and two curves that define the surface edges. For more details on this method, see the Rhino help file for the Sweep2 command.
		Note, this method does not perform any curve sorting or direction matching on the input shape curves. This is the responsibility of the script writer.
		For best results:
		* The shape curves should all be oriented in the same direction.
		* The starting point of each shape curve should either intersect with or be close to the first rail curve.
		* The ending point of each shape curve should either intersect with or be close to the second rail curve.
		* The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.
    """,

    "syntax_html": {
        0: ("arrRails", "arrShapes", "arrStartPt", "arrEndPt", "blnClosed", "blnSimpleSweep", "blnMaintainHeight", "intSimplify", "vaSimplifyArg"),
    },

    "params_html": {
        0: {
            "name": "arrRails",
            "py_name": "rails",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "arr_of_str",
            "name_main": "Rails",
            "doc": """
        An array of strings identifying two rail curves.
            """
        },
        1: {
            "name": "arrShapes",
            "py_name": "shapes",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Shapes",
            "doc": """
        An array of strings identifying one or more shape, or cross section, curves.
            """
        },
        2: {
            "name": "arrStartPt",
            "py_name": "start_pt",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "StartPt",
            "doc": """
        The 3-D starting point of the surface.
            """
        },
        3: {
            "name": "arrEndPt",
            "py_name": "end_pt",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "EndPt",
            "doc": """
        The 3-D ending point of the surface.
            """
        },
        4: {
            "name": "blnClosed",
            "py_name": "closed",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Closed",
            "doc": """
        If True, then create a closed surface, continuing the surface past the last curve around to the first curve. This option is only available after you select two cross-section curves.  The default value is False.
            """
        },
        5: {
            "name": "blnSimpleSweep",
            "py_name": "simple_sweep",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "SimpleSweep",
            "doc": """
        If True, then create surfaces using exact input. This option generates simpler surfaces in cases when the curves are perfectly set up.  The default value is False.
            """
        },
        6: {
            "name": "blnMaintainHeight",
            "py_name": "maintain_height",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "MaintainHeight",
            "doc": """
        By default, shape curves normally scale in both the height and width dimensions. To remove the association between the height scaling from the width scaling, set this value to True.  The default value is False.
            """
        },
        7: {
            "name": "intSimplify",
            "py_name": "simplify",
            "opt_or_req": "Optional",
            "type": "Integer",
            "name_prefix": "int",
            "name_main": "Simplify",
            "doc": """
        Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild. The default value is 0 = Do Not Simplify.
            """
        },
        8: {
            "name": "vaSimplifyArg",
            "py_name": "simplify_arg",
            "opt_or_req": "Optional",
            "type": "Variant",
            "name_prefix": "va",
            "name_main": "SimplifyArg",
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

    "id_com": 894,

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
            "name": "vaSimpleSweep",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        6: {
            "name": "vaSameHeight",
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

