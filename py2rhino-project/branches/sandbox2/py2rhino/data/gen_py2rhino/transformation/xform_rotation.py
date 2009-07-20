xform_rotation = {
    "module_name": "transformation",
    "class_name": "Transformation",
    "method_name": "xform_rotation",

    "doc_html": """
        Returns a rotation transformation matrix. The XformRotation provides several ways to compute a rotation transformation.  A positive rotation angle indicates a counter-clockwise (right hand rule) rotation about the axis of rotation.
    """,

    "syntax_html": """
        Rhino.XformRotation (arrPlane1, arrPlane2)
    """,

    "params_html": {
        0: {
            "name": "Plane1",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "type_string": "arr",
            "doc": """
        The starting plane.
            """
        },
        1: {
            "name": "Plane2",
            "opt_or_req": "Required",
            "type": "Array (Plane)",
            "type_string": "arr",
            "doc": """
        The ending plane.
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
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The rotation axis.
            """
        },
        4: {
            "name": "StartDir",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The starting direction.
            """
        },
        5: {
            "name": "EndDir",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The ending direction.
            """
        },
        6: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array (3-D Point)",
            "type_string": "arr",
            "doc": """
        The rotation center point.
            """
        },
        7: {
            "name": "X0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The initial frame X
            """
        },
        8: {
            "name": "Y0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The initial frame Y.
            """
        },
        9: {
            "name": "Z0",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The initial frame Z.
            """
        },
        10: {
            "name": "X1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The final frame X.
            """
        },
        11: {
            "name": "Y1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The final frame Y.
            """
        },
        12: {
            "name": "Z1",
            "opt_or_req": "Required",
            "type": "Array (3-D Vector)",
            "type_string": "arr",
            "doc": """
        The final frame Z.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "The 4x4 transformation matrix."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 794,

    "params_com": {
        0: {
            "name": "va0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "va1",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "va2",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "va3",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "va4",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        5: {
            "name": "va5",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

