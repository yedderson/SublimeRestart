import sublime, sublime_plugin, os, sys

__author__ = 'Hassen Ben Yeddder'
__email__ = 'hassenbenyedder@gmail.com'

class RestartCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        os.execl(sys.executable,' ') # magic :)
