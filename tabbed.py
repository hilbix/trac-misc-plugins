# Needs https://github.com/hilbix/tracinfosnippetplugin

import io

from trac.wiki.macros import WikiMacroBase
from trac.util.html import escape
import re

class TabbedMacro(WikiMacroBase):
	"""
	Display Tabbed data as table

	{{{
	{{{#!Tabbed
	123	abc	xyz
	456	def	uvw
	}}}
	}}}

	gives:

	|| 123 || abc || xyz ||
	|| 456 || 234 || uvw ||

	This also supports copybutton from https://github.com/hilbix/tracinfosnippetplugin
	"""

	def get_macros(self):
		yield 'Tabbed'

	def expand_macro(self, formatter, name, content):
		with io.StringIO() as out:
			m = 0
			for line in content.splitlines():
				l = len(re.split(r'\t+', line.rstrip()))
				if l > m: m = l
			out.write('<pre><table class="wiki"><tbody>\n')
			for line in content.splitlines():
				out.write('<tr>')
				s	= re.split(r'\t+', line.rstrip())
				l	= len(s)
				l1	= l-1
				for i in range(l):
					out.write('<td')
					if i == l1 and i < m:
						out.write(f' colspan="{m-i+1}"')
					o = s[i];
					oa= o.startswith(' ')
					ob= o.endswith(' ')
					if oa and ob:
						out.write(' align="center"')
					elif oa:
						out.write(' align="right"')
					elif ob:
						out.write(' align="left"')
					out.write('>')
					out.write(escape(o.strip()))
					out.write('</td>')
				out.write('</tr>\n')
			out.write('</tbody></table></pre>\n')
			return out.getvalue()

