import cv2

video_path = 'video.MP4'

def video_to_frames(video_path):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)
    #设置帧数初始值
    count = 0
    fps = 100
    while(video.isOpened()):
        # 逐帧读取视频
        ret, frame = video.read()
        if ret == False:
            break
        if (count % fps == 0):
            cv2.imwrite('D:/pythonProject/STUDY/bishe/P/' + str(count) +'.jpg',frame)
        #保存帧为图片
        # cv2.imwrite('D:/pythonProject/STUDY/bishe/P/frame' + str(count) +'.jpg',frame)
        # # save_path = cv2.im('D:\pythonProject\STUDY\bishe\P')
        # # save_flie = save_path + 'frame'
        # # frame.save(save_flie)

        #帧数+1
        count += 1
    #释放视频对象
    video.release()

video_to_frames(video_path)
