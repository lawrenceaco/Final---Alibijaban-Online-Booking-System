import os
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from PyQt6.uic import loadUi
import csv
from PyQt6.QtCore import *
import pandas as pd
import time
import mysql.connector
import sqlite3


def FirstToDo():
    def CsvCreate():
        # Column names for the CSV file
        global conn
        conn = mysql.connector.connect(
            host='localhost',user='root',password='Aco11161982',database='AlibijabanOnlineBookingSystemDb')
        
        query = 'SELECT * FROM Tourist_Information'
        df = pd.read_sql(query,conn)
        
        
        # Path to the CSV file
        global csv_file_path
        csv_file_path = 'C:/Users/Lawrence/anaconda3/Library/bin/TouristInfos.csv'
        
        # Check if the CSV file already exists
        if os.path.exists(csv_file_path):
            print(f'CSV file "{ csv_file_path}" already exists.')
        else:
            # Open the file in write mode
            df.to_csv(csv_file_path,index=False)
        
            print(f'Empty CSV file "{csv_file_path}" created successfully with columns')
            
               
    
    
    class MyTableModel(QAbstractTableModel):
        def __init__(self, data, header):
            super().__init__()
            self._data = data
            self._header = header
    
        def rowCount(self, parent):
            return len(self._data)
    
        def columnCount(self, parent):
            return len(self._header)
    
        def data(self, index, role):
            if role == Qt.ItemDataRole.DisplayRole:
                row = index.row()
                col = index.column()
                value = self._data[row][col]
                return str(value)
    
            return None
    
        def headerData(self, section, orientation, role):
            if role == Qt.ItemDataRole.DisplayRole:
                if orientation == Qt.Orientation.Horizontal:
                    return self._header[section]
    
            return None
    
    
    
    
    
    class FirstWindow (QWidget):
        def __init__(self):
            super(FirstWindow,self).__init__()
            uic.loadUi("C:/Users/Lawrence/anaconda3/Library/bin/Pangalawa.ui",self)
            
            self.setWindowTitle("Alibjaban Database Manager")
            
            # self.resize(700,300)
            self.setWindowIcon(QIcon("C:/Users/Lawrence/Downloads/20210317_201504.ico"))
            
            
        # Create an empty model initially
            self.model = QStandardItemModel(self.tableView)
    
            # Set the model to the table view
            self.tableView.setModel(self.model)
    
            # Load and display the data from the CSV file
            self.load_csv_data()
    
            # Connect the button's clicked signal to a custom slot
            self.AddPushButton.clicked.connect (self.clicked)
            self.NextPushButton.clicked.connect (self.nextclicked)
            
            
        def load_csv_data(self):
            # Get the CSV file path
            csv_file_path = 'C:/Users/Lawrence/anaconda3/Library/bin/TouristInfos.csv'
    
            # Read data from the CSV file
            data = []
            with open(csv_file_path, newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    data.append(row)
    
            # Define the header for the table view
            header = data[0]
    
            # Remove the header row from the data
            data = data[1:]
    
            # Create the model
            self.model = MyTableModel(data, header)
    
            # Set the model to the table view
            self.tableView.setModel(self.model)    
            
        
            
        def clicked(self):
            csv_file_path = 'C:/Users/Lawrence/anaconda3/Library/bin/TouristInfos.csv'
        # Get the text from the QLineEdit
            text1 = self.NameLineEdit.text()
            text2 = self.NatLineEdit.text()
            text3 = self.AddressLineEdit.text()
            text4 = self.NumLineEdit.text()
            value1 = self.AgeSpinBox.value()
            value2 = self.SexComBox.currentText()
            
            if text1 and text2 and text3 and text4 and value1 and value2:
                with open(csv_file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([text1,value1,value2,text2,text3,text4])
                
                row = [text1,value1,value2,text2,text3,text4]
                self.model._data.append(row)
                self.model.layoutChanged.emit()
                
                self.NameLineEdit.clear()
                self.NatLineEdit.clear()
                self.AddressLineEdit.clear()
                self.AddressLineEdit.clear()
                self.NumLineEdit.clear()
                self.AgeSpinBox.clear()
                
                sql = "Insert Into Tourist_Information (TouristName,TouristAge,Gender,Nationality,CurrentAddress,ContactNumber) Values ('%s', '%s', '%s','%s','%s','%s')" % (text1,value1,value2,text2,text3,text4)
                cursor = conn.cursor()
                cursor.execute(sql)
                conn.commit()
                
                print(f'Tourist information appended to "{csv_file_path}" successfully.')  
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Notice!")
                msg_box.setText("Please fill in all fields!")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.addButton(QMessageBox.StandardButton.Ok)
                msg_box.exec()
                print("Please fill in all fields")
        
        def nextclicked(self):
            
            self.close()
        
        
    
    
    
    CsvCreate()
    
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        widget = FirstWindow()
        widget.show()
        sys.exit(app.exec())
        
        


def SecondToDo():
    def CsvCreate():
        # Column names for the CSV file
        columns = ['Booked Resorts', 'Resorts/Campsites', 'ArrivalDate', 'ReturnDate', 'Destination/s', 'Tour Type', 'Number of Days']
        
        # Path to the CSV file
        global csv_file_path
        csv_file_path = 'C:/Users/Lawrence/anaconda3/Library/bin/TravelInfos.csv'
        
        # Check if the CSV file already exists
        if os.path.exists(csv_file_path):
            print(f'CSV file "{ csv_file_path}" already exists.')
        else:
            # Open the file in write mode
            with open(csv_file_path, mode='w', newline='') as file:
        
                # Create a CSV writer object
                writer = csv.writer(file)
        
                # Write the column names to the CSV file
                writer.writerow(columns)
        
            print(f'Empty CSV file "{csv_file_path}" created successfully with columns: {columns}')
            
            
    
    
    CsvCreate()
    
    class SecondWindow (QWidget):
        def __init__(self):
            super(SecondWindow,self).__init__()
            uic.loadUi("C:/Users/Lawrence/anaconda3/Library/bin/Alibijaban Online Booking App.ui",self)
            
            self.setWindowTitle("Alibjaban Database Manager")
            
            # self.resize(700,300)
            self.setWindowIcon(QIcon("C:/Users/Lawrence/Downloads/20210317_201504.ico"))
            self.ProceedButton.clicked.connect(self.click)
            
        def click(self):
            csv_file = "C:/Users/Lawrence/anaconda3/Library/bin/TravelInfos.csv"
            # column_name = "Booked Resorts"
            
            # if self.BkCheckYes.checkState() == Qt.CheckState.Checked:
            #     with open(csv_file, "a", newline="") as file:
            #         writer = csv.writer(file)
            #     existing_rows = []
            #     with open(csv_file, "r") as file:
            #         reader = csv.reader(file)
            #         existing_rows = list(reader)
            #     header_row = existing_rows[0]
            #     column_index = header_row.index(column_name)
            #     for row in existing_rows[1:]:
            #         row[column_index] = "Yes"
            #         with open(csv_file, "w", newline="") as file:
            #             writer = csv.writer(file)
            #             writer.writerows(existing_rows)
                        
            
            text1 = str(self.DaysComboBox.value())
            text2 = self.TourTypes.checkedButton().text() if self.TourTypes.checkedButton() is not None else ""

            text3 = self.Destinations.checkedButton().text() if self.Destinations.checkedButton() is not None else ""

            text4 = self.DateReturn.date().toString(Qt.DateFormat.ISODate)
            button = self.BkChecks.checkedButton()
            text5 = button.text() if button is not None else ""
            value1 = self.DateArrival.date().toString(Qt.DateFormat.ISODate)
            value2 = self.CampsitesChoice.currentText()
            if text5 == 'No':
                value2 = 'Not Yet'
        
            if text1 != "" and text2 != "" and text3 != "" and text4 != "" and text5 != "" and value1 != "" and value2 != "":
                with open(csv_file_path, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([text5, value2, str(value1), str(text4), text3, text2, text1])
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Notice!")
                    msg_box.setText("Successfully Booked!")
                    msg_box.setIcon(QMessageBox.Icon.Warning)
                    msg_box.addButton(QMessageBox.StandardButton.Ok)
                    msg_box.exec()
                    print("Successfuly Booked!")
                    print("Data appended to CSV file successfully.")
                    self.close()
            else:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Notice!")
                msg_box.setText("Please fill in all fields!")
                msg_box.setIcon(QMessageBox.Icon.Warning)
                msg_box.addButton(QMessageBox.StandardButton.Ok)
                msg_box.exec()
                print("Please fill in all fields")
                    
            

            
            

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        widget = SecondWindow()
        widget.show()
        sys.exit(app.exec())



FirstToDo()
# time.sleep(1)
# SecondToDo()