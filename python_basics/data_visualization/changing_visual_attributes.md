# **Changing Visual Attributes**
Once you have built a basic plot, you can customize its visual attributes, including changing the **title** color and font, adding labels for **xaxis** and **yaxis**, changing the color of the axis ticks, etc. All these properties are illustrated in the diagram below:

![](https://img-c.udemycdn.com/redactor/raw/2018-02-20_12-58-41-61fde32e445923113a5aa9948679621a.png)

And here is the code if you want to play around with it:
```py
from bokeh.plotting import figure, output_file, show
p = figure(plot_width=500, plot_height=400, tools = 'pan, reset')
p.title.text = "Earthquakes"
p.title.text_color = "Orange"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.yaxis.minor_tick_line_color = "Yellow"
p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"
p.circle([1,2,3,4,5], [5,6,5,5,3], size = [i*2 for i in [8,12,14,15,20]], color="red", alpha=0.5)
output_file("Scatter_plotting.html")
show(p)
```
For a complete list of visual attributes, see the [Styling Visual Attributes](https://docs.bokeh.org/en/latest/docs/user_guide/styling.html) documentation page of Bokeh.

