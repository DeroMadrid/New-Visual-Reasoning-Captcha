from subprocess import call

path = "C:/Users/Dero/Desktop/1.mp4"
path1 = "C:/Users/Dero/Desktop/2.mp4"
command = "ffmpeg -i %s.mp4 %s.mp4" % (path, path1)
call(command.split())
