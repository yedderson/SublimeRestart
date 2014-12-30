import sublime, sublime_plugin, os, sys, subprocess

__author__ = 'Hassen Ben Yeddder'
__email__ = 'hassenbenyedder@gmail.com'

class RestartCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path = sublime.load_settings("Restart.sublime-settings").get("path")
        
        if path:
            os.execl(path)
        elif sys.platform == 'win32':
            if sublime.version()[:1]=='3':
                subprocess.call('taskkill /im sublime_text.exe /f & cmd /C "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"', shell=True)
            else:
                os.execl(sys.executable,' ')
        elif sys.platform == 'darwin':
            #Restarting ST3 on mac
            if sublime.version()[:1]=='3':
                subprocess.call("pkill subl && /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl", shell=True)
            else:
                os.execl('/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl')
        else:
            #Restarting ST3 on linux
            if sublime.version()[:1]=='3':
                subprocess.call("pkill 'sublime_text' && /opt/sublime_text/sublime_text", shell=True)
                
            else:
                os.execl('/usr/local/sublime-text/sublime_text')
