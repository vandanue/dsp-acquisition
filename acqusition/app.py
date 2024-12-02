from PySide6.QtCore import Slot, QObject, Signal, QThread, QFile
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIntValidator
import serial.tools
import serial.tools.list_ports
from ui.main_ui import Ui_MainWindow

import serial

class ReadSerial(QObject) :

    dataReady = Signal(bytearray)

    def __init__(self, portname : str, baudrate : int, parent = None):
        super().__init__(parent)

        self._portname = portname
        self._baudrate = baudrate

        self._is_looping = False

    def run(self):
        self.ser = serial.Serial(self._portname,self._baudrate,timeout=10)

        self._is_looping = True 

        self.ser.flush()

        while self._is_looping:
            data = self.ser.read_until(expected=b"\r\n")
            #print(data)
            self.dataReady.emit(data)

        self.ser.close()
        self.ser = None

    def stop(self):
        self._is_looping = False



class MainWindow (QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnStart.clicked.connect(self.start_handler)
        self.ui.btnStop.clicked.connect(self.stop_handler)

        # Get all Port serial
        port_info = serial.tools.list_ports.comports(True)
        
        list_port = []
        for port in port_info:
            list_port.append(port.device)

        self.ui.cmbPort.addItems(list_port)
        self.ui.txtBaudrate.setValidator(QIntValidator(0,100000,self))

        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)


    @Slot()
    def start_handler(self):
        print("Start Receiving data")

        # Deklarasi filename, Jika nama tidak diganti maka file akan ditimpa
        self.file = open(self.ui.txtFilename.text(),'a+')


        #Deklarasi Read serial worker
        self.worker = ReadSerial(self.ui.cmbPort.currentText(),
                                 int(self.ui.txtBaudrate.text()))
        
        self.worker.dataReady.connect(self.data_handler)
        
        # Deklarasi Threa
        self.thread = QThread()

        #Pindahkan Readserial ke Thread
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.thread.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        # Clear data
        self.ui.txtData.clear()

        self.ui.btnStart.setEnabled(False)
        self.ui.btnStop.setEnabled(True)

        self.thread.start()


    @Slot()
    def stop_handler(self):
        print("Stoping Acquisition data")

        self.ui.btnStart.setEnabled(True)
        self.ui.btnStop.setEnabled(False)

        self.worker.stop()
        self.file.close()

    @Slot()
    def data_handler(self,data : bytes):
        #print(data)
        data_str = data.decode('utf-8')
        #print(data_str)
        data_str = data_str.replace('\r', '').replace('\n', '')
        if (data_str.split(',')[0][1]) != '.':
            return
        
        self.ui.txtData.appendPlainText(data_str)
        self.file.write(data_str + '\n')

        

if __name__ == '__main__' :
    import sys 

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()