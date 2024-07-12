from tkinter import *
from tkinter import filedialog, messagebox, PhotoImage

#Function for Encryption
def Encrypt():
    try:
        # take path of image as a input
        path =  filedialog.askopenfilename(title="Select Image File to Encrypt")
        
        # taking encryption key as input
        key = int(entry_key.get())
        
        
        # print path of image file and encryption key that we are using
        print('The path of file : ', path)
        print('Key for encryption : ', key)
        
        # open file for reading purpose
        fin = open(path, 'rb')
        
        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        
        # converting image into byte array to perform encryption easily on numeric data
        image = bytearray(image)
        
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key
        
        # opening file for writing purpose
        fin = open(path, 'wb')
        
        # writing encrypted data in image
        fin.write(image)
        fin.close()
        print('Encryption Done...')
        messagebox.showinfo("Encryption", "Encryption Done!")
    
    except Exception:
        print('Error caught : ', Exception.__name__)
        messagebox.showinfo("Eecryption", "Exception caught during excecution")





# try block to handle exception
def Decrypt():
    try:
        # take path of image as a input
        path = filedialog.askopenfilename(title="Select Image File to Decrypt")
        
        # taking encryption key as input
        key = int(entry_key.get())
        

        # print path of image file and encryption key that we are using
        print('The path of file : ', path)
        print('Key for encryption : ', key)
        
        # open file for reading purpose
        fin = open(path, 'rb')
        
        # storing image data in variable "image"
        image = fin.read()
        fin.close()
        
        # converting image into byte array to perform encryption easily on numeric data
        image = bytearray(image)
        
        # performing XOR operation on each value of bytearray
        for index, values in enumerate(image):
            image[index] = values ^ key
        
        # opening file for writing purpose
        fin = open(path, 'wb')
        
        # writing encrypted data in image
        fin.write(image)
        fin.close()
        print('Decryption Done...')
        messagebox.showinfo("Decryption", "Decryption Done!")
    
    except Exception:
        print('Error caught : ', Exception.__name__)
        messagebox.showinfo("Decryption", "Exception caught during excecution")

#window to create a dailogue box
window = Tk()
window.geometry("500x200")

#frames
f1= Frame(window, bg="blue", borderwidth=5, relief=SUNKEN)
f2= Frame(window, bg="blue", borderwidth=2, relief=SUNKEN)
f3= Frame(window, bg="blue", borderwidth=2, relief=SUNKEN)

#packing frames
f1.pack(pady = 15)
f2.pack(pady = 1)
f3.pack(pady = 1)


#title of the dailogue box
window.title("Image Encryption Decryption Tool")
window.minsize(width=500, height=300)

#adding a labels to the GUI
intial_label = Label(f1,text = " How would you like to proceed with the Image ", font = ("Roboto Mono", 14, "bold"))
entery_label2 = Label(text = "Enter the key below before proceeding further")

#packing labels
intial_label.pack()
entery_label2.pack()

#entery field box to input key
entry_key = Entry(window, width = 20)
entry_key.pack()

#button to call Encryption & Decryption function upon being clicked
encrypt_Button = Button(f2,text = "Encrypt", command = Encrypt)
decrypt_Button = Button(f3,text = "Dencrypt", command = Decrypt)

#packing the Encryption and Decryption buttons
encrypt_Button.pack()
decrypt_Button.pack()



#keep the GUI up & running whilest it's listening
while True:
    window.mainloop()
    