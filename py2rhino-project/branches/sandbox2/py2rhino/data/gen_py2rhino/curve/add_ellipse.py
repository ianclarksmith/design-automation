add_ellipse = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddEllipse",
    "output_package_name": "curve",
    "output_module_name": "add_ellipse",

    "doc_html": """
        Adds an elliptical curve to the document.
    """,

    "syntax_html": """
        Rhino.AddEllipse (arrPlane, dblXRadius, dblYRadius)
    """,

    "params_html": {
        0: {
            "name": "Plane",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The plane on which the ellipse will lie. The origin of the plane will be the center point of the ellipse.
            """
        },
        1: {
            "name": "XRadius",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The radius in the X-axis direction.
            """
        },
        2: {
            "name": "YRadius",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The radius in the Y-axis direction.
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

    "id_com": 679,

    "params_com": {
        0: {
            "name": "vaPlane",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDX",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDY",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

