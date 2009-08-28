add_sub_crv = {
    "input_folder_name": "Curve_Methods",
    "input_file_name": "AddSubCrv",
    "output_package_name": "curve",
    "output_module_name": "add_sub_crv",

    "doc_html": """
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    """,

    "syntax_html": {
        0: ("strObject", "dblParam0", "dblParam1"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of a closed, planar curve object.
            """
        },
        1: {
            "name": "dblParam0",
            "py_name": "param_0",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Param0",
            "doc": """
        The first parameter on the source curve.
            """
        },
        2: {
            "name": "dblParam1",
            "py_name": "param_1",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Param1",
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

