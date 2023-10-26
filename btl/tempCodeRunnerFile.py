from PIL import Image
import base64
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Toplevel
from PIL import ImageTk


ENDOFMESSAGE = "0100100101010101010101100100111101010010010001010011100101000111010101000101010101010110010101000101010100110000010001100100100001010010010100110100010100111101"

def encode_message_as_bytestring(message):
    b64 = message.encode("utf8")
    bytes_ = base64.encodebytes(b64)
    bytestring = "".join(["{:08b}".format(x) for x in bytes_])
    bytestring += ENDOFMESSAGE
    return bytestring

def get_pixels_from_image(fname):
    img = Image.open(fname)
    img_width, img_height = img.size
    pixels = list(img.getdata())
    return pixels, img_width, img_height

def encode_pixels_with_message(pixels, bytestring):
    enc_pixels = []
    string_i = 0

    for pixel in pixels:
        enc_pixel = []
        for component in pixel:
            if string_i >= len(bytestring):
                enc_component = component
            else:
                bit = int(bytestring[string_i])
                enc_component = (component & 254) | bit
                string_i += 1
            enc_pixel.append(enc_component)
        enc_pixels.append(tuple(enc_pixel))
    return enc_pixels

def write_pixels_to_image(pixels, fname, img_width, img_height):
    img = Image.new('RGB', (img_width, img_height))
    img.putdata(pixels)
    img.save(fname)

def decode_pixels(pixels):
    bytestring = []
    for pixel in pixels:
        for component in pixel:
            bit = component & 1
            bytestring.append(str(bit))
    bytestring = ''.join(bytestring)
    message = decode_message_from_bytestring(bytestring)
    return message

def decode_message_from_bytestring(bytestring):
    bytestring = bytestring.split(ENDOFMESSAGE)[0]
    message = int(bytestring, 2).to_bytes(len(bytestring) // 8, byteorder='big')
    message = base64.decodebytes(message).decode("utf8")
    return message

def choose_image():
    file_path = filedialog.askopenfilename(title="Select an Image")
    if file_path:
        image_label.config(text="Selected Image: " + file_path)
        encode_button["state"] = "active"
        decode_button["state"] = "active"
        global selected_image
        selected_image = file_path

def encode_image():
    if selected_image:
        in_image = selected_image
        in_message = message_entry.get()
        pixels, img_width, img_height = get_pixels_from_image(in_image)
        bytestring = encode_message_as_bytestring(in_message)
        epixels = encode_pixels_with_message(pixels, bytestring)
        out_image = in_image[:-4] + "-enc.png"
        write_pixels_to_image(epixels, out_image, img_width, img_height)
        result_label.config(text=f"Encoded image saved as {out_image}")

       
        new_window = Toplevel(root)
        new_window.title("Original and Encoded Images")

        original_image = Image.open(in_image)
        encoded_image = Image.open(out_image)

        original_image = original_image.resize((500, 500))  
        encoded_image = encoded_image.resize((500, 500))  

        original_image = ImageTk.PhotoImage(original_image)
        encoded_image = ImageTk.PhotoImage(encoded_image)

        before_label = Label(new_window, text="Before", font=("Arial", 30))
        after_label = Label(new_window, text="After", font=("Arial", 30))
        original_label = Label(new_window, image=original_image)
        encoded_label = Label(new_window, image=encoded_image)

        before_label.grid(row=0, column=0, padx=10, pady=5)  
        after_label.grid(row=0, column=1, padx=10, pady=5)  
        original_label.grid(row=1, column=0, padx=10, pady=5)  
        encoded_label.grid(row=1, column=1, padx=10, pady=5)  

        new_window.grid_rowconfigure(1, weight=1)
        new_window.grid_columnconfigure(0, weight=1)
        new_window.grid_columnconfigure(1, weight=1)

        original_label.image = original_image
        encoded_label.image = encoded_image

def decode_image():
    password = password_entry.get()
    if password == 'admin123':        
        if selected_image:
            in_image = selected_image
            pixels, _, _ = get_pixels_from_image(in_image)
            result = decode_pixels(pixels)
            result_label.config(text=f"Decoded message: {result}")
    else:
        result_label.config(text = "Wrong password!")

# Tạo cửa sổ giao diện chính
root = tk.Tk()
root.title("Steganography App")
root.geometry("800x600")

# Tạo biến lưu trữ đường dẫn của hình ảnh được chọn
selected_image = None

# Label để hiển thị đường dẫn của hình ảnh được chọn
image_label = Label(root, text="Select an Image", font=("Arial", 18))
image_label.pack(pady=20)

# Nút để chọn hình ảnh
select_button =tk.Button (root, text="Choose Image", command=choose_image, width=30, font=("Arial", 16))
select_button.pack()

# Nút để mã hóa hình ảnh
encode_button = tk.Button(root, text="1. Encode", command=encode_image, state="disabled", width=30, font=("Arial", 16))
encode_button.pack()

# Nút để giải mã hình ảnh
decode_button = tk.Button(root, text="2. Decode", command=decode_image, state="disabled", width=30, font=("Arial", 16))
decode_button.pack()

