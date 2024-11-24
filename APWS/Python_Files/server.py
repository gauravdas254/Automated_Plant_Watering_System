from flask import Flask, render_template, request
import serial
from apws import*

buzzOnce = 0
watered = 0

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/result',methods = ['POST','GET'])
def result():
    if request.form['submit_button'] == 'Periwinkle':
        output = apws(700, 10)
        if output == "plantWatered":
            wateredChry = "Your Periwinkle is watered."
            return render_template('index.html',ackMsg = wateredChry)

        elif output == "noWater":
            noWaterChry = "No water in tank, please refill."
            return render_template('index.html', ackMsg = noWaterChry)

    elif request.form['submit_button'] == 'Rose':
        output = apws(700, 15)
        if output == "plantWatered":
            wateredRose = "Your Rose is watered"
            return render_template('index.html', ackMsg = wateredRose)

        elif output == "noWater":
            noWaterRose = "No water in tank, please refill."
            return render_template('index.html', ackMsg = noWaterRose)

    elif request.form['submit_button'] == 'Succulent':
        output = apws(700, 20)
        if output == "plantWatered":
            wateredSucculent = "Your Succulent is watered"
            return render_template('index.html', ackMsg = wateredSucculent)

        elif output == "noWater":
            noWaterSucculent = "No water in tank, please refill."
            return render_template('index.html', ackMsg = noWaterSucculent)


    else:
        return render_template('index.html', ackMsg = "Invalid")

@app.route('/sensorVal', methods = ['POST', 'GET'])
def sensorVal():
    sml = getSml()
    wl = getWl()
    saveSml(str(sml))
    saveWl(str(wl))
    moistureLevel = readSml()
    waterLevel = readWl()
    return render_template('index.html', moistureLevel = moistureLevel, waterLevel = waterLevel)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")
