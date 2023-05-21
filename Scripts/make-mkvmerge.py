# Генерация команд для mkvmerge для перепаковки эпизодов из релиза Simu
# А именно, выкидываем корейскую озвучку

cmd_line = r'D:\Distrib\Video\mkvtoolnix\mkvmerge.exe --ui-language ru --priority lower --output ^"D:\_out\Candy-Candy_DVD_Ep%03d.mkv^" --audio-tracks 1 --language 0:ja --display-dimensions 0:960x720 --language 1:ja ^"^(^" ^"D:\Anime\Candy-Candy ^(DVD^)\Episodes\Candy-Candy_DVD_Ep%03d_Simu_2audio.mkv^" ^"^)^" --track-order 0:0,0:1'

for n in range(1, 115+1):
    print(cmd_line % (n, n))
