match_material = {
    "input_folder_name": "Material_Methods",
    "input_file_name": "MatchMaterial",
    "output_package_name": "material",
    "output_module_name": "match_material",

    "doc_html": """
        Copies the material definition from one material to one or more objects.
    """,

    "syntax_html": {
        0: ("intSrcMaterialIndex", "strDestObject"),
        1: ("strSrcObject", "arrDestObjects"),
    },

    "params_html": {
        0: {
            "name": "intSrcMaterialIndex",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "SrcMaterialIndex",
            "doc": """
        The zero-based source material index.
            """
        },
        1: {
            "name": "strSrcObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "SrcObject",
            "doc": """
        The identifier of the source object.  The object must have a material assigned.
            """
        },
        2: {
            "name": "arrDestObjects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "DestObjects",
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

