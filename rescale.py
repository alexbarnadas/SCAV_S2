import subprocess as sp


def resc():
    size_id = int (
        input ('Available sizes:\n1. 720p\n2. 480p\n3. 360x240\n4. 160x120 \nChoose a number between 1 and 4: '))
    size = 'Error'
    if size_id == 1:
        size = '1280x720'
    elif size_id == 2:
        size = '854x480'
    elif size_id == 3:
        size = '360x240'
    elif size_id == 4:
        size = '160x120'
    else:
        print ('Try again with another number')
        exit ()

    line = 'ffmpeg -i bbb.mp4 -s ' + size + ' -c:a copy resize_' + size + '.mp4'
    sp.run (line, shell=True)
