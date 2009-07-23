enable_object_mesh = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "EnableObjectMesh",
    "output_package_name": "object",
    "output_module_name": "enable_object_mesh",

    "doc_html": """
        Enables or disables an object's custom render mesh parameters. If an object's custom render mesh parameters are enabled, then they will be used, instead of the document's render mesh parameters, when a render mesh is generated for the object.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    """,

    "syntax_html": {
        0: ("strObject", "blnEnable"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "opt_or_req": "Required",
            "type": "Object",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        The identifier of a meshable object.
            """
        },
        1: {
            "name": "blnEnable",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Enable",
            "doc": """
        Enable the custom render mesh settings.
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

    "id_com": 856,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaEnable",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

