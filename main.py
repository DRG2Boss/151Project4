import arcade
file1 = open("nationsPop.txt", "r")
# First, lets do the readlines command and split the lines within nationsPop.txt
nation_info = file1.readlines()
for lines in nation_info:
    lines = lines.split(',')
# Then, we'll open our Arcade window.
my_window = arcade.open_window(1600, 900, "Populations Of The Largest Nations On Earth")
arcade.set_background_color(arcade.color.CADMIUM_YELLOW)
# Let's get rendering! We'll start with the graph lines and title.
arcade.start_render()
arcade.draw_line(75, 75, 75, 900, arcade.color.BLACK, 5)
arcade.draw_line(75, 75, 1600, 75, arcade.color.BLACK, 5)
arcade.draw_text("Populations of The Largest Nations On Earth", 675, 875, arcade.color.BLACK, 15)
# Now we need to label our Y-Axis.
scale = (900 - 75) / len(range(100, 1500, 100))
# This builds the scale for our labels. It's subtracting the top of the y-axis line to the bottom of the y-axis line.
# Then it divides by the # of y-axis labels (14).
currentY = 75
for pop in range(100, 1500, 100):
    currentLabel = arcade.Text(f"{pop}M", 5, currentY, arcade.color.BLACK)
    currentY += scale
    # This is how we will dynamically adjust the yloc. Every loop will increase currentY by the calculated scale.
    # "x += y" is the same as x = qw x+y
    currentLabel.draw()

arcade.finish_render()
arcade.run()