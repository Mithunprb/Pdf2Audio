#!usr/bin/python
import tkinter as Tk
from tkinter import ttk
import PyPDF2
import os
import pyttsx3
from tkinter import filedialog
from gtts import gTTS, tts

class Pdf_audio(object):
    def __init__(self, parent, *args, **kwargs):
        #Tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.root.title("PDF to Audio")
        self.frame = Tk.Frame(parent)
        self.frame.pack() 


    def switch(self):
        
      my_notebook.select(1)

    def switch1(self):

      my_notebook.select(2)

    def switch2(self):

        my_notebook.select(0)

    

  
    def sel(self):
        print("You selected " + str(var.get()))

    def open_file(self):
         filename = filedialog.askopenfilename(initialdir="/home/mithun/Mithun/Books",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.pdf*"),
                                                         ("all files",
                                                          "*.*")))
         self.filename = filename 
    def audio_maker(self):
        self.open_file()
        print(self.filename)
        pdfFileObj = open(self.filename, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        mytext = ""

        for pageNum in range(pdfReader.numPages):

            pageObj = pdfReader.getPage(pageNum)

            mytext += pageObj.extractText()

            myobj1 = gTTS(text=mytext, lang=str(var.get()))
            myobj1.save(qpath)
            os.system(qpath)

        pdfFileObj.close()



                                          # Clear the textbox

    def clear_text_box(self):
        my_text .delete(1.0, Tk.END)

                                        # Open our pdf file
    def open_pdf(self):
                                 # Grab the filename of the pdf file
        self.open_file()
                                        # Check to see if there is a file
        if self.filename:
                                          # Open the pdf file
            pdf_file = PyPDF2.PdfFileReader(self.filename)
                                              # Set the page to read
            page = pdf_file.getPage(0)
                                              # Extract the text from the pdf file
            page_stuff = page.extractText()

                                               #  Add text to textbox
            my_text.insert(1.0, page_stuff)

                                        #Create A Menu
    

    def nump(self):

      self.open_file()
      pdfReader = PyPDF2.PdfFileReader(self.filename)
                                             #no th of page
      from_page = pdfReader.getPage(int_num)
      LN = pdfReader.getNumPages()

                                            #extracting the text from PDF
      text = from_page.extractText()
                                            #reading the txt
      speak = pyttsx3.init()
      speak.say(text)
      speak.runAndWait

    

    def play(self):
          myobj = gTTS(text=entry.get(), lang=v, slow=False)
          
          myobj.save("convert.wav")
          os.system("convert.wav")


if __name__ == "__main__":
    root = Tk.Tk()
    
    app = Pdf_audio(root)
    icon = Tk.PhotoImage(file='/home/mithun/Mithun/Programming/Python/Tkinter/Audio/pdf2audio/icon.png')
    root.iconphoto(False, icon)


    my_notebook = ttk.Notebook(root)
    my_notebook.pack(pady=15)

    my_frame1 = Tk.Frame(my_notebook, width=500, height=500, bg="#4a8577")
    my_frame2 = Tk.Frame(my_notebook, width=500, height=500)
    my_frame3 = Tk.Frame(my_notebook, width=500, height=500, bg="lightgrey")

    my_notebook.add(my_frame1, text="1st Tab")
    my_notebook.add(my_frame2, text="2nd Tab")
    my_notebook.add(my_frame3, text="3rd Tab")

    canvas = Tk.Canvas(my_frame1, bg="#4a8577", bd=0, highlightthickness=0)
    photo = Tk.PhotoImage(file="/home/mithun/Mithun/Programming/Python/Tkinter/Audio/pdf2audio/download.png")
                                                           #
    lbl = Tk.Label(my_frame1, image=photo, bg="#4a8577")
    lbl.place(relx=0.5, rely=0.36, anchor='center')

    canvas.create_text(200, 100, text=" PDF TO AUDIO ",anchor='center', fill="#0f1020", font=("Times New Roman", 25, "bold"))
    canvas.pack()

    btn2 = Tk.Button(my_frame1,text="Pdf to audio", width="15", command=app.audio_maker)
    btn2.place(x=200, y=270)

                # From here Tab2 code
                # Create a textbox
    my_text = Tk.Text(my_frame2, height=30, width=60)
    my_text.pack(pady=10)
    my_text.insert(1.0,"Extract your PDF here!!")
    my_menu = Tk.Menu(my_frame2)

    root.config(menu=my_menu)

    langs = {'English':'en', 'Hindi':'hi-IN', 'French':'fr-FR','Italian':'it-IT','Japanese':'ja-JP','Kannada':'kn-IN','Malyalam':'ml-IN','Spanish':'es-US'}
    var = Tk.StringVar(value="1")
    var1 = Tk.StringVar(value="1")

    for  k,v in langs.items():

        print(v)
        button_R = Tk.Radiobutton(my_frame1,text=k,value=v, variable=var, highlightthickness=0, bd=0, bg='#4a8577',command=app.sel)
        button_R.pack(anchor=Tk.W)
        
    for  k1,v1 in langs.items():   
        button_R1 = Tk.Radiobutton(my_frame3,text=k1,value=v1, variable=var1,highlightthickness=0, bd=0, bg='lightgrey',command=app.sel)
        button_R1.pack(anchor=Tk.W)


    q = Tk.Label(my_frame1, text="Destination folder : ", bg="#4a8577").place(x=150, y=350)

    e2 = Tk.StringVar()
    e2 = Tk.Entry(my_frame1)

    e2.insert(0,"pdf.mp3")
    e2.place(x=280, y=350)

    qpath = str(e2.get())

                                             # Add some dropdown menus
    file_menu = Tk.Menu(my_menu, tearoff=False)

    my_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=app.open_pdf)
    file_menu.add_command(label="Clear", command=app.clear_text_box)
    file_menu.add_separator()

    file_menu.add_command(label="Exit", command=root.destroy)

    Eentry = Tk.Entry(my_frame1)
    Eentry.place(x=80, y=470)
    Eentry.insert(0, "")
    Eentry = Tk.IntVar()
    num = Eentry.get()
    int_num = int(num)
    Elabel = Tk.Label(my_frame1, text="Page no:",bg="#4a8577")
    Elabel.place(x=10,y=470)
    subtton = Tk.Button(my_frame1,text="GO", command=app.nump).place(x=250,y=465)

                                                                           #2nd Tab  end here
                                                                           #tab 3

    label = Tk.Label(my_frame3, text="Text to Speech",bg="lightgrey",font="bold, 20").place(x=150, y=30)

    entry = Tk.Entry(my_frame3, width=33, bd=2, font=14)
    entry.place(x=100, y=90)
    entry.insert(0, "")

    btn = Tk.Button(my_frame3, text="SUBMIT",

             width="15", pady=10,font="bold, 15", command=app.play, bg='yellow')
    btn.place(x=160, y=180)



    style = ttk.Style()
    style.configure("my_notebook.Tab", foreground="black", background="white")

    my_button3 = Tk.Button(my_frame1, text=">>", command=app.switch)
    my_button3.place(x=400, y=450)
    my_button4 = Tk.Button(my_frame2, text=">>", command=app.switch1)
    my_button4.place(x=400, y=450)

    my_button_4 = Tk.Button(my_frame2, text="<<", command=app.switch2)
    my_button_4.place(x=100, y=450)
    my_button_5 = Tk.Button(my_frame3, text="<<", command=app.switch)
    my_button_5.place(x=100, y=450)

    my_button5 = Tk.Button(my_frame3, text=">>", state=Tk.DISABLED)
    my_button5.place(x=400, y=450)


    root.mainloop()
