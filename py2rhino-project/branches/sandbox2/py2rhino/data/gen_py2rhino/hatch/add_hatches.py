add_hatches = {
    "input_folder_name": "Hatch_Methods",
    "input_file_name": "AddHatches",
    "output_package_name": "hatch",
    "output_module_name": "add_hatches",

    "doc_html": """
        Creates one or more new hatch objects from an array of closed planar curve objects.
    """,

    "syntax_html": """
        Rhino.AddHatches (arrCurves [, strHatch [, dblScale [, dblRotation]]])
    """,

    "params_html": {
        0: {
            "name": "Curves",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_str",
            "doc": """
        An array of strings that identify one or more closed planar curves that defines the boundaries of the hatch objects.
            """
        },
        1: {
            "name": "Hatch",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the hatch pattern to be used by the hatch object.  If omitted, the current hatch pattern will be used.
            """
        },
        2: {
            "name": "Scale",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The hatch pattern scale factor.  If omitted, a scale factor of 1.0 will be used.
            """
        },
        3: {
            "name": "Rotation",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The hatch pattern rotation angle in degrees.  If omitted, a rotation angle of 0.0 degrees will be used.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The identifiers of the newly created hatch objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 836,

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

