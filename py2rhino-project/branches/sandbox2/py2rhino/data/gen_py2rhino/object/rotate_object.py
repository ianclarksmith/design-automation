rotate_object = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "rotate_object",

    "doc_html": """
        Rotates a single object. Rotation is based on the active construction plane.
    """,

    "syntax_html": """
        Rhino.RotateObject (strObject, arrPoint, dblAngle [, arrAxis [, blnCopy]])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object to rotate.
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D center point of the rotation.
            """
        },
        2: {
            "name": "Angle",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The rotation angle in degrees.
            """
        },
        3: {
            "name": "Axis",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D vector that identifies the axis of rotation. If omitted, the Z axis of the active construction plane is used as the rotation axis.
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
            "doc": "The identifier of the rotated object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 392,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAngle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaAxis",
            "opt_or_req": "Optional",
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

