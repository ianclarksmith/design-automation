purge_layer = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "PurgeLayer",
    "output_package_name": "layer",
    "output_module_name": "purge_layer",

    "doc_html": """
        Removes an existing layer from the document.  Unlike the DeleteLayer method, PurgeLayer will remove the layer even if contains geometry objects.  The layer to be removed cannot be the current layer.
    """,

    "syntax_html": """
        Rhino.PurgeLayer (strLayer)
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the layer to purge.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the purged layer if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 291,

    "params_com": {
        0: {
            "name": "vaLayer",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

