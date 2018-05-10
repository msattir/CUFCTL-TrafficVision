import cv2
import os

image_folder = 'data/inference_output/MVI_40714'
video_name = 'video01.avi'

images = sorted([img for img in os.listdir(image_folder) if img.endswith(".png")])
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*"MJPG"), 25, (width, height))

for image in images:
	# print(image)
	video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()