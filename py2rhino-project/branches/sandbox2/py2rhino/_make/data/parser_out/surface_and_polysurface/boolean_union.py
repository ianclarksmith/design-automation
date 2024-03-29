boolean_union = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "BooleanUnion",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "boolean_union",

    "doc_html": """
        Performs a Boolean union operation on a set of input surfaces and polysurfaces. For more details, see the BooleanUnion command in the Rhino help file.
    """,

    "syntax_html": {
        0: ("arrInput", "blnDelete"),
    },

    "params_html": {
        0: {
            "name": "arrInput",
            "py_name": "input",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Input",
            "doc": """
        The identifiers of the surfaces or polysurfaces to union.
            """
        },
        1: {
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

    "id_com": 506,

    "params_com": {
        0: {
            "name": "vaObjects",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDelete",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

