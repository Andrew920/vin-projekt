import serial
import mysql.connector

import time

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="arduino"
)

cursor = db.cursor()

try:
    while True:
        data = serial.Serial(port='COM5', baudrate=9600).readline()
        data = str(data).strip()

        temp, hum, light = data.split("&")

        temp = temp[2:-1]
        hum = hum.split('.')[0]
        light = light[:-5]

        test = serial.Serial(port='COM5', baudrate=9600).readline()

        sql = "INSERT INTO data (time, temp, hum, light) VALUES (%s, %s, %s, %s)"
        val = (str(int(time.time())), temp, hum, light)
        cursor.execute(sql, val)
        db.commit()
        print(data)
        print(test)
        print(temp, hum, light)
        time.sleep(10)


except:
    cursor.close()
