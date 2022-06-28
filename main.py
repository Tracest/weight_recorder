import os
import time
import datetime
import tkinter as tk
import tkinter.messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

text_one = '说明:在第一个框输入今天的体重，第二个框输入今天的日期'

global glob_str 

def confirm_weight(entryw, entryd):

    if entryw.get() and entryd.get():

        if os.path.exists('weight_recorder.txt'):
            with open('weight_recorder.txt','a') as file_weight_append:
                file_weight_append.write(',')
                file_weight_append.write(entryw.get())

            with open('date_recorder.txt','a') as file_date_append:
                file_date_append.write(',')
                file_date_append.write(entryd.get())
                

            with open('weight_recorder.txt','r') as file_weight_read:
                weight_str = file_weight_read.read()
                weight_y = weight_str.split(',')
                weight_y = list(map(float,weight_y))

            with open('date_recorder.txt','r') as file_date_read:
                date_str = file_date_read.read()
                date_x = date_str.split(',')
                date_x = list(map(str,date_x))
 
            image = plt.figure(figsize=(15,8))
            image_plot = image.add_subplot()
            canvas_spice = FigureCanvasTkAgg(image, window)
            canvas_spice.get_tk_widget().pack()
            plt.ylim((65,95))
            plt.plot(date_x, weight_y)
            
            for d,w in zip(date_x, weight_y):
                plt.text(d ,w ,w ,ha='center', va='bottom', fontsize=8)
                        
        else:
            with open('weight_recorder.txt','w') as file_weight_write:
                file_weight_write.write(entryw.get())

            with open('date_recorder.txt','w') as file_date_write:
                file_date_write.write(entryd.get())

            tk.messagebox.askquestion(title='Tips', message='一个点就不画图了，明天输入后画图') 
    else:

        tk.messagebox.askquestion(title='Error', message='请输入体重与日期') 
    
    entryw.delete(0, tk.END)
    entryd.delete(0, tk.END)



if __name__ == '__main__':

    window = tk.Tk()
    window.title('Weight recorder')

    label = tk.Label(window, text=text_one)
    label.pack()

    entryw = tk.Entry(window)
    entryw.pack()

    entryd = tk.Entry(window)
    entryd.pack()

    confirm_button = tk.Button(window, text='confirm', command=lambda:confirm_weight(entryw, entryd))
    confirm_button.pack()

    label = tk.Label(window)
    label.pack()

    window.mainloop()