## Image Encryption and Decryption Tool

### Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [How It Works](#how-it-works)
   - [Encryption](#encryption)
   - [Decryption](#decryption)
7. [Code Explanation](#code-explanation)
   - [Importing Libraries](#importing-libraries)
   - [Encryption Function](#encryption-function)
   - [Decryption Function](#decryption-function)
   - [GUI Setup](#gui-setup)
8. [Notes](#notes)
9. [License](#license)


### Overview
This program is a simple GUI-based tool for encrypting and decrypting image files using pixel manipulation through XORing the bytearray. The encryption and decryption process is done by applying the XOR operation on each byte of the image with a user-provided key.

### Features
- **Encryption**: Secure your image files using a key.
- **Decryption**: Restore your encrypted image files using the same key.

### Requirements
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

### Installation
1. Make sure you have Python 3.x installed on your machine.
2. Clone or download this repository.
3. Navigate to the directory containing the `ImgEncryption.py` file.

### Usage
1. Run the script:
    ```sh
    python ImgEncryption.py
    ```
2. A GUI window will appear with options to either encrypt or decrypt an image.
3. Enter a numeric key in the provided input field.
4. Select the image file you want to encrypt or decrypt.
5. Click on the "Encrypt" or "Decrypt" button to perform the desired action.

### How It Works
#### Encryption
- The program takes the path of the image file and a numeric key as input.
- It reads the image file and converts it into a bytearray.
- Each byte of the bytearray is XORed with the provided key.
- The modified bytearray is then written back to the image file, completing the encryption process.
  
#### Decryption
- The decryption process is identical to the encryption process.
- By applying the XOR operation with the same key on the encrypted bytearray, the original image is restored.

### Code Explanation
#### Importing Libraries
```python
from tkinter import *
from tkinter import filedialog, messagebox, PhotoImage
```
These libraries are used for creating the GUI and handling file dialogs and message boxes.

#### Encryption Function
```python
def Encrypt():
    try:
        path = filedialog.askopenfilename(title="Select Image File to Encrypt")
        key = int(entry_key.get())
        print('The path of file : ', path)
        print('Key for encryption : ', key)
        
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key
        
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Encryption Done...')
        messagebox.showinfo("Encryption", "Encryption Done!")
    except Exception:
        print('Error caught : ', Exception.__name__)
        messagebox.showinfo("Encryption", "Exception caught during execution")
```

#### Decryption Function
```python
def Decrypt():
    try:
        path = filedialog.askopenfilename(title="Select Image File to Decrypt")
        key = int(entry_key.get())
        print('The path of file : ', path)
        print('Key for encryption : ', key)
        
        fin = open(path, 'rb')
        image = fin.read()
        fin.close()
        
        image = bytearray(image)
        for index, values in enumerate(image):
            image[index] = values ^ key
        
        fin = open(path, 'wb')
        fin.write(image)
        fin.close()
        print('Decryption Done...')
        messagebox.showinfo("Decryption", "Decryption Done!")
    except Exception:
        print('Error caught : ', Exception.__name__)
        messagebox.showinfo("Decryption", "Exception caught during execution")
```

#### GUI Setup
```python
window = Tk()
window.geometry("500x200")
window.title("Image Encryption Decryption Tool")
window.minsize(width=500, height=300)

f1= Frame(window, bg="blue", borderwidth=5, relief=SUNKEN)
f2= Frame(window, bg="blue", borderwidth=2, relief=SUNKEN)
f3= Frame(window, bg="blue", borderwidth=2, relief=SUNKEN)

f1.pack(pady = 15)
f2.pack(pady = 1)
f3.pack(pady = 1)

intial_label = Label(f1,text = " How would you like to proceed with the Image ", font = ("Roboto Mono", 14, "bold"))
entery_label2 = Label(text = "Enter the key below before proceeding further")

intial_label.pack()
entery_label2.pack()

entry_key = Entry(window, width = 20)
entry_key.pack()

encrypt_Button = Button(f2,text = "Encrypt", command = Encrypt)
decrypt_Button = Button(f3,text = "Decrypt", command = Decrypt)

encrypt_Button.pack()
decrypt_Button.pack()

while True:
    window.mainloop()
```
This code sets up the GUI, including the layout and the buttons for encryption and decryption.

### Notes
- Ensure the key used for encryption is the same as the one used for decryption.
- The program modifies the original image file. Make sure to keep a backup if needed.
- **Important**: Enter the key before selecting the image file for encryption or decryption. Failure to do so will result in an exception error.

### License
This project is licensed under the MIT License.



---

