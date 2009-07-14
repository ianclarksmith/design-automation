# To connect Python to Rhino - do the following:
# 1. Install pywin32
# 2. copy rhinoCOM folder to the Lib/site-packages folder
# 3. Start Rhino v4
# 4. Then type this at the python prompt

from rhinoCOM import RhinoConnection
RhinoConnection.rhino.AddText("Hello Rhino", (0,0,0))