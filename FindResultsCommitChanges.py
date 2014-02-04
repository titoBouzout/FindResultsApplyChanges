# coding=utf8
import sublime, sublime_plugin, re

class FindResultsCommitChanges(sublime_plugin.WindowCommand):
	def run(self):
		for view in sublime.active_window().views():
			if view.name() == 'Find Results':

			# get "Find Results" buffer contents

				_content = view.substr(sublime.Region(0, view.size())).split("\n")
				# pop the header "Searching 2 files for "aa" and the empty line
				_content.pop(0)
				_content.pop(0)

				# get an iter
				_content = iter(_content)

				# regexps
				_match_numbered = re.compile(r'^\s+([0-9]+|\.+$)', re.I);
				_match_changed = re.compile(r'^\s+[0-9]+\:', re.I);

				# the first file name
				file_name = str(re.sub(r'\:$', '', next(_content)))

				# the list of changes to apply
				changes = {}

			# get the changes

				for line in iter(_content):
					l = str(line)
					#print('about file:'+file_name);
					while _match_numbered.match(l):
						if _match_changed.match(l):
							#print('have to change'+l)
							try:
								changes[file_name]
							except:
								changes[file_name] = {}
							# hold the change in the file name with line number as index and content as value
							changes[file_name][int(re.sub(r"^\s+([0-9]+)\:.*", "\\1", l))-1]  = re.sub(r"^\s+[0-9]+\: (.*)", '\\1', l)
						line = next(_content);
						l = str(line)
					file_name = re.sub(r'\:$', '', l)

				# print(changes);

			# apply changes

				for f in changes:
					f = f.strip();
					if f:
						print('about modifying file '+f)
						content = self.read(f).split('\n');
						for k in changes[f].keys():
							k = int(k)
							# print('Line number: '+k)
							# print('Has new value: '+changes[f][k]);
							content[k] = changes[f][k]
						self.write(f, "\n".join(content))


	def is_enabled(self):
		for view in sublime.active_window().views():
			if view.name() == 'Find Results':
				return True
		return False

	def read(self, name):
		return open(name, 'r', newline='').read()

	def write(self, name, content):
		open(name, 'w+', encoding='utf8', newline='').write(str(content))