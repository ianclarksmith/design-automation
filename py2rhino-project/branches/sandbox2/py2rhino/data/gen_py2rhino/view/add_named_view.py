add_named_view = {
    "input_folder_name": "View_Methods",
    "input_file_name": "AddNamedView",
    "output_package_name": "view",
    "output_module_name": "add_named_view",

    "doc_html": """
        Adds a new named view to the document.
    """,

    "syntax_html": """
        Rhino.AddNamedView (strName [, strView])
    """,

    "params_html": {
        0: {
            "name": "Name",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of the new named view.
            """
        },
        1: {
            "name": "View",
            "opt_or_req": "Optional",
            "type": "String",
            "type_string": "str",
            "doc": """
        The title or identifier of the view to save.  If omitted, the current active view is saved.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "string",
            "doc": "The name of the newly created named view if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 281,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaView",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

