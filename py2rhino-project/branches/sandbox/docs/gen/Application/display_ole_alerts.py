display_ole_alerts = {

    "class": "Application",
    "method": "display_ole_alerts",
    "doc": """
        Enables or disables OLE Server Busy/Not Responding dialog boxes from appearing during a lengthy OLE, or COM, operations. In detail, this function does the following:
		* Enables or disables the "Server Busy" dialog box, which is displayed when the message-pending delay expires during an OLE call.
		* Enables or disables the "Not Responding" dialog box, which is displayed if a keyboard or mouse message is pending during an OLE call and the call has timed out.
		Note, the display of OLE Server Busy/Not Responding dialog boxes will be re-enabled whenever the script engine is reset, either by running the ResetRhinoScript command or by having the Reinitialize option enabled in Tools->Options->RhinoScript.
    """,

    "syntax": """
        Rhino.DisplayOleAlerts (blnDisplay)
    """,

    "params": {
        0: {
            "name": "display",
            "optional": False,
            "type_vb": "boolean",
            "type_string": "bln",
            "doc": """
        Enable or disable the display of OLE alert dialog boxes.
            """
        },
    },

    "returns": {
        0: {
            "type_vb": "Null",
            "doc": "If successful or on error."
        },
    }

}

