match_material = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MatchMaterial",
    "output_package_name": "material",
    "output_module_name": "match_material",

    "doc_html": """
        Copies the material definition from one material to one or more objects.
    """,

    "syntax_html": """
        Rhino.MatchMaterial (intSrcMaterialIndex, strDestObject)
    """,

    "params_html": {
        0: {
            "name": "SrcMaterialIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The zero-based source material index.
            """
        },
        1: {
            "name": "SrcObject",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the source object.  The object must have a material assigned.
            """
        },
        2: {
            "name": "DestObject",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of the destination object.  If the object's material source is set to "By Layer", it will be changed to "By Object."
            """
        },
        3: {
            "name": "DestObjects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of destination object identifiers.  If the objects' material sources are set to "By Layer", they will be changed to "By Object."
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The number of object that were modified if successful."
        },
        1: {
            "type": "null",
            "doc": "It not successful, or on error."
        },
    },

    "id_com": 322,

    "params_com": {
        0: {
            "name": "vaSrc",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaDest",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

