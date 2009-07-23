add_startup_script = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "AddStartupScript",
    "output_package_name": "application",
    "output_module_name": "add_startup_script",

    "doc_html": """
        Adds a new startup script to RhinoScript's startup script list. Startup script  items can be added manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.
    """,

    "syntax_html": {
        0: ("strScriptFile", "intIndex"),
    },

    "params_html": {
        0: {
            "name": "strScriptFile",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "ScriptFile",
            "doc": """
        A valid path to a RhinoScript .RVB file.
            """
        },
        1: {
            "name": "intIndex",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "Index",
            "doc": """
        A zero-based position index in the startup script list to insert the string. If omitted, the path will be appended to the end of the startup script list.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The zero-based index of the new startup script item. If the index is less than zero, then the path item was not added to the search path list."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 714,

    "params_com": {
        0: {
            "name": "vaScript",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaIndex",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

