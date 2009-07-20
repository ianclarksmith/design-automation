add_material_to_object = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "AddMaterialToObject",
    "output_package_name": "material",
    "output_module_name": "add_material_to_object",

    "doc_html": """
        Adds a material to an object and returns the new material's index.  Note, adding a material to an object modifies the object's material source from "By Layer" to "By Object."  See ObjectMaterialSource for details.  If the object already has a material, then the object's current material index is returned.
    """,

    "syntax_html": """
        Rhino.AddMaterialToObject (strObject)
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the object.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The zero-based material index of the object if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 174,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

