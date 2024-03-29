# Isaiah Marshall | Everything completed | "It just works.." ..as long as your Arcade library is installed.

# First, we need to import the installed library "Arcade."
import arcade

# Now lets open and read the file.
file1 = open("nationsPop.txt", "r")

# This will create a list where each line is an element within said list.
allLines = file1.readlines()

# Then, we'll open our Arcade window and set a background color.
myWindow = arcade.open_window(1600, 900, "Populations Of The Largest Nations On Earth")
arcade.set_background_color(arcade.color.CADMIUM_YELLOW)

# Let's get rendering! We'll start with the graph lines and title.
arcade.start_render()
arcade.draw_line(75, 75, 75, 900, arcade.color.BLACK, 3)
arcade.draw_line(75, 75, 1600, 75, arcade.color.BLACK, 3)
arcade.draw_text("Populations of The Largest Nations On Earth", 675, 875, arcade.color.BLACK, 15)

# Now we need to define some global variables for the x-axis.
# This first one builds the scale for our spacing. It's subtracting the highest value of the x-axis line with the lowest
# Then it divides by the # of x-axis labels (14).
xScale = (1600 - 75) / len(range(100, 1500, 100))

# This variable works in conjunction with xScale to properly space our labels and bars.
beginningX = 75

# Next we need to run through a pretty complicated 'for' loop in order to create a few objects.
for line in allLines:

    # The first two lines create our x-axis labels.
    splitNationData = line.split(',')
    currentLabel = arcade.Text(splitNationData[0], beginningX, 50, arcade.color.BLACK)

    # Similar to xScale, this will be used to help properly scale our bar height within the graph.
    barScale = ((int(splitNationData[1])-100000000)/1700000)

    # Now we want to create the bars that exist within the graph.
    # An ifElse is used to properly define the colors of the graph based on whether our rate of change is pos or neg.
    if float(splitNationData[2]) < 0:
        arcade.draw_xywh_rectangle_filled(beginningX, 75, 100, barScale, arcade.color.RED)
    else:
        arcade.draw_xywh_rectangle_filled(beginningX, 75, 100, barScale, arcade.color.GREEN)
    # Using both of the earlier variables, I'm able to get the spacing correct between all of my X labels and graphs.
    # Note: "x += y" is the same as "x = x+y"
    beginningX += xScale
    currentLabel.draw()

# Now we need to label our Y-Axis using a much similar flow. We'll start with declaring similar global variables.
yScale = (900 - 75) / len(range(100, 1500, 100))
beginningY = 75

for number in range(100, 1500, 100):

    # The following lines will draw our y-axis labels and lines, and then properly space them using similar logic.
    currentLabel = arcade.Text(f"{number}M", 5, beginningY, arcade.color.BLACK)
    arcade.draw_line(75, beginningY, 1600, beginningY, arcade.color.BLACK)
    beginningY += yScale
    currentLabel.draw()

arcade.finish_render()
arcade.run()
