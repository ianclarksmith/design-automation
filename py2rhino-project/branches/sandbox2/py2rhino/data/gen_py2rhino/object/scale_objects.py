scale_objects = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ScaleObjects",
    "output_package_name": "object",
    "output_module_name": "scale_objects",

    "doc_html": """
        Scales one or more objects. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.
    """,

    "syntax_html": """
        Rhino.ScaleObjects (arrObjects, arrOrigin, arrScale [, blnCopy])
    """,

    "params_html": {
        0: {
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to scale.
            """
        },
        1: {
            "name": "Origin",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The origin of the scale transformation.
            """
        },
        2: {
            "name": "Scale",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of three numbers that identify the X axis, Y axis, and Z axis scale factors to apply. Scaling is based on the active construction plane.
            """
        },
        3: {
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

    "id_com": 586,

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
            "name": "vaScale",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaCopy",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

