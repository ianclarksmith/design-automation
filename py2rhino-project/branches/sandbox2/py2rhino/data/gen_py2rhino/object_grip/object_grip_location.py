object_grip_location = {
    "input_folder_name": "Object_Grip_Methods",
    "input_file_name": "ObjectGripLocation",
    "output_package_name": "object_grip",
    "output_module_name": "object_grip_location",

    "doc_html": """
        Returns or modifies the location of an object's grip.
    """,

    "syntax_html": """
        Rhino.ObjectGripLocation (strObject, intIndex [, arrPoint])
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
        1: {
            "name": "Index",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The zero-based index of the grip to either query or modify.
            """
        },
        2: {
            "name": "Point",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
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

