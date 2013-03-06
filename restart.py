import sublime, sublime_plugin, os, sys

__author__ = 'Hassen Ben Yeddder'
__email__ = 'hassenbenyedder@gmail.com'

class RestartCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if sys.platform == 'win32':
            os.execl(sys.executable,' ')
        else:
            os.execv(sublime.load_settings("Restart.sublime-settings").get("path"),[])
