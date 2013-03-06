import sublime, sublime_plugin, os, sys

__author__ = 'Hassen Ben Yeddder'
__email__ = 'hassenbenyedder@gmail.com'

class RestartCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if sys.platform == 'win32':
            os.execl(sys.executable,' ')
        else:
            path = sublime.load_settings("Restart.sublime-settings").get("path")
            if path:
                os.execl(path)
            elif sys.platform == 'darwin':
                os.execl('/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl')
            else:
                os.execl('/usr/local/sublime-text/sublime_text')
