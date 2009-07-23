render_mesh_max_dist_edge_to_srf = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "RenderMeshMaxDistEdgeToSrf",
    "output_package_name": "document",
    "output_module_name": "render_mesh_max_dist_edge_to_srf",

    "doc_html": """
        Returns or sets the render mesh maximum distance, edge to surface parameter of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("dblDistance"),
    },

    "params_html": {
        0: {
            "name": "dblDistance",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Distance",
            "doc": """
        The render mesh maximum distance, edge to surface.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 849,

    "params_com": {
        0: {
            "name": "vaDistance",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

