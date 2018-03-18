import cv2
import timeit
import numpy
start_time=timeit.default_timer()
myimg = cv2.imread('/home/pi/colourdetect/images/download4.jpg')
avg_color_per_row = numpy.average(myimg, axis=0)
avg_color = numpy.average(avg_color_per_row, axis=0)
sum=0
for i in avg_color:
    sum+=i
print "Unique Identity for colour detection :",
print sum
elapsed_time=timeit.default_timer()-start_time
print "Time elapsed in average colour detection :",
print elapsed_time,
print "in seconds"
