is_object_in_box = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "IsObjectInBox",
    "output_package_name": "object",
    "output_module_name": "is_object_in_box",

    "doc_html": """
        Verifies an object's bounding box is inside of another bounding box.
    """,

    "syntax_html": """
        Rhino.IsObjectInBox (strObject, arrBox, [blnMode])
    """,

    "params_html": {
        0: {
            "name": "Object",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The identifier of an object.
            """
        },
        1: {
            "name": "Box",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The bounding box to test against. A bounding box is an array of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.
            """
        },
        2: {
            "name": "Mode",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "type_string": "bln",
            "doc": """
        The test mode.
		Value
		Description
		True (Default)
		The object's bounding box must be contained by the test bounding box. In other words, test.min <= object.min and object.max <= test.max.
		False
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 799,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaBox",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaFlag",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

