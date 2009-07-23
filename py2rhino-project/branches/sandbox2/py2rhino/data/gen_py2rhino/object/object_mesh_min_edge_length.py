object_mesh_min_edge_length = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectMeshMinEdgeLength",
    "output_package_name": "object",
    "output_module_name": "object_mesh_min_edge_length",

    "doc_html": """
        Returns or modifies an object's custom render mesh parameter's minimum edge length property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("strObject", "dblLength"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
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
            "py_name": "length",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Length",
            "doc": """
        The render mesh minimum edge length.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If dblLength is not specified, the current render mesh minimum edge length if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If dblLength is specified, the previous render mesh minimum edge length if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 861,

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

