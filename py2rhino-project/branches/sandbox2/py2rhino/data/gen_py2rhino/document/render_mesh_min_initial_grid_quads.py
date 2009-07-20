render_mesh_min_initial_grid_quads = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "render_mesh_min_initial_grid_quads",

    "doc_html": """
        Returns or sets the render mesh minimum initial grid quads parameter of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.RenderMeshMinInitialGridQuads ([intQuads])
    """,

    "params_html": {
        0: {
            "name": "Quads",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The render mesh minimum initial grid quads.  The suggested range is from 0 to 10000.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intQuads is not specified, the current render mesh minimum initial grid quads if successful."
        },
        1: {
            "type": "number",
            "doc": "If intQuads is specified, the previous render mesh minimum initial grid quads if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 850,

    "params_com": {
        0: {
            "name": "vaQuads",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

