add_material_to_layer = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "AddMaterialToLayer",
    "output_package_name": "material",
    "output_module_name": "add_material_to_layer",

    "doc_html": """
        Adds a material to a layer and returns the new material's index.  If the layer already has a material, then the layer's current material index is returned.
    """,

    "syntax_html": {
        0: ("strLayer"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "py_name": "object",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The name of an existing layer.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The zero-based material index of the layer if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 173,

    "params_com": {
        0: {
            "name": "vaLayer",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

