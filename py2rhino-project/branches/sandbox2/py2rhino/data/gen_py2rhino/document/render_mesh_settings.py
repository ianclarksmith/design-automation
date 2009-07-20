render_mesh_settings = {
    "module_name": "document",
    "class_name": "Document",
    "method_name": "render_mesh_settings",

    "doc_html": """
        Returns or sets the render mesh settings of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.RenderMeshSettings ([intSettings])
    """,

    "params_html": {
        0: {
            "name": "Settings",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The render mesh settings, which is a bit-coded number that allows or disallows certain features.  The bits can be added together in any combination to form a value between 0 and 7.  The bit values are as follows:
		Value
		Description
		0
		No settings enabled.
		1
		Refine mesh enabled.
		2
		Jagged seams enabled.
		4
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If intSettings is not specified, the current render mesh settings if successful."
        },
        1: {
            "type": "number",
            "doc": "If intSettings is specified, the previous render mesh settings if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 851,

    "params_com": {
        0: {
            "name": "vaFlags",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

