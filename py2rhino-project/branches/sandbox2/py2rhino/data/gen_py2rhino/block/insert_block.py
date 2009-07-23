insert_block = {
    "input_folder_name": "Block_Methods",
    "input_file_name": "InsertBlock",
    "output_package_name": "block",
    "output_module_name": "insert_block",

    "doc_html": """
        Inserts a block whose definition already exists in the document.
    """,

    "syntax_html": {
        0: ("strName", "arrPoint", "arrScale", "dblAngle", "arrNormal"),
        1: ("strName", "arrXform"),
    },

    "params_html": {
        0: {
            "name": "strName",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Name",
            "doc": """
        The name of the block definition to insert.
            """
        },
        1: {
            "name": "arrPoint",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Point",
            "doc": """
        The 3-D insertion point of the block.
            """
        },
        2: {
            "name": "arrScale",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Scale",
            "doc": """
        An array of three numbers that identify the x,y,z scale factors. If omitted, the block is not scaled.
            """
        },
        3: {
            "name": "dblAngle",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Angle",
            "doc": """
        The rotation angle in degrees. If omitted, the block is not rotated.
            """
        },
        4: {
            "name": "arrNormal",
            "opt_or_req": "Optional",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Normal",
            "doc": """
        A 3-D vector identifying the axis of rotation. If omitted and dblAngle is specified, the world Z axis is used.
            """
        },
        5: {
            "name": "arrXform",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr",
            "name_main": "Xform",
            "doc": """
        4x4 transformation matrix to apply.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The identifier of the newly inserted block instance, if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 633,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaPt",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaScale",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaAngle",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        4: {
            "name": "vaRotate",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

