def main():
    file_name = get_file_name()
    print_file_type(file_name)

def get_file_name():
    file_name = str(input("Type file name here: ")
        .strip().lower())
    return file_name

def print_file_type(file_name):
    if file_name.endswith(".png"):
        print ("image/png")
    elif file_name.endswith((".jpeg", ".jpg")):
        print ("image/jpeg")
    elif file_name.endswith(".gif"):
        print ("image/gif")
    elif file_name.endswith(".pdf"):
        print ("application/pdf")
    elif file_name.endswith(".txt"):
        print ("text/plain")
    elif file_name.endswith(".zip"):
        print ("application/zip")
    else:
        print("application/octet-stream")

main()

"""
.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
"""
