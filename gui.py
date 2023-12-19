import tkinter as tk
from compressmodule import compress,decompress
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(initialdir='/',title="select a file to compress")
    return filename


def Compression(i,o):
    compress(i,o)
def Decompress(i,o):
    decompress(i,o)


window = tk.Tk()
window.title("Compression engine")
window.geometry("600x400")
input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
input_label = tk.Label(window,text="File to be compressed")
output_label = tk.Label(window,text="Name of compressed file")

compress_button = tk.Button(window,text="Compress",command= lambda: Compression(open_file(),"compressedoutput1.txt"))
decompress_button = tk.Button(window,text="Decompress",command= lambda: decompress("compressedoutput1.txt","decompressed1.txt"))


compress_button.grid(row=2,column=1)
decompress_button.grid(row=3,column=1)
window.mainloop() 