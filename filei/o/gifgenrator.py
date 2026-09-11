# ============================================================
# PROGRAM: Create an animated GIF from multiple images
# ============================================================
#
# We will give image filenames through the terminal:
#
#     python costumes.py costume1.gif costume2.gif
#
# The program will:
#
# 1. Get the image filenames from the terminal
# 2. Open each image using Pillow
# 3. Store the opened images in a Python list
# 4. Combine the images
# 5. Save them as an animated GIF
#
# ============================================================


# ------------------------------------------------------------
# 1. IMPORT sys
# ------------------------------------------------------------

import sys

# sys is a built-in Python MODULE.
#
# A module is like a toolbox containing useful Python code.
#
# We are using sys because it gives us access to:
#
#     sys.argv
#
# sys.argv contains the values that we give to our Python
# program through the terminal.
#
#
# Example terminal command:
#
#     python costumes.py costume1.gif costume2.gif
#
# Python stores these values approximately like this:
#
#     sys.argv = [
#         "costumes.py",
#         "costume1.gif",
#         "costume2.gif"
#     ]
#
#
# Index:
#
#     sys.argv[0] -> "costumes.py"
#     sys.argv[1] -> "costume1.gif"
#     sys.argv[2] -> "costume2.gif"


# ------------------------------------------------------------
# 2. IMPORT Image FROM PIL
# ------------------------------------------------------------

from PIL import Image

# PIL (commonly used today through Pillow) is a package for
# working with images.
#
# Image is a MODULE inside PIL.
#
# Think:
#
#     PIL (package)
#       |
#       └── Image (module)
#
#
# The Image module provides functions/classes for working
# with images.
#
# One thing we will use is:
#
#     Image.open()
#
# open() is used to open an image file.
#
#
# IMPORTANT:
#
#     Image.open("costume1.gif")
#
# returns an IMAGE OBJECT.
#
# That object represents the opened image inside Python.
#
#
# Think:
#
#     image file
#          |
#          ↓
#     Image.open()
#          |
#          ↓
#     Image OBJECT
#
#
# The Image object has methods such as:
#
#     .save()
#     .resize()
#     .rotate()
#
# etc.


# ------------------------------------------------------------
# 3. CREATE AN EMPTY LIST
# ------------------------------------------------------------

images = []

# We create an empty list because we need somewhere to store
# all the Image OBJECTS that we open.
#
# Initially:
#
#     images = []
#
#
# After opening the first image:
#
#     images = [image1]
#
#
# After opening the second image:
#
#     images = [image1, image2]
#
#
# IMPORTANT:
#
# images is a LIST.
#
# Therefore:
#
#     images.append(...)
#
# is a LIST METHOD.
#
# But:
#
#     image.save(...)
#
# is NOT a list method.
#
# .save() belongs to the IMAGE OBJECT.


# ------------------------------------------------------------
# 4. GET IMAGE FILENAMES FROM THE TERMINAL
# ------------------------------------------------------------

for arg in sys.argv[1:]:

    # sys.argv[1:] means:
    #
    # "Give me everything from index 1 onwards."
    #
    #
    # If:
    #
    # sys.argv = [
    #     "costumes.py",
    #     "costume1.gif",
    #     "costume2.gif"
    # ]
    #
    # then:
    #
    # sys.argv[1:]
    #
    # becomes:
    #
    # [
    #     "costume1.gif",
    #     "costume2.gif"
    # ]
    #
    #
    # Why don't we use sys.argv directly?
    #
    # Because sys.argv[0] is the Python file name:
    #
    #     "costumes.py"
    #
    # We don't want to try to open costumes.py as an image.
    #
    #
    # The for loop takes one filename at a time.
    #
    # First iteration:
    #
    #     arg = "costume1.gif"
    #
    # Second iteration:
    #
    #     arg = "costume2.gif"


    # --------------------------------------------------------
    # 5. OPEN THE IMAGE
    # --------------------------------------------------------

    image = Image.open(arg)

    # Suppose this is the first iteration:
    #
    #     arg = "costume1.gif"
    #
    # Then Python executes:
    #
    #     image = Image.open("costume1.gif")
    #
    #
    # Image.open() opens the image and returns an
    # IMAGE OBJECT.
    #
    # That object is stored inside the variable "image".
    #
    #
    # So:
    #
    #     image
    #       ↓
    #     Image OBJECT
    #
    #
    # IMPORTANT:
    #
    # "image" is NOT the filename.
    #
    # "image" is the object representing the opened image.
    #
    #
    # Because it is an Image object, it has image-related
    # methods such as:
    #
    #     image.save()
    #     image.resize()
    #     image.rotate()


    # --------------------------------------------------------
    # 6. ADD THE IMAGE OBJECT TO OUR LIST
    # --------------------------------------------------------

    images.append(image)

    # images is a LIST.
    #
    # .append() is therefore a LIST METHOD.
    #
    # It adds the Image object to the end of the list.
    #
    #
    # First iteration:
    #
    #     images = []
    #
    #     images.append(image)
    #
    #     images = [image1]
    #
    #
    # Second iteration:
    #
    #     images.append(image)
    #
    #     images = [image1, image2]
    #
    #
    # So after the loop finishes:
    #
    #     images[0] -> first Image object
    #     images[1] -> second Image object


# ============================================================
# 7. CREATE THE ANIMATED GIF
# ============================================================

images[0].save(
    "costumes.gif",

    save_all=True,

    append_images=[images[1]],

    duration=200,

    loop=0
)


# ------------------------------------------------------------
# Let's understand the line above
# ------------------------------------------------------------

# images[0]
#
# means:
#
#     "Give me the FIRST item from the images list."
#
#
# Remember:
#
#     images[0] -> first Image object
#     images[1] -> second Image object
#
#
# Therefore:
#
#     images[0].save()
#
# means:
#
#     "Call the save() METHOD on the first Image object."
#
#
# .save() is NOT a list method.
#
# It is a METHOD of the Image object.
#
#
# Think:
#
#     images
#       |
#       ├── [0] → Image object → .save()
#       |
#       └── [1] → Image object
#
#
# The thing BEFORE the dot tells you which object's method
# you are calling.
#
#     images.append()
#          ↑
#       list object
#
#     image.save()
#          ↑
#      Image object


# ------------------------------------------------------------
# "costumes.gif"
# ------------------------------------------------------------

# This is the name of the output file.
#
# Our final animated GIF will be saved as:
#
#     costumes.gif


# ------------------------------------------------------------
# save_all=True
# ------------------------------------------------------------

# We don't want to save only the first image.
#
# We want to save multiple images/frames.
#
# Therefore:
#
#     save_all=True
#
# tells Pillow to save all the frames.


# ------------------------------------------------------------
# append_images=[images[1]]
# ------------------------------------------------------------

# images[0] is our first image.
#
# We want images[1] to be the next frame.
#
# So:
#
#     append_images=[images[1]]
#
# means:
#
#     "Add the second Image object as another frame."
#
#
# Notice the square brackets:
#
#     [images[1]]
#
# This creates a LIST containing the second Image object.
#
#
# So conceptually:
#
#     Frame 1 → images[0]
#     Frame 2 → images[1]


# ------------------------------------------------------------
# duration=200
# ------------------------------------------------------------

# duration controls how long each frame is displayed.
#
# 200 milliseconds = 0.2 seconds.
#
# So roughly:
#
#     Image 1 → 0.2 sec
#     Image 2 → 0.2 sec


# ------------------------------------------------------------
# loop=0
# ------------------------------------------------------------

# loop=0 means the GIF keeps repeating.
#
# So:
#
#     Image 1
#        ↓
#     Image 2
#        ↓
#     Image 1
#        ↓
#     Image 2
#        ↓
#       ...
#
# The animation continues looping.


# ============================================================
# FINAL RESULT
# ============================================================
#
# Terminal:
#
#     python costumes.py costume1.gif costume2.gif
#
#                  ↓
#
#               sys.argv
#
#     ["costumes.py", "costume1.gif", "costume2.gif"]
#
#                  ↓
#
#              sys.argv[1:]
#
#     ["costume1.gif", "costume2.gif"]
#
#                  ↓
#
#              for loop
#
#                  ↓
#
#          Image.open(filename)
#
#                  ↓
#
#             Image OBJECT
#
#                  ↓
#
#          images.append(image)
#
#                  ↓
#
#     [Image object, Image object]
#
#                  ↓
#
#          images[0].save()
#
#                  ↓
#
#             costumes.gif
#
#                  ↓
#
#          Animated GIF 
#
# ============================================================