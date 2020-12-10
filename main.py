# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess as sp
from rescale import resc


def cut_it():
    sp.run("ffprobe bbb.mp4 2>&1 | grep 'Duration'", shell=True)
    time = str(input('Choose the time to start (mm:ss):'))
    line1 = 'ffmpeg -i bbb.mp4 -ss 00:' + time + ' -t 00:00:10 -c copy cut.mp4'
    sp.run(line1, shell=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opt = int(input('    ~~~~~~  MAIN MENÚ  ~~~~~~\n\n'
                 'Choose a function to aply to the BBB video:'
                 '\n 1. Cut 10 seconds of the video.'
                 '\n 2. Overlay the YUV histogram'
                 '\n 3. Rescale the video'
                 '\n 4. Change the audio to mono\n \nChoose a number between 1 and 4: '))
    if opt == 1:
        cut_it()
    elif opt == 2:
        line = 'ffplay bbb.mp4 -vf "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay"'
        sp.run(line, shell=True)
    elif opt == 3:
        resc()
    elif opt == 4:
        line = 'fmpeg -i bbb.mp4 -ac 1 bbb_mono.mp4'
        sp.run(line, shell=True)
    else:
        print('Try again with another number')
        exit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
