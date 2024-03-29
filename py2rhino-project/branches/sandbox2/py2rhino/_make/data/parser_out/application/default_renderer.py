default_renderer = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "DefaultRenderer",
    "output_package_name": "application",
    "output_module_name": "default_renderer",

    "doc_html": """
        Returns or changes Rhino's current, or default, render plug-in.  Use the PlugIns method to get a list of available render plug-ins.
    """,

    "syntax_html": {
        0: ("strRenderer"),
    },

    "params_html": {
        0: {
            "name": "strRenderer",
            "py_name": "renderer",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Renderer",
            "doc": """
        The name of a render plug-in to set as default.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a render plug-in is not specified, the name of the current render plug-in if successful."
        },
        1: {
            "type": "string",
            "doc": "If a render plug-in is specified, the name of the previous current render plug-in if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 316,

    "params_com": {
        0: {
            "name": "vaRenderer",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

