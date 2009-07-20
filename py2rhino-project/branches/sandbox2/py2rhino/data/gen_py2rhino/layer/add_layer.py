add_layer = {
    "input_folder_name": "Layer_Methods",
    "input_file_name": "AddLayer",
    "output_package_name": "layer",
    "output_module_name": "add_layer",

    "doc_html": """
        Adds a new layer to the document.
    """,

    "syntax_html": """
        Rhino.AddLayer ([strLayer [, lngColor [, blnVisible [, blnLocked [,strParent]]]]])
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the new layer.  If omitted, Rhino automatically generates the layer name.
            """
        },
        1: {
            "name": "Color",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        A Red-Green-Blue color value.  If omitted, the color Black is assigned.
            """
        },
        2: {
            "name": "Visible",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The layer's visibility. The default is visible (True).
            """
        },
        3: {
            "name": "Locked",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The layer's locked state. The default is not locked (False).
            """
        },
        4: {
            "name": "Parent",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
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

