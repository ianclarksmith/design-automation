add_object_mesh = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "AddObjectMesh",
    "output_package_name": "object",
    "output_module_name": "add_object_mesh",

    "doc_html": """
        
    """,

    "syntax_html": """
        Rhino.AddObjectMesh (strObject [, intQuality [, blnEnable]])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "Object",
            "type_string": "str",
            "doc": """
        The identifier of a meshable object.
            """
        },
        1: {
            "name": "Quality",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The initial settings of the new custom render mesh parameters. The available options are as follows:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default)
            """
        },
        2: {
            "name": "Enable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        Enable the custom render mesh parameters.  If omitted, the newly added parameters will be enabled (True).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnEnable is not specified, then the current enabled/disabled state if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If blnEnable is not specified, then the current enabled/disabled state if successful."
        },
        2: {
            "type": "null",
            "doc": "If the object does not have custom render mesh parameters, or on error."
        },
    },

    "id_com": 866,

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
        2: {
            "name": "vaEnable",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

