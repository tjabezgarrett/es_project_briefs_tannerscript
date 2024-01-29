from render_doc import mkdoc
from logic_modules import mod_context
from data import raw_context
import os
import subprocess
from global_variables import wd

# Clear output table
dir = f"{wd}/Output/"
try:
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
except:
    print('>Cannot delete old output, does not exist')

# Establish template Filenames
pb_tpl = "ES Project Briefs v4.docx"

# Generate Context
variable_list = mod_context(raw_context)
context = variable_list


# Render Documents with variables injected
mkdoc(context,'proj_brief',pb_tpl)

#Bring up Finder window of output folder
subprocess.call(["open","-R", dir])