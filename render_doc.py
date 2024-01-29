import time
from docxtpl import DocxTemplate
import os
from make_title import mktitle
from global_variables import wd

def mkdoc(context, doc_type, tpl_filename):
    os.chdir(f"{wd}/Templates")
    tpl = DocxTemplate(tpl_filename)
    tpl.render(context)
    os.chdir(f"{wd}/Output")
    tpl.save(mktitle(context,doc_type))