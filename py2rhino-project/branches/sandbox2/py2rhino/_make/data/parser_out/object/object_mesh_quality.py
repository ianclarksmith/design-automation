object_mesh_quality = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectMeshQuality",
    "output_package_name": "object",
    "output_module_name": "object_mesh_quality",

    "doc_html": """
        Returns or sets the render mesh quality of an object's custom render mesh parameters.
    """,

    "syntax_html": {
        0: ("strObject", "intQuality"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "Object",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of an object that has custom render mesh parameters.
            """
        },
        1: {
            "name": "intQuality",
            "py_name": "quality",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Quality",
            "doc": """
        The render mesh quality, either:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default)
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If intQuality is not specified, the current render mesh quality if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If intQuality is specified, the previous render mesh quality if successful."
        },
        2: {
            "type": "null",
            "doc": "If the object does not have custom render mesh parameters, or on error."
        },
    },

    "id_com": 857,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaQuality",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

