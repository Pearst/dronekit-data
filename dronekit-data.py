from fastapi import Body, FastAPI, APIRouter

app = FastAPI()
router = APIRouter()


data = "Get all vehicle attribute values:\nAutopilot Firmware version: APM:Copter-4.0.1\nMajor version number: 4\nMinor version number: 0\nPatch version number: 1\nRelease type: rc\nRelease version: 0\nStable release?: True\nAutopilot capabilities\nSupports MISSION_FLOAT message type: True\nSupports PARAM_FLOAT message type: True\nSupports MISSION_INT message type: True\nSupports COMMAND_INT message type: True\nSupports PARAM_UNION message type: False\nSupports ftp for file transfers: True\nSupports commanding attitude offboard: True\nSupports commanding position and velocity targets in local NED frame: True\nSupports set position + velocity targets in global scaled integers: True\nSupports terrain protocol / data handling: True\nSupports direct actuator control: False\nSupports the flight termination command: True\nSupports mission_float message type: True\nSupports onboard compass calibration: True\nGlobal Location: LocationGlobal:lat=0.0,lon=0.0,alt=None\nGlobal Location (relative altitude): LocationGlobalRelative:lat=0.0,lon=0.0,alt=0.0\nLocal Location: LocationLocal:north=None,east=None,down=None\nAttitude: Attitude:pitch=0.0,yaw=0.0,roll=0.0\nVelocity: [0.0, 0.0, 0.0]\nGPS: GPSInfo:fix=0,num_sat=0\nGimbal status: Gimbal: pitch=None, roll=None, yaw=None\nBattery: None\nEKF OK?: False\nLast Heartbeat: 0.375\nRangefinder: Rangefinder: distance=None, voltage=None\nRangefinder distance: None\nRangefinder voltage: None\nHeading: 0\nIs Armable?: False\nSystem status: ACTIVE\nGroundspeed: 0.0\nAirspeed: 0.0\nMode: STABILIZE\nCALLBACK: Attitude changed to Attitude:pitch=0.0,yaw=0.0,roll=0.0\nCALLBACK: Attitude changed to Attitude:pitch=0.0,yaw=0.0,roll=0.0\nCALLBACK: Attitude changed to Attitude:pitch=0.0,yaw=0.0,roll=0.0\nRemove Vehicle.attitude observer\nCALLBACK: (last_heartbeat): 0.625\nCALLBACK: (attitude): Attitude:pitch=0.0,yaw=0.0,roll=0.0\nCALLBACK: (location.global_relative_frame): LocationGlobalRelative:lat=0.0,lon=0.0,alt=0.0\nCALLBACK: (location): <dronekit.Locations object at 0x000001CB7FC0B310>\nCALLBACK: (velocity): [0.0, 0.0, 0.0]\nCALLBACK: (heading): 0\nCALLBACK: (airspeed): 0.0\nCALLBACK: (groundspeed): 0.0\nCALLBACK: (channels): {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}\nCALLBACK: (last_heartbeat): 0.6880000000001019\nCALLBACK: (last_heartbeat): 0.0\nCALLBACK: (last_heartbeat): 0.06300000000010186\nCALLBACK: (last_heartbeat): 0.125\nCALLBACK: (attitude): Attitude:pitch=0.0,yaw=0.0,roll=0.0\nCALLBACK: (location.global_relative_frame): LocationGlobalRelative:lat=0.0,lon=0.0,alt=0.0\nCALLBACK: (location): <dronekit.Locations object at 0x000001CB7FC0B310>\nCALLBACK: (velocity): [0.0, 0.0, 0.0]\nCALLBACK: (heading): 0\nCALLBACK: (airspeed): 0.0\nCALLBACK: (groundspeed): 0.0\nCALLBACK: (channels): {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}\nCALLBACK: (last_heartbeat): 0.18800000000010186\nCALLBACK: (last_heartbeat): 0.0\nCALLBACK: (last_heartbeat): 0.06300000000010186\nCALLBACK: (last_heartbeat): 0.125\nCALLBACK: (attitude): Attitude:pitch=0.0,yaw=0.0,roll=0.0\nCALLBACK: (location.global_relative_frame): LocationGlobalRelative:lat=0.0,lon=0.0,alt=0.0\nCALLBACK: (location): <dronekit.Locations object at 0x000001CB7FC0B310>\nCALLBACK: (velocity): [0.0, 0.0, 0.0]\nCALLBACK: (heading): 0\nCALLBACK: (airspeed): 0.0\nCALLBACK: (groundspeed): 0.0\nCALLBACK: (channels): {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}\nCALLBACK: (last_heartbeat): 0.18800000000010186\nCALLBACK: (last_heartbeat): 0.25\nCALLBACK: (last_heartbeat): 0.31300000000010186\nCALLBACK: (last_heartbeat): 0.375\nCALLBACK: (attitude): Attitude:pitch=0.0,yaw=0.0,roll=0.0\nCALLBACK: (location.global_relative_frame): LocationGlobalRelative:lat=0.0,lon=0.0,alt=0.0\nCALLBACK: (location): <dronekit.Locations object at 0x000001CB7FC0B310>\nCALLBACK: (velocity): [0.0, 0.0, 0.0]\nCALLBACK: (heading): 0\nCALLBACK: (airspeed): 0.0\nCALLBACK: (groundspeed): 0.0\nCALLBACK: (channels): {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}\nCALLBACK: (gps_0): GPSInfo:fix=0,num_sat=0\nCALLBACK: (last_heartbeat): 0.43800000000010186\nCALLBACK: (last_heartbeat): 0.5\nCALLBACK: (last_heartbeat): 0.5630000000001019\nRemove Vehicle attribute observer\nCompleted"
list = []

print("pearsted")

f = open("data.txt", "r")
for x in f:
    try:
        i1 = x.index(':')
        i2 = x.index('\n')

        firstp = x[:i1]
        scndp = x[i1:]

        data1 = {firstp+scndp}
        data2 = x[:i2]
        list.append(data2)

    except:
        pass


@app.get("/")
async def dronekit_data():
    return list



