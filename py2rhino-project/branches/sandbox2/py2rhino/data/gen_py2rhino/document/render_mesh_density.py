render_mesh_density = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "render_mesh_density",

    "doc_html": """
        Returns or sets the render mesh density property of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.RenderMeshDensity ([dblDensity])
    """,

    "params_html": {
        0: {
            "name": "Density",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The render mesh density, which is a number between 0.0 and 1.0.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblDensity is not specified, the current render mesh density if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblDensity is specified, the previous render mesh density if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 844,

    "params_com": {
        0: {
            "name": "vaDensity",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

