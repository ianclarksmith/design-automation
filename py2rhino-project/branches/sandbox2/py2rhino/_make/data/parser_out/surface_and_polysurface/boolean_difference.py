boolean_difference = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "BooleanDifference",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "boolean_difference",

    "doc_html": """
        Performs a Boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file.
    """,

    "syntax_html": {
        0: ("arrInput0", "arrInput1", "blnDelete"),
    },

    "params_html": {
        0: {
            "name": "arrInput0",
            "py_name": "input_0",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Input0",
            "doc": """
        The identifiers of the surfaces or polysurfaces to subtract from.
            """
        },
        1: {
            "name": "arrInput1",
            "py_name": "input_1",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Input1",
            "doc": """
        The identifiers of the surfaces or polysurfaces to be subtracted.
            """
        },
        2: {
            "name": "blnDelete",
            "py_name": "delete",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Delete",
            "doc": """
        Delete all input objects. The default is to delete all input objects (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array containing the identifiers of the newly created objects, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 508,

    "params_com": {
        0: {
            "name": "vaInBreps0",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaInBreps1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

