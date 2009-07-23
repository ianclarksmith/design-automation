add_layer = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "AddLayer",
    "output_package_name": "layer",
    "output_module_name": "add_layer",

    "doc_html": """
        Adds a new layer to the document.
    """,

    "syntax_html": {
        0: ("strLayer", "lngColor", "blnVisible", "blnLocked", "strParent"),
    },

    "params_html": {
        0: {
            "name": "strLayer",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Layer",
            "doc": """
        The name of the new layer.  If omitted, Rhino automatically generates the layer name.
            """
        },
        1: {
            "name": "lngColor",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "lng",
            "name_main": "Color",
            "doc": """
        A Red-Green-Blue color value.  If omitted, the color Black is assigned.
            """
        },
        2: {
            "name": "blnVisible",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Visible",
            "doc": """
        The layer's visibility. The default is visible (True).
            """
        },
        3: {
            "name": "blnLocked",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Locked",
            "doc": """
        The layer's locked state. The default is not locked (False).
            """
        },
        4: {
            "name": "strParent",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Parent",
            "doc": """
        The name of the new layer's parent layer. If omitted, the new layer will have not parent layer.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the new layer if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 3,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaColor",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaVisible",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaLocked",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaParent",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

