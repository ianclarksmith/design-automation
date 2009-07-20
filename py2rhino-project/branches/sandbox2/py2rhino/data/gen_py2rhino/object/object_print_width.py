object_print_width = {
    "module_name": "object",
    "class_name": "Object",
    "method_name": "object_print_width",

    "doc_html": """
        Returns or modifies the print width of an object.  Object print widths are measured in millimeters (mm).
    """,

    "syntax_html": """
        Rhino.ObjectPrintWidth (strObject [, dblWidth])
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
            "name": "Objects",
            "opt_or_req": "Required",
            "type": "Array",
            "type_string": "arr",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        2: {
            "name": "Width",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "dbl",
            "doc": """
        The new print width value in millimeters, where dblWidth = 0.0 means use the default width, and dblWidth < 0.0 means do not print (visible for screen display, but does not show on print).  If omitted, the current object print width is returned.  Note, if arrObjects is specified, dblWidth is required.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "If a print width value is not specified,  the current print width value if successful."
        },
        1: {
            "type": "number",
            "doc": "If a print width value is specified, the previous print width value if successful."
        },
        2: {
            "type": "number",
            "doc": "If arrObjects is specified, then the number of objects modified if successful."
        },
        3: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 807,

    "params_com": {
        0: {
            "name": "vaObject",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vavaWidth",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

