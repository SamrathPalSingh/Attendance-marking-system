#starts the webserver for student interface(index.html) and opens the teacher interface(teacher_webpage.html)
import threading
import webbrowser
import simple_http_server_file as shsf
#thread = threading.Thread(target='shsf.startServer', args = [])
webbrowser.open('teacher_webpage.html')
shsf.startServer()

