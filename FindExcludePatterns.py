import sublime_plugin, sublime
import re

class FindExcludePatternsOMG(sublime_plugin.EventListener):

    def on_window_command(self, window, command_name, args):
        if command_name == 'show_panel' and 'panel' in args and args['panel'] == 'find_in_files' and 'FindExcludePatternsOMG' not in args:
            s = sublime.load_settings('Preferences.sublime-settings')
            exclude = list(set(list(s.get('index_exclude_patterns', []) +
                                    s.get('binary_file_patterns', []))))

            for k, v in enumerate(exclude):
                exclude[k] = exclude[k].replace('\\', '/')
            exclude = sorted(exclude)

            if 'where' in args and args['where']:
                where = args['where']
                where = where.replace('\\', '/')
                where = where.replace('*', '')
                where = re.sub('([a-z])\:/', '', where, 0, re.I)
                where = re.sub('/$', '', where)
                new_exclude = []
                for item in exclude:
                    thingy = item
                    thingy = thingy.replace('-*', '')
                    thingy = thingy.replace('*', '')
                    thingy = re.sub('([a-z])\:/', '', thingy, 0, re.I)
                    thingy = re.sub('-/([a-z])\/', '', thingy, 0, re.I)
                    thingy = re.sub('/$', '', thingy)
                    if thingy not in where:
                        new_exclude.append(item)
                args['where'] = args['where'] + ',' + ('-'+(',-'.join(new_exclude)))
            else:
                args['where'] = '-'+(',-'.join(exclude))

            args['where'] = re.sub('([a-z])\:/', '/\\1/', args['where'].replace('\\', '/'), 0, re.I)
            args['FindExcludePatternsOMG'] = 1

            return (command_name, args)