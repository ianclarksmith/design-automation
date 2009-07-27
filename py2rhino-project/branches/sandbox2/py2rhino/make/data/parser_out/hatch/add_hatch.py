add_hatch = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "AddHatch",
    "output_package_name": "hatch",
    "output_module_name": "add_hatch",

    "doc_html": """
        Creates a new hatch object from a closed planar curve object.
    """,

    "syntax_html": {
        0: ("strCurve", "strHatch", "dblScale", "dblRotation"),
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
        The identifier of the closed planar curve that defines the boundary of the hatch object.
            """
        },
        1: {
            "name": "strHatch",
            "py_name": "hatch",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Hatch",
            "doc": """
        The name of the hatch pattern to be used by the hatch object.  If omitted, the current hatch pattern will be used.
            """
        },
        2: {
            "name": "dblScale",
            "py_name": "scale",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Scale",
            "doc": """
        The hatch pattern scale factor.  If omitted, a scale factor of 1.0 will be used.
            """
        },
        3: {
            "name": "dblRotation",
            "py_name": "rotation",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Rotation",
            "doc": """
        The hatch pattern rotation angle in degrees.  If omitted, a rotation angle of 0.0 degrees will be used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the newly created hatch object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 835,

    "params_com": {
        0: {
            "name": "vaCurve",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaHatch",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaScale",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaRotation",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

