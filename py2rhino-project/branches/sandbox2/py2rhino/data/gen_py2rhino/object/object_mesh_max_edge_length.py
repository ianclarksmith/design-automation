object_mesh_max_edge_length = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectMeshMaxEdgeLength",
    "output_package_name": "object",
    "output_module_name": "object_mesh_max_edge_length",

    "doc_html": """
        Returns or modifies an object's custom render mesh parameter's maximum edge length property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("strObject", "dblLength"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "Object",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of an object that has custom render mesh parameters.
            """
        },
        1: {
            "name": "dblLength",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Length",
            "doc": """
        The render mesh maximum edge length.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If dblLength is not specified, the current render mesh maximum edge length if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If dblLength is specified, the previous render mesh maximum edge length if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 862,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLength",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

