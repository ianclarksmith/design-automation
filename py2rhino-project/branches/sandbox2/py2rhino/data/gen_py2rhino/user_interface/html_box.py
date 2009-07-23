html_box = {
    "input_folder_name": "User_Interface_Methods",
    "input_file_name": "HtmlBox",
    "output_package_name": "user_interface",
    "output_module_name": "html_box",

    "doc_html": """
        Displays a custom, modal HTML dialog page. A modal dialog box retains the input focus while open. The user cannot switch windows until the dialog box is closed.
    """,

    "syntax_html": {
        0: ("strFileName", "arrArguments", "strOptions", "blnModal"),
    },

    "params_html": {
        0: {
            "name": "strFileName",
            "opt_or_req": "Required",
            "type": "String",
            "name_prefix": "str",
            "name_main": "FileName",
            "doc": """
        The filename the HTML dialog page to display.
            """
        },
        1: {
            "name": "vaArguments",
            "opt_or_req": "Optional",
            "type": "Variant",
            "name_prefix": "va",
            "name_main": "Arguments",
            "doc": """
        An argument, or a zero-based, one-dimensional array of arguments, to pass to the HTML-dialog page.
            """
        },
        2: {
            "name": "strOptions",
            "opt_or_req": "Optional",
            "type": "String",
            "name_prefix": "str",
            "name_main": "Options",
            "doc": """
        The window ornaments for the dialog box, using one or more of the following semicolon-delimited values:
		Value
		Description
		dialogHeight:sHeight
		Sets the height of the dialog window.
		dialogLeft:sXPos
		Sets the left position of the dialog window relative to the upper-left corner of the desktop.
		dialogTop:sYPos
		Sets the top position of the dialog window relative to the upper-left corner of the desktop.
		dialogWidth:sWidth
		Sets the width of the dialog window.
		center:{ yes | no | 1 | 0 | on | off }
		Specifies whether to center the dialog window within the desktop. The default is yes.
		dialogHide:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window is hidden when printing or using print preview. This feature is only available when a dialog box is opened from a trusted application. The default is no.
		edge:{ sunken | raised }
		Specifies the edge style of the dialog window. The default is raised.
		help:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window displays the context-sensitive Help icon. The default is yes.
		resizable:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window has fixed dimensions. The default is no.
		scroll:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window displays scrollbars. The default is yes.
		status:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window displays a status bar. The default is yes for untrusted dialog windows and no for trusted dialog windows.
		unadorned:{ yes | no | 1 | 0 | on | off }
            """
        },
        3: {
            "name": "blnModal",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Modal",
            "doc": """
        If omitted or True, a modal dialog will be displayed.  If False, a modeless dialog box will be displayed.
            """
        },
    },

    "returns_html": {
        0: {
            "type": "boolean",
            "doc": "If blnModal is specified and is True, then True or False indicating success or failure."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 276,

    "params_com": {
        0: {
            "name": "vaFile",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaArgs",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        2: {
            "name": "vaOptions",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        3: {
            "name": "vaModal",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

