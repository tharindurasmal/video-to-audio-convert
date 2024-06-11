import moviepy.editor
name = input('Enter your video name with extension: ')
save = input('Give name to your audio file: ')
video = moviepy.editor.VideoFileClip( name )
audio = video. audio
audio.write_audiofile (save+'.mp3')
