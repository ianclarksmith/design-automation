shear_object = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ShearObject",
    "output_package_name": "object",
    "output_module_name": "shear_object",

    "doc_html": """
        Performs a shear transformation on a single object. Transformation is based on the active construction plane.
    """,

    "syntax_html": """
        Rhino.ShearObject (strObject, arrOrigin, arrRefPt, dblAngle [, blnCopy])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to shear.
            """
        },
        1: {
            "name": "Origin",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The origin of the shear transformation.
            """
        },
        2: {
            "name": "RefPt",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The reference point of the shear transformation.
            """
        },
        3: {
            "name": "Scale",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "arr",
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
        Copy the object. If omitted, the object will not be copied (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the sheared object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 587,

    "params_com": {
        0: {
            "name": "vaObject",
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

