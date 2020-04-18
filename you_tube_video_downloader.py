import pytube


def get_details(stream):
    v_list = str(stream).split()
    v_list.pop(0)
    v_list.pop()
    details = {}
    for x in v_list:
        details[x[:x.index("=")]] = eval(x[x.index("=") + 1:])

    return details


link = pytube.YouTube(input("Enter the Link: "))
video = link.streams.filter(progressive=True)
i = 1
for v_format in video:
    video_details = get_details(v_format)
    print(i, ".", ' , '.join(['Format : ' + video_details['mime_type'], 'Resolution : ' + video_details['res'],
                              'FPS : ' + video_details['fps']]))
    i += 1

video_num = int(input("Enter the number for the video: "))

video[video_num].download(input("Enter the download path: ").replace("\\", '\\\\'))



