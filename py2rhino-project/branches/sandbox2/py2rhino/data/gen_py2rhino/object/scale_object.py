scale_object = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "scale_object",

    "doc_html": """
        Scales a single object. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.
    """,

    "syntax_html": """
        Rhino.ScaleObject (strObject, arrOrigin, arrScale [, blnCopy])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to scale.
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
        Copy the object. If omitted, the object will not be copied (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the scaled object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 585,

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

