text_object_point = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "TextObjectPoint",
    "output_package_name": "geometry",
    "output_module_name": "text_object_point",

    "doc_html": """
        Returns or modifies the location of a text object.
    """,

    "syntax_html": {
        0: ("strObject", "arrPoint"),
    },

    "params_html": {
        0: {
            "name": "strObject",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object",
            "doc": """
        The identifier of the object.
            """
        },
        1: {
            "name": "arrPoint",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point identifying the new location point.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "If a new location is not specified,  the 3-D point identifying the current location if successful."
        },
        1: {
            "type": "string",
            "doc": "If a new location is specified,  the 3-D point identifying the previous location if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 471,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPoint",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

