render_mesh_quality = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "render_mesh_quality",

    "doc_html": """
        Returns or sets the render mesh quality of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.RenderMeshQuality ([intQuality])
    """,

    "params_html": {
        0: {
            "name": "Quality",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The render mesh quality, either:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intQuality is not specified, the current render mesh quality if successful."
        },
        1: {
            "type": "number",
            "doc": "If intQuality is specified, the previous render mesh quality if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 843,

    "params_com": {
        0: {
            "name": "vaQuality",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

