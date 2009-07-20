render_mesh_max_aspect_ratio = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "render_mesh_max_aspect_ratio",

    "doc_html": """
        Returns or sets the render mesh maximum aspect ratio property of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.RenderMeshMaxAspectRatio ([dblRatio])
    """,

    "params_html": {
        0: {
            "name": "Ratio",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The render mesh maximum aspect ratio.  The suggested range, when not zero, is from 1 to 100.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblRatio is not specified, the current render mesh maximum aspect ratio if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblRatio is specified, the previous render mesh maximum aspect ratio if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 846,

    "params_com": {
        0: {
            "name": "vaRatio",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

