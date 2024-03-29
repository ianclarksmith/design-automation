render_mesh_max_aspect_ratio = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "RenderMeshMaxAspectRatio",
    "output_package_name": "document",
    "output_module_name": "render_mesh_max_aspect_ratio",

    "doc_html": """
        Returns or sets the render mesh maximum aspect ratio property of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("dblRatio"),
    },

    "params_html": {
        0: {
            "name": "dblRatio",
            "py_name": "ratio",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Ratio",
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

