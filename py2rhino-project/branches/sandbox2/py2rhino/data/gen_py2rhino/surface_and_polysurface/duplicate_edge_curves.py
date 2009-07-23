duplicate_edge_curves = {
    "input_folder_name": "Surface_and_Polysurface_Methods",
    "input_file_name": "DuplicateEdgeCurves",
    "output_package_name": "surface_and_polysurface",
    "output_module_name": "duplicate_edge_curves",

    "doc_html": """
        Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help file for information on the DupEdge command.
    """,

    "syntax_html": {
        0: ("strObject", "blnSelect"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the surface or polysurface object.
            """
        },
        1: {
            "name": "blnSelect",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Select",
            "doc": """
        Select the duplicated edge curves.  The default is not to select (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the newly created curve objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 657,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

