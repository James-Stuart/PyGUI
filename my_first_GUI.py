'''
The idea of this script is to start making a basic python GUI for the picoscope.
This way we will be able to look at live plots from the pioscope without having to open the app. 

This will use the PyGUI framework which I have no idea how to use, good luck!
Goal: Make GUI that shows a matplotlib plot (or some other plot) and have GUI controls to set amp, time settings.
'''
import dearpygui.dearpygui as dpg
import numpy as np
#import matplotlib.pyplot as plt

#==== Make a text bo that live updates
class data_values():
    clicks = 0

def save_callback(sender, value, user_data):
    # print("Clicked")
    data_values.clicks +=1

    #Update text
    dpg.set_value(user_data, f'Number of clicks: {data_values.clicks:.0f}')
data = data_values()
#====


#Lets add a plot
x_arr = np.linspace(0,2*np.pi,100)
def get_y(x_arr):
    return np.sin(x_arr)+np.random.rand(x_arr.size)*0.05

#ALways create context and viewport and setup the GUI
dpg.create_context() #Start point
dpg.create_viewport(width=600, height=400)#make the window
dpg.setup_dearpygui()


with dpg.window(label="Example Window", width=600, height=400):
    dpg.add_text("Hello world")
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")
   
    text_control = dpg.add_text("Number of clicks: 0")
    dpg.add_button(label="Clicker", callback=save_callback, user_data = text_control)

    with dpg.plot(label="Line Series", height=200, width=400):

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
    
        with dpg.plot_axis(dpg.mvYAxis, label="y"):
            y_arr = get_y(x_arr)
            # series belong to a y axis
            dpg.add_line_series(x_arr, y_arr, label="sin(x)", user_data = text_control)
                   

#Always show the viewport, start the GUI and destroy context
dpg.show_viewport()


#Render loop <-- handled by start_dearpygui but sommetimes needed
#for calling commands that run every frame (like a plot?)
dpg.start_dearpygui() #<--- is replaced by v.
# while dpg.is_dearpygui_running():
#     print('This will run every frame.')
#     dpg.render_dearpygui_frame()

dpg.destroy_context()