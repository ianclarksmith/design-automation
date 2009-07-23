unit_system = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitSystem",
    "output_package_name": "document",
    "output_module_name": "unit_system",

    "doc_html": """
        Returns or sets the document's units system.  See Rhino's DocumentProperties command (Units window) for details.
    """,

    "syntax_html": {
        0: ("intSystem", "blnScale"),
    },

    "params_html": {
        0: {
            "name": "intSystem",
            "opt_or_req": "Optional",
            "type": "Number",
            "name_prefix": "int",
            "name_main": "System",
            "doc": """
        The units system.  The available units systems are as follows:
		Value
		Description
		0
		No unit system
		1
		Microns (1.0e-6 meters)
		2
		Millimeters (1.0e-3 meters)
		3
		Centimeters (1.0e-2 meters)
		4
		Meters
		5
		Kilometers (1.0e+3 meters)
		6
		Microinches (2.54e-8 meters, 1.0e-6 inches)
		7
		Mils (2.54e-5 meters, 0.001 inches)
		8
		Inches (0.0254 meters)
		9
		Feet (0.3408 meters, 12 inches)
		10
		Miles (1609.344 meters, 5280 feet)
		11
		* Reserved for Custom Unit System *
		12
		Angstroms (1.0e-10 meters)
		13
		Nanometers (1.0e-9 meters)
		14
		Decimeters (1.0e-1 meters)
		15
		Dekameters (1.0e+1 meters)
		16
		Hectometers (1.0e+2 meters)
		17
		Megameters (1.0e+6 meters)
		18
		Gigameters (1.0e+9 meters)
		19
		Yards (0.9144  meters, 36 inches)
		20
		Printer point (1/72 inches, computer points)
		21
		Printer pica (1/6 inches, (computer picas)
		22
		Nautical mile (1852 meters)
		23
		Astronomical (1.4959787e+11)
		24
		Lightyears (9.46073e+15 meters)
		25
            """
        },
        1: {
            "name": "blnScale",
            "opt_or_req": "Optional",
            "type": "Boolean",
            "name_prefix": "bln",
            "name_main": "Scale",
            "doc": """
        Scale existing geometry based on the new unit system.  If not specified, any existing geometry is not scaled (False).
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The previous units system if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 330,

    "params_com": {
        0: {
            "name": "vaSystem",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaScale",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

