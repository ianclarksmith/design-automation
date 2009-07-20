delete_startup_script = {
    "module_name": "application",
    "class_name": "Application",
    "method_name": "delete_startup_script",

    "doc_html": """
        Removes an existing startup script from RhinoScript's startup script list. Startup script items can be removed manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.
    """,

    "syntax_html": """
        Rhino.DeleteStartupScript (strScriptFile)
    """,

    "params_html": {
        0: {
            "name": "ScriptFile",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        An existing script file path to remove.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "On error."
        },
    },

    "id_com": 715,

    "params_com": {
        0: {
            "name": "vaScript",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

