from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import date
from datetime import datetime
import locale
import mysql.connector
import math
import time

def monitor(request):
	template = loader.get_template('index.html')
	cas = datetime.now()
	locale.setlocale(locale.LC_TIME, "sl_SE")
	podatki = database_data()
	temp = [i[1] for i in podatki]
	hum = [i[2] for i in podatki]
	light = [i[3] for i in podatki]

	context = {
		'datum': date.today(),
		'vlaga': hum[0],
		'temperatura': temp[0],
		'dan': cas.strftime("%A").upper(),
		'ura': cas.strftime("%H:%M"),
		'svetlost': svetlost(light[0]),
		'avg_hum': int(sum(hum) / len(hum)),
		'max_hum': max(hum),
		'min_hum': min(hum),
		'avg_temp': int(sum(temp) / len(temp)),
		'max_temp': max(temp),
		'min_temp': min(temp),
		'podatki': get_nazaj(podatki),
	}

	
	return HttpResponse(template.render(context, request))

def database_data():
	db = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="arduino"
	)

	cursor = db.cursor()
	cursor.execute("SELECT time, temp, hum, light FROM data ORDER BY time DESC LIMIT 2200;")
	podatki = cursor.fetchall()

	db.close()

	return podatki

def get_nazaj(podatki):
	ura = math.floor((int(time.time()) % 86400) /3600)
	podatki = [(math.floor((i[0] % 86400) /3600), i[1]) for i in podatki]
	now = int(time.time())

	rezultat = ["?"] *6
	for r in range(6):
		temp = [i[1] for i in podatki if i[0] == ura - r]
		rezultat[r] =  (ura + 2 - r) , ("??" if len(temp) == 0 else math.floor( sum(temp) / len(temp) ))
		
	print(rezultat)
	return rezultat


def svetlost(light):
	if (light < 10):
		return "Noč"
	elif (light < 200):
		return "Temno"
	elif (light < 500):
		return "Normalno"
	elif (light < 800):
		return "Svetlo"
	else:
		return "Zelo svetlo"

