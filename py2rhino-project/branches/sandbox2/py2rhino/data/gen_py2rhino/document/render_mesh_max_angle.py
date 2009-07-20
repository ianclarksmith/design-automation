render_mesh_max_angle = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "RenderMeshMaxAngle",
    "output_package_name": "document",
    "output_module_name": "render_mesh_max_angle",

    "doc_html": """
        Returns or sets the render mesh maximum angle property of the active document.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": """
        Rhino.RenderMeshMaxAngle ([dblAngle])
    """,

    "params_html": {
        0: {
            "name": "Angle",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The render mesh maximum angle in degrees.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If dblAngle is not specified, the current render maximum angle if successful."
        },
        1: {
            "type": "number",
            "doc": "If dblAngle is specified, the previous render mesh maximum angle if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 845,

    "params_com": {
        0: {
            "name": "vaAngle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

