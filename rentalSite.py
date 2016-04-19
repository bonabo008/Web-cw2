import csv
import time
from datetime import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/displayList', methods=['GET'])
def displayList():
	# f = open("static\\csv\\comments.csv", "w")
	# f.truncate()
	# f.close()
	commentsFile = 'static\\csv\\comments.csv'
	commentsList = readFile(commentsFile)
	return render_template('comments.html', commentsList = commentsList)

@app.route('/addEntry', methods = ['POST'])
def addEntry():
	commentsFile = 'static\\csv\\comments.csv'
	commentsList = readFile(commentsFile)
	
	formName = request.form[('name')]
	formComment = request.form[('comment')]
	valid = True
	
	if formName.strip() == '':
		formName = 'Anon'
	
	if formComment.strip() == '':
		valid = False
	
	if valid == True:
		newEntry = [datetime.now().strftime('%d/%m/%Y'), formName, formComment]
		commentsList.append(newEntry)
		writeFile(commentsList, commentsFile)
		return render_template('comments.html', commentsList = commentsList)
	else:
		return render_template('comments.html', valid = valid, commentsList = commentsList)

@app.route('/clearCsv', methods = ['POST'])
def clearCsv():
	f = open("static\\csv\\comments.csv", "w")
	f.truncate()
	f.close()
	return render_template('comments.html')

@app.route('/attractions')
def attractions():
    return render_template('attractions.html')

@app.route('/comments')
def comments():
    return render_template('comments.html', valid = True)

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/addBooking', methods = ['POST'])
def addBooking():
	bookingFile = 'static\\csv\\bookings.csv'
	bookingList = readFile(bookingFile)
	
	formName = request.form[('name')]
	formEmail = request.form[('email')]
	formStartDate = request.form[('startDate')]
	formEndDate = request.form[('endDate')]
	formPeople = request.form[('people')]
	formInfo = request.form[('info')]
	
	newEntry = [formName, formEmail, formStartDate, formEndDate, formPeople, formInfo]
	bookingList.append(newEntry)
	
	writeFile(bookingList, bookingFile)
	return render_template('booking.html')

def readFile(aFile):
	with open(aFile, 'r') as inFile:
		reader = csv.reader(inFile)
		commentsList = [row for row in reader]
	return commentsList

def writeFile(aList, aFile):
	with open(aFile, 'w', newline='') as outFile:
		writer = csv.writer(outFile)
		writer.writerows(aList)
	return



if __name__ == '__main__':
    app.run(debug = True)