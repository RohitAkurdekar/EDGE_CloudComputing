"""
sensor range is 0-50
"""


def send_alert(username, deviceid, sensor_name, sensor_value):
    print(f"Hello {username} on your {deviceid}; {sensor_name} is not working as it is sending {sensor_value} which is out of range (0-50)")
