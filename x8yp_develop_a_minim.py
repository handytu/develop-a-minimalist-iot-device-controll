# x8yp_develop_a_minim.py

# Import required libraries
import tkinter as tk
import serial
import time

# Define IoT device controller class
class IoTDeviceController:
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.serial_connection = serial.Serial(serial_port, 9600, timeout=1)

    def send_command(self, command):
        self.serial_connection.write(command.encode())

    def read_data(self):
        return self.serial_connection.readline().decode().strip()

# Create GUI
class GUI:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="IoT Device Controller")
        self.label.pack()

        self.entry = tk.Entry(self.frame)
        self.entry.pack()

        self.send_button = tk.Button(self.frame, text="Send", command=self.send_command)
        self.send_button.pack()

        self.read_button = tk.Button(self.frame, text="Read", command=self.read_data)
        self.read_button.pack()

        self.output_label = tk.Label(self.frame, text="")
        self.output_label.pack()

    def send_command(self):
        command = self.entry.get()
        self.controller.send_command(command)
        self.output_label.config(text="Sent: " + command)

    def read_data(self):
        data = self.controller.read_data()
        self.output_label.config(text="Received: " + data)

# Create controller and GUI
controller = IoTDeviceController('COM3')
root = tk.Tk()
gui = GUI(root, controller)

# Run GUI
root.mainloop()