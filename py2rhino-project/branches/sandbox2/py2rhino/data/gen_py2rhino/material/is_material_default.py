is_material_default = {
    "module_name": "material",
    "class_name": "Material",
    "method_name": "is_material_default",

    "doc_html": """
        Verifies that a material is a copy of Rhino's built-in "default" material.  The default material is used by objects and layers that have not been assigned a material.
    """,

    "syntax_html": """
        Rhino.IsMaterialDefault (intMaterialIndex)
    """,

    "params_html": {
        0: {
            "name": "MaterialIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The zero-based material index.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 175,

    "params_com": {
        0: {
            "name": "vaIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

