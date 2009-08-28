display_ole_alerts = {
    "input_folder_name": "Application_Methods",
    "input_file_name": "DisplayOleAlerts",
    "output_package_name": "application",
    "output_module_name": "display_ole_alerts",

    "doc_html": """
        Enables or disables OLE Server Busy/Not Responding dialog boxes from appearing during a lengthy OLE, or COM, operations. In detail, this function does the following:
		* Enables or disables the "Server Busy" dialog box, which is displayed when the message-pending delay expires during an OLE call.
		* Enables or disables the "Not Responding" dialog box, which is displayed if a keyboard or mouse message is pending during an OLE call and the call has timed out.
		Note, the display of OLE Server Busy/Not Responding dialog boxes will be re-enabled whenever the script engine is reset, either by running the ResetRhinoScript command or by having the Reinitialize option enabled in Tools->Options->RhinoScript.
    """,

    "syntax_html": {
        0: ("blnDisplay"),
    },

    "params_html": {
        0: {
            "name": "blnDisplay",
            "py_name": "display",
            "opt_or_req": "Required",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Display",
            "doc": """
        Enable or disable the display of OLE alert dialog boxes.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "null",
            "doc": "If successful or on error."
        },
    },

    "id_com": 896,

    "params_com": {
        0: {
            "name": "vaDisplay",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

