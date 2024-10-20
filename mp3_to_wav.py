from moviepy.editor import VideoFileClip, AudioFileClip

# Загрузка видео и аудио файлов
video = VideoFileClip("may_demo.mp4")
audio = AudioFileClip(r"C:\intern\GeneFace\KENDALL JENNER.wav")

# Наложение аудио на видео
final_video = video.set_audio(audio)

# Сохранение результата
final_video.write_videofile("output.mp4", codec="libx264", audio_codec="aac")
