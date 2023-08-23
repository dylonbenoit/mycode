#!/usr/bin/env python3

import requests
import datetime

URL = "http://api.open-notify.org/iss-now.json"

iss_api = requests.get(URL).json()

def time_convert():

    timestamp_epoch = iss_api['timestamp']
    #dtime = date_time.strftime(timestamp_epoch)
    dtime = datetime.datetime.fromtimestamp(timestamp_epoch)
    

def main():
    #time_convert()
    #print(iss_api)
    dtime = time_convert()
    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {dtime}\nLon: {iss_api['iss_position']['longitude']}")
    print(f"Lat: {iss_api['iss_position']['latitude']}")


if __name__ == "__main__":
    main()