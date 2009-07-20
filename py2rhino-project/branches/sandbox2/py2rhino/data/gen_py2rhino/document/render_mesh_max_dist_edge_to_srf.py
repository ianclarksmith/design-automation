render_mesh_max_dist_edge_to_srf = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "render_mesh_max_dist_edge_to_srf",

    "doc_html": """
        Returns or sets the render mesh maximum distance, edge to surface parameter of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.RenderMeshMaxDistEdgeToSrf ([dblDistance])
    """,

    "params_html": {
        0: {
            "name": "Distance",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
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

