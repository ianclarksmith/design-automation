shear_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ShearObjects",
    "output_package_name": "object",
    "output_module_name": "shear_objects",

    "doc_html": """
        Performs a shear transformation on one or more objects. Transformation is based on the active construction plane.
    """,

    "syntax_html": """
        Rhino.ShearObjects (arrObjects, arrOrigin, arrRefPt, dblAngle [, blnCopy])
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_str",
            "doc": """
        An array of strings identifying the objects to shear.
            """
        },
        1: {
            "name": "Origin",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The origin of the shear transformation.
            """
        },
        2: {
            "name": "RefPt",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr_of_dbl",
            "doc": """
        The reference point of the shear transformation.
            """
        },
        3: {
            "name": "Scale",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "arr_of_int",
            "doc": """
        An angle in degrees of the shear transformation, where -90.0 <= angle <= 90.0.
            """
        },
        4: {
            "name": "Copy",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
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

