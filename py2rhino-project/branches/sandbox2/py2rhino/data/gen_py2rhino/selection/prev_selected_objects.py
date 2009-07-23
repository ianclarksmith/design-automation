prev_selected_objects = {
    "input_folder_name": "Selection_Methods",
    "input_file_name": "PrevSelectedObjects",
    "output_package_name": "selection",
    "output_module_name": "prev_selected_objects",

    "doc_html": """
        Returns the identifiers of the previously selected objects.  The operation of this function is similar to that of Rhino's SelPrev command.
    """,

    "syntax_html": {
        0: ("blnSelect"),
    },

    "params_html": {
        0: {
            "name": "blnSelect",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Select",
            "doc": """
        Select the object.  If omitted, the object is not selected (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "array",
            "doc": "An array of strings identifying the previously selected objects if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 486,

    "params_com": {
        0: {
            "name": "vaSelect",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

