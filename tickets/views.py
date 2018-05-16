from django.http import HttpResponse
from django.shortcuts import render
import matplotlib
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
matplotlib.use('Agg')
from django import template
import PIL, PIL.Image
import matplotlib.pyplot as plt
from matplotlib import pylab
import pandas as pd
from pylab import *
import numpy as np
import datetime
import io

IMAGE_FILE_TYPES = ['png']

def index(request):
	return render(request, 'tickets/index.html')

def studio_data(request):
	df = pd.read_excel('C:/data_boy/tickets/studiodata.xlsx')
	tickets = df['# of Tickets Bought']
	studio = df['Studio']
	colors = ['#b1ffb0', '#f38630', '#a495bf', '#f4eac1', '#13e36a', '#ff9944', '#ab7694', '#89ec6b']
	fig1, ax1 = plt.subplots()
	ax1.pie(tickets, labels=studio, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
	ax1.axis('equal')
	plt.title("Breakdown by major studios:")

	buffer = io.BytesIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
	pilImage.save(buffer, "PNG")
	pylab.close()

	return HttpResponse(buffer.getvalue(), content_type="image/png")

def smaller_studios(request):
	df = pd.read_excel('C:/data_boy/tickets/studiodata (smaller).xlsx')
	tickets = df['# of Tickets Bought']
	studio = df['Studio']
	fig1, ax1 = plt.subplots()
	ax1.pie(tickets, labels=studio, autopct='%1.1f%%', shadow=True, startangle=90)
	ax1.axis('equal')
	plt.title("Breakdown by smaller studios:")

	buffer = io.BytesIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
	pilImage.save(buffer, "PNG")
	pylab.close()

	return HttpResponse(buffer.getvalue(), content_type="image/png")

def number_of_tickets(request):
	df = pd.read_excel('C:/data_boy/tickets/yearlydata.xlsx')
	fig, ax = plt.subplots()
	ticketnumbs = df['Tickets Bought']
	each_year = df['Year']
	ax.plot(each_year, ticketnumbs)
	fig.autofmt_xdate()
	plt.xlabel('Year')
	plt.ylabel('No. of Tickets Bought')
	plt.title('Amount of movie tickets I bought yearly:')

	buffer = io.BytesIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
	pilImage.save(buffer, "PNG")
	pylab.close()

	return HttpResponse(buffer.getvalue(), content_type="image/png")