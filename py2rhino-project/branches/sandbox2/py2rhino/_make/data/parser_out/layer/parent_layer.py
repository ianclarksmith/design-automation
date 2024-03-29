parent_layer = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "ParentLayer",
    "output_package_name": "layer",
    "output_module_name": "parent_layer",

    "doc_html": """
        Returns or modifies the parent layer of a layer.
    """,

    "syntax_html": {
        0: ("strLayer", "strParent"),
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
        The name of the layer.
            """
        },
        1: {
            "name": "strParent",
            "py_name": "parent",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Parent",
            "doc": """
        The name of the new parent layer. To remove the parent layer, thus making a root-level layer, specify either Null or an empty string, or "".
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If strParent is not specified, the name of the current parent layer if successful."
        },
        1: {
            "type": "string",
            "doc": "If strParent is specified, the name of the previous parent layer if successful."
        },
        2: {
            "type": "null",
            "doc": "If the layer does not have a parent, or on error."
        },
    },

    "id_com": 688,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaParent",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

