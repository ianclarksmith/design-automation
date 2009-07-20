unit_scale = {
    "input_folder_name": "Document_Methods",
    "input_file_name": "UnitScale",
    "output_package_name": "document",
    "output_module_name": "unit_scale",

    "doc_html": """
        Returns the scale factor for changing between unit systems.
    """,

    "syntax_html": """
        Rhino.UnitSystem (intToSystem [, intFromSystem])
    """,

    "params_html": {
        0: {
            "name": "ToSystem",
            "opt_or_req": "Required",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The units system to convert to.  The possible units systems are as follows:
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
            "name": "FromSystem",
            "opt_or_req": "Optional",
            "type": "Number",
            "type_string": "int",
            "doc": """
        The units system to convert from (see above).  If omitted, the document's current unit system is used
            """
        },
    },

    "returns_html": {
        0: {
            "type": "number",
            "doc": "The scale factor for changing between unit systems if successful."
        },
        1: {
            "type": "null",
            "doc": "If not successful, or on error."
        },
    },

    "id_com": 868,

    "params_com": {
        0: {
            "name": "vaTo",
            "opt_or_req": "Required",
            "type": "tagVARIANT",
        },
        1: {
            "name": "vaFrom",
            "opt_or_req": "Optional",
            "type": "tagVARIANT",
        },
    },

    "returns_com": "tagVARIANT",

}

