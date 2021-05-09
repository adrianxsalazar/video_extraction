# Importing all necessary libraries
import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--video', type=str, default='image', help='initial image')
opt = parser.parse_args()


#Get the video
cap = cv2.VideoCapture(opt.video)

#get path and extension of the video and the path of the results file.
video_root,video_extension = os.path.splitext(opt.video)
results_txt_path = opt.video.replace(video_extension, ".txt")


#Extrac data from the video
length = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps    = cap.get(cv2.CAP_PROP_FPS)


#Write the results into a txt file in the same directory as the video.
file2write=open(results_txt_path,'w')
file2write.write("The lenght of the video frames is "+str(length)+" \n")
file2write.write("The width of the video frames is "+str(width)+" \n")
file2write.write("The total number of frames is "+str(frames)+' \n')
file2write.write("The fps of the video are "+str(fps)+' \n')
file2write.close()
