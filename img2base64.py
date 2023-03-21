# This method will produce a Base64 img element for import into an html file.
# 
# Usage: 
# point to your image file => image_file_name
# set id for your <img> element => img_element_id
# By default it will save the file in the same directory as this script.

import base64
import sys, getopt


def main(argv):
    image_file_name = ''
    img_element_id = ''    
    
    # Handle command line input
    arglen = len(argv)
    usage_message = '\n>\tUsage: \
                    \n\t\tpython3 image2base64.py -i <inputfile> -o <outputfile> \
                    \n\t\tThe <img> element will hold id=<outputfile>\n'
    error_usage_message = "\n>\tIncorrect usage! Use -h for more info.\n"
    
    if not arglen == 1 and not arglen == 4 :
        sys.exit(error_usage_message)
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except:
        sys.exit(error_usage_message)
    for opt, arg in opts:
        if opt == '-h':
            sys.exit(usage_message)
        elif opt == '-i':
            image_file_name = arg
        elif opt == '-o':
            img_element_id = arg
        else:
            sys.exit(error_usage_message)   


    # Convert the image to base64
    try:
        with open(image_file_name, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())
    except FileNotFoundError:
        print(f'\n>\tCould not find \033[4m{image_file_name}\033[0m\n')
        return 0

    # Save to a txt file as <img> element to use in html
    f = open(f'{img_element_id}.txt', 'a')
    f.write(f'<img id="{img_element_id}" src="data:image/png;base64,{encoded_string.decode("utf-8")}">')
    f.close()

    
    print(f'\n>\tThe <img> element is saved in \033[4m{img_element_id}.txt\033[0m file.')
    print('>\tOpen it and copy the whole content, then paste in your html directly.\n')

if __name__ == "__main__":
    main(sys.argv[1:])