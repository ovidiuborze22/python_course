# plotting time intervals from the data generated by the webcam
from motion_detector import df
from bokeh.plotting import figure,output_file,show


p=figure(x_axis_type='datetime',height=250, width=800,sizing_mode='stretch_width',title="Motion Graph")
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker.desired_num_ticks=1


q=p.quad(left=df["Start"],right=df["End"],bottom=0,top=1,color="green")

output_file("python_course/python_apps/App2_Controlling_the_Webcam_and_Detecting_Objects/Graph.html")
show(p)

