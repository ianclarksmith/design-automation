compare_geometry = {
    "input_folder_name": "Geometry_Methods",
    "input_file_name": "CompareGeometry",
    "output_package_name": "geometry",
    "output_module_name": "compare_geometry",

    "doc_html": """
        Compares two objects to determine if they are geometrically identical.
    """,

    "syntax_html": {
        0: ("strObject1", "strObject2"),
    },

    "params_html": {
        0: {
            "name": "strObject1",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object1",
            "doc": """
        The identifier of the first object to compare.
            """
        },
        1: {
            "name": "strObject2",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Object2",
            "doc": """
        The identifier of the second object to compare.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True if the objects are geometrically identical, otherwise False."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 598,

    "params_com": {
        0: {
            "name": "vaObj1",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaObj2",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

