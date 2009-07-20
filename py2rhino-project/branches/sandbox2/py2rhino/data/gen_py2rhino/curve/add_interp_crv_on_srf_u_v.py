add_interp_crv_on_srf_u_v = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "add_interp_crv_on_srf_u_v",

    "doc_html": """
        Adds an interpolated curve object. based on surface parameters, that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.
    """,

    "syntax_html": """
        Rhino.AddInterpCrvOnSrfUV (strObject, arrPoints)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The surface object's identifier.
            """
        },
        1: {
            "name": "Points",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of 2-D surface parameters. The array must contain at least two sets of surface parameters.
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

    "id_com": 641,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoints",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

