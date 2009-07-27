layer_locked = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "LayerLocked",
    "output_package_name": "layer",
    "output_module_name": "layer_locked",

    "doc_html": """
        Returns or changes the locked mode of a layer. This method should be use instead of LayerMode.
    """,

    "syntax_html": {
        0: ("strLayer", "blnLocked"),
    },

    "params_html": {
        0: {
            "name": "strLayer",
            "py_name": "layer",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layer",
            "doc": """
        The name of an existing layer.
            """
        },
        1: {
            "name": "blnVisible",
            "py_name": "visible",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Visible",
            "doc": """
        The new layer locked mode.  True = Locked, False = Unlocked.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If a layer mode is not specified,  the current layer locked mode if successful."
        },
        1: {
            "type": "boolean",
            "doc": "If a layer mode is specified, the previous layer locked mode if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 601,

    "params_com": {
        0: {
            "name": "vaLayer",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaLocked",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

