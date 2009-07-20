add_sub_crv = {
    "module_name": "curve",
    "class_name": "Curve",
    "method_name": "add_sub_crv",

    "doc_html": """
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    """,

    "syntax_html": """
        Rhino.AddSubCrv (strObject, dblParam0, dblParam1)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of a closed, planar curve object.
            """
        },
        1: {
            "name": "Param0",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The first parameter on the source curve.
            """
        },
        2: {
            "name": "Param1",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The second parameter on the source curve.
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

    "id_com": 681,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParam0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaParam1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

