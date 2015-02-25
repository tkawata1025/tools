# -*- coding: UTF-8 -*-

import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
from naoqi import ALProxy


global AX_l
global AX_f
global AX_r
global AX_plots
global NAOQI_memoryProxy
global LaserSV_watchDataList
global LaserVL_watchDataList
global LaserVR_watchDataList
global LaserSL_watchDataList
global LaserSF_watchDataList
global LaserSR_watchDataList

# animation
def _update_plot(i):

	dataList_sv = NAOQI_memoryProxy.getListData(LaserSV_watchDataList)
	dataList_vl = NAOQI_memoryProxy.getListData(LaserVL_watchDataList)
	dataList_vr = NAOQI_memoryProxy.getListData(LaserVR_watchDataList)
	dataList_sl = NAOQI_memoryProxy.getListData(LaserSL_watchDataList)
	dataList_sf = NAOQI_memoryProxy.getListData(LaserSF_watchDataList)
	dataList_sr = NAOQI_memoryProxy.getListData(LaserSR_watchDataList)

	#remove previous frame
	while len(AX_plots) > 0:
		AX_plots[0].remove()
		AX_plots.pop(0)

	i = 0
	while i < len(dataList_sv):
		if dataList_sv[i] != None and dataList_sv[i+1] != None:
			AX_plots.append(AX_f.scatter(dataList_sv[i], dataList_sv[i+1], color="m"))
		i = i + 2

	i = 0
	while i < len(dataList_vl):
		if dataList_vl[i] != None and dataList_vl[i+1] != None:
			AX_plots.append(AX_f.scatter(dataList_vl[i], dataList_vl[i+1], color="b"))
		i = i + 2

	i = 0
	while i < len(dataList_vr):
		if dataList_vr[i] != None and dataList_vr[i+1] != None:
			AX_plots.append(AX_f.scatter(dataList_vr[i], dataList_vr[i+1], color="g"))
		i = i + 2

	i = 0
	while i < len(dataList_sf):
		if dataList_sf[i] != None and dataList_sf[i+1] != None:
			AX_plots.append(AX_f.scatter(dataList_sf[i], dataList_sf[i+1], color="r"))
		i = i + 2

	i = 0
	while i < len(dataList_sl):
		if dataList_sl[i] != None and dataList_sl[i+1] != None:
			AX_plots.append(AX_l.scatter(dataList_sl[i], dataList_sl[i+1], color="r"))
		i = i + 2

	i = 0
	while i < len(dataList_sr):
		if dataList_sr[i] != None and dataList_sr[i+1] != None:
			AX_plots.append(AX_r.scatter(dataList_sr[i], dataList_sr[i+1], color="r"))
		i = i + 2

	#AX_l.legend(labels=("Left",))
	#AX_f.legend(labels=("Front",))
	#AX_r.legend(labels=("Right",))


if __name__ == '__main__':
	import sys
	args = sys.argv
	robotIp = "localhost"
	robotPort = 9559
	if len(args) > 1:
		robotIp = str(args[1])
	if len(args) > 2:
		robotPort = int(args[2])

	NAOQI_memoryProxy = ALProxy("ALMemory",robotIp,robotPort)

	fig =  pyplot.figure()

	AX_l = fig.add_subplot(1,3,1)
	AX_f = fig.add_subplot(1,3,2)
	AX_r = fig.add_subplot(1,3,3)

	AX_l.set_ylim([-10.0,10.0])
	AX_f.set_ylim([-10.0,10.0])
	AX_r.set_ylim([-10.0,10.0])

	AX_l.set_xlim([-10.0,10.0])
	AX_f.set_xlim([-10.0,10.0])
	AX_r.set_xlim([-10.0,10.0])

	LaserSV_watchDataList = []
	LaserVL_watchDataList = []
	LaserVR_watchDataList = []
	LaserSL_watchDataList = []
	LaserSF_watchDataList = []
	LaserSR_watchDataList = []

	for i in range(1,4):
		LaserSV_watchDataList.append("Platform/LaserSensor/Front/Shovel/Seg%02d/X/Sensor/Value" % i)
		LaserSV_watchDataList.append("Platform/LaserSensor/Front/Shovel/Seg%02d/Y/Sensor/Value" % i)


	LaserVR_watchDataList.append("Platform/LaserSensor/Front/Vertical/Right/Seg01/X/Sensor/Value")
	LaserVR_watchDataList.append("Platform/LaserSensor/Front/Vertical/Right/Seg01/Y/Sensor/Value")
	LaserVL_watchDataList.append("Platform/LaserSensor/Front/Vertical/Left/Seg01/X/Sensor/Value")
	LaserVL_watchDataList.append("Platform/LaserSensor/Front/Vertical/Left/Seg01/Y/Sensor/Value")

	for i in range(1,16):
		LaserSL_watchDataList.append("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg%02d/X/Sensor/Value" % i)
		LaserSL_watchDataList.append("Device/SubDeviceList/Platform/LaserSensor/Left/Horizontal/Seg%02d/Y/Sensor/Value" % i)
		LaserSF_watchDataList.append("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg%02d/X/Sensor/Value" % i)
		LaserSF_watchDataList.append("Device/SubDeviceList/Platform/LaserSensor/Front/Horizontal/Seg%02d/Y/Sensor/Value" % i)
		LaserSR_watchDataList.append("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg%02d/X/Sensor/Value" % i)
		LaserSR_watchDataList.append("Device/SubDeviceList/Platform/LaserSensor/Right/Horizontal/Seg%02d/Y/Sensor/Value" % i)

	AX_plots = [] 

	# start animation
	ani = animation.FuncAnimation(fig, _update_plot, frames=600, interval = 10) 
	pyplot.show()
	