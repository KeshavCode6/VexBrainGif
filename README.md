# Vex Gif
This program can convert any gif and draw it on the Vex V5 screen. By default has a spinning banana gif at 24 FPS.  Created by Keshav from Team 17451

## Restrictions
- Memory: Vex V5 Brain can only allocate so much memory, so size of gifs is limited
- Size: Gif has to be square shaped and less than 272 pixels wide and long

## How to add custom gifs
You have to have python 3 and pillow installed for this to work.

In the DataGenerator folder, add any gif following restrictions with the name 'bad.gif'. Then, execute the 'run.py' script. Various files will be created in the directory. Then, go to FINAL.txt, and copy the python array. All files except for the 2 python files can be deleted after this. 

Then, open the GIF vex project and replace the huge data array with your own. If you have syntax errors, move your cursor to the start of the line where the final closing bracket of the data array is and hit back space.

Now, using the VEXCODE 5 extension, you can build and upload the script and run it on your V5 Brain

## Editing Code
You can customize the FPS and Frames extracted from the gif by editing various variables found in the python files.

Feel free to do any editing 

