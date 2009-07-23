render_mesh_max_edge_length = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "RenderMeshMaxEdgeLength",
    "output_package_name": "document",
    "output_module_name": "render_mesh_max_edge_length",

    "doc_html": """
        Returns or sets the render mesh maximum edge length parameter of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("dblLength"),
    },

    "params_html": {
        0: {
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
            "type": "number",
            "doc": "If dblLength is not specified, the current render mesh maximum edge length if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblLength is specified, the previous render mesh maximum edge length if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 848,

    "params_com": {
        0: {
            "name": "vaLength",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

