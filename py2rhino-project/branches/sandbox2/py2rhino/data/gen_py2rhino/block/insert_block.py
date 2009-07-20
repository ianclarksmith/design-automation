insert_block = {
    "module_name": "block",
    "class_name": "Block",
    "method_name": "insert_block",

    "doc_html": """
        Inserts a block whose definition already exists in the document.
    """,

    "syntax_html": """
        Rhino.InsertBlock (strName, arrPoint [, arrScale [, dblAngle [, arrNormal]]])
    """,

    "params_html": {
        0: {
            "name": "Name",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the block definition to insert.
            """
        },
        1: {
            "name": "Point",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        The 3-D insertion point of the block.
            """
        },
        2: {
            "name": "Scale",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of three numbers that identify the x,y,z scale factors. If omitted, the block is not scaled.
            """
        },
        3: {
            "name": "Angle",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The rotation angle in degrees. If omitted, the block is not rotated.
            """
        },
        4: {
            "name": "Normal",
            "opt_or_req": "Optional",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        A 3-D vector identifying the axis of rotation. If omitted and dblAngle is specified, the world Z axis is used.
            """
        },
        5: {
            "name": "Xform",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
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

