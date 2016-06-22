# -*- coding: utf-8 -*-


import re

#This script was built automatically, using the script: "make_md_template.py"
#Feel free to edit the content to reflect any updates.

with open("sample.md", "w") as f_new:
	f_new.write('## Synopsis\n')
	f_new.write('\n')
	f_new.write('At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)\n')
	f_new.write('\n')
	f_new.write('## Code Example\n')
	f_new.write('\n')
	f_new.write('Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.\n')
	f_new.write('\n')
	f_new.write('## Motivation\n')
	f_new.write('\n')
	f_new.write('A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.\n')
	f_new.write('\n')
	f_new.write('## Installation\n')
	f_new.write('\n')
	f_new.write('Provide code examples and explanations of how to get the project.\n')
	f_new.write('\n')
	f_new.write('## API Reference\n')
	f_new.write('\n')
	f_new.write('Depending on the size of the project, if it is small and simple enough the reference docs can be added to the README. For medium size to larger projects it is important to at least provide a link to where the API reference docs live.\n')
	f_new.write('\n')
	f_new.write('## Tests\n')
	f_new.write('\n')
	f_new.write('Describe and show how to run the tests with code examples.\n')
	f_new.write('\n')
	f_new.write('## Contributors\n')
	f_new.write('\n')
	f_new.write('Let people know how they can dive into the project, include important links to things like issue trackers, irc, twitter accounts if applicable.\n')
	f_new.write('\n')
	f_new.write('## License\n')
	f_new.write('\n')
	f_new.write('A short snippet describing the license (MIT, Apache, etc.)\n')
