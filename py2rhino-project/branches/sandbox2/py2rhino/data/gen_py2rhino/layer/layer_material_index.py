layer_material_index = {
    "module_name": "layer",
    "class_name": "Layer",
    "method_name": "layer_material_index",

    "doc_html": """
        Returns the material index of a layer.  A material index of -1 indicates that no material has been assigned to the layer.  Thus, the layer will use Rhino's default layer material.
    """,

    "syntax_html": """
        Rhino.LayerMaterialIndex (strLayer)
    """,

    "params_html": {
        0: {
            "name": "Layer",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of an existing layer.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "A zero-based material index if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 13,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

