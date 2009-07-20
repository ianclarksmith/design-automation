get_plug_in_object = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "GetPlugInObject",
    "output_package_name": "application",
    "output_module_name": "get_plug_in_object",

    "doc_html": """
        Returns a scriptable object from a specified plug-in. Note, not all plug-ins contain scriptable objects. Check with the manufacturer of your plug-in to see if they support this capability.
    """,

    "syntax_html": """
        Rhino.GetPlugInObject (strPlugIn)
    """,

    "params_html": {
        0: {
            "name": "PlugIn",
            "opt_or_req": "Required",
            "type": "String",
            "type_string": "str",
            "doc": """
        The name of a registered plug-in that supports scripting.  If the plug-in is registered but not loaded, it will be loaded.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 636,

    "params_com": {
        0: {
            "name": "vaName",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

