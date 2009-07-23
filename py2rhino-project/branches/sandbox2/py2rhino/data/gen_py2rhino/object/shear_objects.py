shear_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ShearObjects",
    "output_package_name": "object",
    "output_module_name": "shear_objects",

    "doc_html": """
        Performs a shear transformation on one or more objects. Transformation is based on the active construction plane.
    """,

    "syntax_html": {
        0: ("arrObjects", "arrOrigin", "arrRefPt", "dblAngle", "blnCopy"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to shear.
            """
        },
        1: {
            "name": "arrOrigin",
            "py_name": "origin",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Origin",
            "doc": """
        The origin of the shear transformation.
            """
        },
        2: {
            "name": "arrRefPt",
            "py_name": "ref_pt",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "RefPt",
            "doc": """
        The reference point of the shear transformation.
            """
        },
        3: {
            "name": "arrScale",
            "py_name": "scale",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "arr_of_int",
            "name_main": "Scale",
            "doc": """
        An angle in degrees of the shear transformation, where -90.0 <= angle <= 90.0.
            """
        },
        4: {
            "name": "blnCopy",
            "py_name": "copy",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Copy",
            "doc": """
        Copy the objects. If omitted, the objects will not be copied (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the scaled objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 588,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaOrigin",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaRefPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaDegrees",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaCopy",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

