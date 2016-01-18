import sublime_plugin, sublime
import fnmatch

class FindExcludePatternsOMG(sublime_plugin.EventListener):

    def on_window_command(self, window, command_name, args):
        if command_name == 'show_panel' and 'panel' in args and args['panel'] == 'find_in_files' and 'FindExcludePatternsOMG' not in args:
            s = sublime.load_settings('Preferences.sublime-settings')
            exclude = list(set(list(s.get('index_exclude_patterns', []) +
                                    s.get('binary_file_patterns', []) +
                                    s.get('find_exclude_patterns', []))))

            if 'where' in args:
                # if the WHERE argument is present then remove from the exlusion list any of these item that matches WHERE we want to find.
                new_exclude = []
                for item in exclude:
                    if not args['where'] or (not fnmatch.fnmatch(args['where'].replace('\\', '/').replace('//', '/'), item) and not fnmatch.fnmatch(args['where'].replace('\\', '/').replace('//', '/')+'/', item)):
                        new_exclude.append(item)
                args['where'] = args['where'] + ',' + ('-'+(',-'.join(new_exclude)))
            else:
                args['where'] = '-'+(',-'.join(exclude))

            args['FindExcludePatternsOMG'] = 1

            return (command_name, args)