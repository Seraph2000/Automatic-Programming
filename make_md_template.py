# -*- coding: utf-8 -*-

import re
import textwrap

#This script has the ability to copy text, and generate a python script from that, which can in turn
#print out a .md file

with open("template.md") as f_old, open("generate_md_script.py", "w") as f_new:
    #Enter standard content
    f_new.write('# -*- coding: utf-8 -*-\n')
    f_new.write('\n\n')
    f_new.write('import re\n\n')
    f_new.write('#This script was built automatically, using the script: "make_md_template.py"\n')
    f_new.write('#Feel free to edit the content to reflect any updates.\n\n')
    f_new.write('with open("sample.md", "w") as f_new:\n')
    for i, line in enumerate(f_old):
        line = line.replace("'", "\\'")
        line = line + '\\n'
        line.replace("'", "\'")
        line = '\t' + "f_new.write('" + str(line).replace('\n', '') + "')\n"
        #test for lines to edit here
        f_new.write(line)
