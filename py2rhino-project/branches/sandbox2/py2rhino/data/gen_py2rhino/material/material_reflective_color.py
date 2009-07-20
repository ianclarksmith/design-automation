material_reflective_color = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MaterialReflectiveColor",
    "output_package_name": "material",
    "output_module_name": "material_reflective_color",

    "doc_html": """
        Returns or modifies a material's reflective color.  Reflective colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    """,

    "syntax_html": """
        Rhino.MaterialReflectiveColor (intMaterialIndex [, lngColor])
    """,

    "params_html": {
        0: {
            "name": "MaterialIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The zero-based source material index.
            """
        },
        1: {
            "name": "Color",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "lng",
            "doc": """
        The new color value.  If omitted, the current reflective color is returned.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If lngColor is not specified, the current reflective color if successful."
        },
        1: {
            "type": "number",
            "doc": "If lngColor is specified, the previous reflective color if successful."
        },
        2: {
            "type": "null",
            "doc": "It not successful, or on error."
        },
    },

    "id_com": 180,

    "params_com": {
        0: {
            "name": "vaIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaValue",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

