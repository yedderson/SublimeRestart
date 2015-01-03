import sublime, sublime_plugin, os, sys, subprocess

__author__ = 'Hassen Ben Yeddder'
__email__ = 'hassenbenyedder@gmail.com'

class RestartCommand(sublime_plugin.WindowCommand):
    def run(self):
        if sys.platform == 'win32':
            if sublime.version()[:1]=='3':
                self.window.run_command('exit')
                subprocess.call(os.path.join(os.getcwd(), 'sublime_text.exe'))
            else:
                os.execl(sys.executable,' ')
                
        elif sys.platform == 'darwin':
            #Restarting ST3 on mac
            if sublime.version()[:1]=='3':
                self.window.run_command('exit')
                subprocess.call(os.path.join(os.getcwd(), 'subl'))
            else:
                os.execl(os.path.join(os.getcwd(), 'subl'))
                
        else:
            #Restarting ST3 on linux
            if sublime.version()[:1]=='3':
                self.window.run_command('exit')
                subprocess.call(os.path.join(os.getcwd(), 'sublime_text'))
            else:
                os.execl(os.path.join(os.getcwd(), 'sublime_text'))
