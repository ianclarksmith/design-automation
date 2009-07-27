layer_mode = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "LayerMode",
    "output_package_name": "layer",
    "output_module_name": "layer_mode",

    "doc_html": """
        OBSOLETE, use either LayerLocked or LayerVisible instead.
		Returns or changes the mode of a layer.
    """,

    "syntax_html": {
        0: ("strLayer", "intMode"),
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
            "name": "intMode",
            "py_name": "mode",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Mode",
            "doc": """
        The new layer mode.  The layer modes are as follows:
		Value
		Description
		0
		Normal.  The layer is visible, and objects on the layer can be selected and changed. (Visible and Unlocked)
		1
		Hidden.  The layer is not visible, and objects on the layer cannot be selected or changed. (Hidden and Unlocked)
		2
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a layer mode is not specified,  the current layer mode  if successful."
        },
        1: {
            "type": "number",
            "doc": "If a layer mode is specified, the previous layer mode if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 14,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaMode",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

