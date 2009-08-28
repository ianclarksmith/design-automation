object_grip_location = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "ObjectGripLocation",
    "output_package_name": "object_grip",
    "output_module_name": "object_grip_location",

    "doc_html": """
        Returns or modifies the location of an object's grip.
    """,

    "syntax_html": {
        0: ("strObject", "intIndex", "arrPoint"),
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
        The identifier of the object.
            """
        },
        1: {
            "name": "intIndex",
            "py_name": "index",
            "opt_or_req": "Required",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Index",
            "doc": """
        The zero-based index of the grip to either query or modify.
            """
        },
        2: {
            "name": "arrPoint",
            "py_name": "point",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr_of_dbl",
            "name_main": "Point",
            "doc": """
        A 3-D point identifying the new location of the grip.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "If arrPoint is not specified, the current location of the grip referenced by intIndex if successful."
        },
        1: {
            "type": "array",
            "doc": "If arrPoint is specified, the previous location of the grip referenced by intIndex if successful."
        },
        2: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 556,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIndex",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaPt",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

