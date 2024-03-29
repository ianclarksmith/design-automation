object_print_width = {
    "input_folder_name": "Object_Methods",
    "input_file_name": "ObjectPrintWidth",
    "output_package_name": "object",
    "output_module_name": "object_print_width",

    "doc_html": """
        Returns or modifies the print width of an object.  Object print widths are measured in millimeters (mm).
    """,

    "syntax_html": {
        0: ("strObject", "dblWidth"),
        1: ("arrObjects", "dblWidth"),
    },

    "params_html": {
        0: {
            "name": "arrObjects",
            "py_name": "objects",
            "opt_or_req": "Required",
            "type": "Array",
            "name_prefix": "arr_of_str",
            "name_main": "Objects",
            "doc": """
        An array of strings identifying the objects to modify.
            """
        },
        1: {
            "name": "dblWidth",
            "py_name": "width",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "dbl",
            "name_main": "Width",
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

