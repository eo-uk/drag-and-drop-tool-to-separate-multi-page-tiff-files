from PIL import Image, ImageSequence
import os
import sys

def separate_tiff(path, filename=None):
    """

    separate_tiff(path, filename=None)


    Separates a multipage .TIFF file into individual pages.
    Saves each page as a .png file.

    path (str): Absolute or relative path to the .TIFF file.
    filename (str): Name for each page. Defaults to the source file name.
    
    """
    
    #open TIFF file with Pillow
    img = Image.open(path)

    #Get the name of TIFF file if no alternative name is given
    if filename == None:
        filename = os.path.basename(path)

    #Iterate through the pages of TIFF file and save them one by one
    for i, page in enumerate(ImageSequence.Iterator(img)):
        page.save(f"{filename} - Page {i+1}.png")

def main():
    #Main Loop
    while True:
        
        #Try block to catch Pillow exceptions
        try:

            #Check if file paths are given as system arguments
            #(ie. files are dragged & dropped onto the .py file)
            if len(sys.argv) > 1:
                for path in sys.argv[1:]:
                    separate_tiff(path)

            #If there are no additional sys args, prompt user for file path
            else:
                path = input(
                             "\n"
                             "Please enter path to the multipage .TIFF file "
                             "you wish to separate "
                             "or type 'exit' to exit: "
                             "\n"
                             )

                #Check exit prompt
                if path.lower().strip() == 'exit':
                    sys.exit()
                    
                #Attempt to separate TIFF file
                separate_tiff(path)

            #Display success message if no errors are raised along the way
            print("\n .TIFF file successfully separated! \n")
                
        #Display error if Pillow can't open the file
        except IOError as e:
            print("\n FILE CANNOT BE OPENED: \n", e)

        #AttributeError is raised in case path is an empty string
        except AttributeError as e:
            print("\n INVALID INPUT \n")


if __name__ == "__main__":
    main()
