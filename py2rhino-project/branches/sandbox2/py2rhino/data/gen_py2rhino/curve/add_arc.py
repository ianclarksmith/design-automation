add_arc = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddArc",
    "output_package_name": "curve",
    "output_module_name": "add_arc",

    "doc_html": """
        Adds an arc curve to the document.
    """,

    "syntax_html": """
        Rhino.AddArc (arrPlane, dblRadius, dblAngle)
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The plane on which the arc will lie. The origin of the plane will be the center point of the arc. The X-axis of the plane will define the 0 angle direction.
            """
        },
        1: {
            "name": "Radius",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The radius arc.
            """
        },
        2: {
            "name": "Angle",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        A angle or interval, in degrees, of the arc.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the new object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 651,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaRadius",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaAngle",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

