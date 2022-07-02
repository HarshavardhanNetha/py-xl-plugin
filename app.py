from ast import Pass
from flask import Flask, render_template, request
import csv
import mysql.connector

import pandas as pd

app = Flask(__name__)


def write_to_db(uploaded_file):
    pass
    # firebase ki rayali
    # dataBase = mysql.connector.connect(
    # host ="localhost",
    # user ="root",
    # passwd ="",
    # database = "gfg"
    # )

    # cursorObject = dataBase.cursor()
    
    # print("creating table")

    # studentRecord = """CREATE TABLE CSVDATA (
    #                 x1 INT NOT NULL,
    #                 x2 INT NOT NULL,
    #                 x3 INT NOT NULL,
    #                 x4 INT NOT NULL
    #                 )"""
    
    # print("table created")

    # cursorObject.execute(studentRecord)
    
    # sql = "INSERT INTO CSVDATA (x1,x2,x3,x4)\
    # VALUES (%s, %s, %s, %s)"

    # for i in uploaded_file:
    #     cursorObject.execute(sql, tuple(i))
    #     dataBase.commit()
    
    # dataBase.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['csvfile']
        print(file)
        data = []

        #filepath = os.path.join('files',file.filename)
        #file.save(filepath)
        with open(file) as f:
            csvfile = csv.reader(f)
            for row in csvfile:
                data.append(row)

        #data = {'x1':['One','Two'],'x2':['One','Two']}
        #data = [['xl','x2'],[1,2]]

        #cell_obj = sheet_obj.cell(row = 1, column = 1)
        #print(cell_obj.value)
        print(data)
        datalist = data[1:]
        data = pd.DataFrame(data)
        print(data)
        data.to_csv("files/"+file,  header=False, index=False)

        # write_to_db(datalist)
        return render_template('data.html', data=data.to_html(header=False, index = False))


if __name__ == '__main__':
    app.run(debug=True)


    #https://www.youtube.com/watch?v=tJKHrLzcopo