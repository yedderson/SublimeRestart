import sublime, sublime_plugin, os, sys, subprocess

__author__ = 'Hassen Ben Yeddder'
__email__ = 'hassenbenyedder@gmail.com'

class RestartCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path = sublime.load_settings("Restart.sublime-settings").get("path")
        
        if sys.platform == 'win32':
            if sublime.version()[:1]=='3':
                subprocess.call('taskkill /im sublime_text.exe /f & cmd /C "'+ os.path.join(os.getcwd(), 'sublime_text.exe') + '"', shell=True)
            else:
                os.execl(sys.executable,' ')
        elif sys.platform == 'darwin':
            #Restarting ST3 on mac
            if sublime.version()[:1]=='3':
                subprocess.call("pkill subl && "+ os.path.join(os.getcwd(), 'subl'), shell=True)
            else:
                os.execl(os.path.join(os.getcwd(), 'subl'))
        else:
            #Restarting ST3 on linux
            if sublime.version()[:1]=='3':
                subprocess.call("pkill 'sublime_text' && "+ os.path.join(os.getcwd(), 'sublime_text'), shell=True)
                
            else:
                os.execl(os.path.join(os.getcwd(), 'sublime_text'))
