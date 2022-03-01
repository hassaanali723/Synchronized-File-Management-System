import socket
import threading
from tkinter import *
import tkinter.messagebox
import time



host="192.168.10.8"
port=9999

if __name__ == "__main__":


    def connect():
     try:
        s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s1.connect((host, port))
        print("Client is connected Server")
        # main_gui(s1)
        username(s1)

     except:
        print("Server is not Live")


        exit()


# def msg_send(msg):
#
#     msg1=msg.encode("utf-8")
#     s1.send(msg1)
#     msg2="File Name"
#     msg22=msg2.encode("utf-8")
#     s1.send(msg22)
#     msg3 = "File Mode"
#     msg33 = msg3.encode("utf-8")
#     s1.send(msg33)




def create_file(s1):
    def create_save():
        file_name=create_text.get(1.0,'end-1c')
        tkinter.messagebox.showinfo("Message","File created")
        func_name="create"
        s1.send(func_name.encode("utf-8"))
        s1.send(file_name.encode("utf-8"))

        # msg_send(file_name)
        # object.create_file(file_name)
        root1.destroy()

    root1 = Tk()
    root1.geometry("300x250")
    create_frame=Frame(root1,bg='#3b93ff')
    create_frame.pack()
    root1.configure(bg='#3b93ff')

    create_label = Label(create_frame,text="Enter the name of file", width=10, height=2,padx=30)
    create_label.pack(pady=10)

    create_text=Text(create_frame,width=20,height=1,padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=create_save)
    create_button.pack(pady=10)



    root1.mainloop()



def delete_file(s1):
    def delete_save():
        file_name=create_text.get(1.0,'end-1c')
        tkinter.messagebox.showinfo("Message","File deleted")
        func_name = "delete"
        s1.send(func_name.encode("utf-8"))
        s1.send(file_name.encode("utf-8"))
        # object.delete_file(file_name)
        root1.destroy()

    root1 = Tk()
    root1.geometry("300x250")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    create_label = Label(create_frame,text="Enter the name of file", width=10, height=2,padx=30)
    create_label.pack(pady=10)

    create_text=Text(create_frame,width=20,height=1,padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=delete_save)
    create_button.pack(pady=10)



    root1.mainloop()



def open_file(s1):
    def open_save():
        file_name=open_text.get(1.0,'end-1c')
        file_mode = create_text.get(1.0, 'end-1c')

        func_name = "open"
        s1.send(func_name.encode("utf-8"))
        s1.send(file_name.encode("utf-8"))
        time.sleep(0.1)
        s1.send(file_mode.encode("utf-8"))
        time.sleep(0.1)
        t = s1.recv(64).decode("utf-8")
        # t=object.Read_From_File()

        tkinter.messagebox.showinfo("Message",t)
        root1.destroy()

    root1 = Tk()
    root1.geometry("300x250")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    open_label = Label(create_frame,text="Enter the name of file", width=15, height=2,padx=30)
    open_label.pack(pady=10)

    open_text=Text(create_frame,width=20,height=1,padx=0)
    open_text.pack(pady=10)

    create_label = Label(create_frame, text="Enter the file mode (r,w,a)", width=15, height=2, padx=30)
    create_label.pack(pady=10)

    create_text = Text(create_frame, width=20, height=1, padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=open_save)
    create_button.pack(pady=10)



    root1.mainloop()


def close_file(s1):
    def close_save():
        file_name=create_text.get(1.0,'end-1c')
        tkinter.messagebox.showinfo("Message","File closed")
        func_name = "close"
        s1.send(func_name.encode("utf-8"))
        s1.send(file_name.encode("utf-8"))
        # object.close_file(file_name)
        root1.destroy()

    root1 = Tk()
    root1.geometry("300x250")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    create_label = Label(create_frame,text="Enter the name of file", width=10, height=2,padx=30)
    create_label.pack(pady=10)

    create_text=Text(create_frame,width=20,height=1,padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=close_save)
    create_button.pack(pady=10)



    root1.mainloop()

def append_file(s1):
    def append_save():
        file_data=create_text.get(1.0,'end-1c')
        tkinter.messagebox.showinfo("Message","Data appended")
        func_name = "append"
        s1.send(func_name.encode("utf-8"))
        s1.send(file_data.encode("utf-8"))
        # object.append_file(file_data)
        root1.destroy()

    root1 = Tk()
    root1.geometry("300x250")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    create_label = Label(create_frame, text="Enter the Data to append in a file", width=20, height=2, padx=30)
    create_label.pack(pady=10)

    create_text = Text(create_frame, width=20, height=1, padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=append_save)
    create_button.pack(pady=10)

    root1.mainloop()






def write_file(s1):
    def data_save():
        file_data=create_text.get(1.0,'end-1c')
        tkinter.messagebox.showinfo("Message","Data saved")
        func_name = "write"
        s1.send(func_name.encode("utf-8"))
        s1.send(file_data.encode("utf-8"))

        # object.write_to_file(file_data)
        root1.destroy()

    root1 = Tk()
    root1.geometry("300x250")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    create_label = Label(create_frame, text="Enter the Data for the file", width=10, height=2, padx=30)
    create_label.pack(pady=10)

    create_text = Text(create_frame, width=20, height=1, padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=data_save)
    create_button.pack(pady=10)

    root1.mainloop()


def write_specific_file(s1):
    def write_specific_save():
        data=open_text.get(1.0,'end-1c')
        file_data = create_text.get(1.0, 'end-1c')
        ques = overwite_text.get(1.0, 'end-1c')
        # print(data,file_data,ques)

        func_name = "writes"
        s1.send(func_name.encode("utf-8"))
        s1.send(data.encode("utf-8"))
        time.sleep(0.1)
        s1.send(file_data.encode("utf-8"))
        time.sleep(0.1)
        s1.send(ques.encode("utf-8"))

        # object.Write_to_File(data, file_data,ques)
        tkinter.messagebox.showinfo("Message", "Process Complete")
        root1.destroy()

    root1 = Tk()
    root1.geometry("400x350")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    open_label = Label(create_frame,text="Enter the Point where you want to write", width=30, height=2,padx=30)
    open_label.pack(pady=10)

    open_text=Text(create_frame,width=20,height=1,padx=0)
    open_text.pack(pady=10)

    create_label = Label(create_frame, text="Enter the data", width=10, height=2, padx=30)
    create_label.pack(pady=10)

    create_text = Text(create_frame, width=20, height=1, padx=0)
    create_text.pack(pady=10)

    overwite_label = Label(create_frame, text="Do you want to overwrite (y or n)", width=31, height=2, padx=30)
    overwite_label.pack(pady=10)

    overwite_text = Text(create_frame, width=20, height=1, padx=0)
    overwite_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=write_specific_save)
    create_button.pack(pady=10)



    root1.mainloop()



def truncate_file(s1):
    def truncate_save():
        file_size=create_text.get(1.0,'end-1c')

        func_name = "truncate"
        s1.send(func_name.encode("utf-8"))
        s1.send(file_size.encode("utf-8"))
        # object.truncate(file_size)
        tkinter.messagebox.showinfo("Message", "Process Complete")
        root1.destroy()

    root1 = Tk()
    root1.geometry("300x250")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    create_label = Label(create_frame, text="Enter the size of the file you want", width=20, height=2, padx=30)
    create_label.pack(pady=10)

    create_text = Text(create_frame, width=20, height=1, padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=truncate_save)
    create_button.pack(pady=10)

    root1.mainloop()


def read_file(s1):

    root1 = Tk()
    root1.geometry("300x150")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    create_label = Label(create_frame, text="", width=20, height=2, padx=30)
    create_label.pack(pady=10)

    func_name = "read"
    s1.send(func_name.encode("utf-8"))
    time.sleep(0.5)
    t=s1.recv(64).decode("utf-8")
    # t=object.Read_From_File()
    create_label.configure(text=t)
    root1.mainloop()

def read_specific_file(s1):
    def read_specific_save():
        start=open_text.get(1.0,'end-1c')
        time.sleep(0.1)

        end = create_text.get(1.0, 'end-1c')
        # text=object.read_from_file(start, end)
        # show_label.configure(text=text)

        func_name = "reads"
        s1.send(func_name.encode("utf-8"))
        s1.send(start.encode("utf-8"))
        time.sleep(0.1)
        s1.send(end.encode("utf-8"))
        t = s1.recv(64).decode("utf-8")
        show_label.configure(text=t)



    root1 = Tk()
    root1.geometry("300x350")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    open_label = Label(create_frame,text="Enter the Stating point", width=10, height=2,padx=30)
    open_label.pack(pady=10)

    open_text=Text(create_frame,width=20,height=1,padx=0)
    open_text.pack(pady=10)

    create_label = Label(create_frame, text="Enter the Ending point", width=10, height=2, padx=30)
    create_label.pack(pady=10)

    create_text = Text(create_frame, width=20, height=1, padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=read_specific_save)
    create_button.pack(pady=10)

    show_label = Label(create_frame, text="", width=10, height=2, padx=30)
    show_label.pack(pady=10)

    root1.mainloop()

def move_file(s1):
    def move_save():
        start=open_text.get(1.0,'end-1c')
        length = create_text.get(1.0, 'end-1c')
        point = overwite_text.get(1.0, 'end-1c')
        func_name = "move"
        s1.send(func_name.encode("utf-8"))
        s1.send(start.encode("utf-8"))
        time.sleep(0.1)
        s1.send(length.encode("utf-8"))
        time.sleep(0.1)
        s1.send(point.encode("utf-8"))

        # object.Move_within_file(start, length, point)
        tkinter.messagebox.showinfo("Message", "Process Complete")
        root1.destroy()

    root1 = Tk()
    root1.geometry("400x350")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    open_label = Label(create_frame,text="Enter the starting point", width=30, height=2,padx=30)
    open_label.pack(pady=10)

    open_text=Text(create_frame,width=20,height=1,padx=0)
    open_text.pack(pady=10)

    create_label = Label(create_frame, text="Enter the size of the string", width=10, height=2, padx=30)
    create_label.pack(pady=10)

    create_text = Text(create_frame, width=20, height=1, padx=0)
    create_text.pack(pady=10)

    overwite_label = Label(create_frame, text="Enter the point where you want to move", width=30, height=2, padx=30)
    overwite_label.pack(pady=10)

    overwite_text = Text(create_frame, width=20, height=1, padx=0)
    overwite_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=move_save)
    create_button.pack(pady=10)



    root1.mainloop()

def memory_map(s1):
    def memory_map_save():
        # output = open("outputfile.txt", 'r')
        # content=output.read()
        func_name = "showm"
        s1.send(func_name.encode("utf-8"))
        time.sleep(0.5)
        content=s1.recv(500).decode("utf-8")
        create_text.insert(END,content)


    # object.show_memory_map()

    root1 = Tk()
    root1.geometry("600x450")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()



    create_text = Text(create_frame, width=70, height=20, padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Show", command=memory_map_save)
    create_button.pack(pady=10)

    root1.mainloop()



def download(s1):
    func_name = "download"
    s1.send(func_name.encode("utf-8"))
    time.sleep(0.5)
    content = s1.recv(10000)
    sample=open("sample.dat","wb")
    sample.write(content)
    tkinter.messagebox.showinfo("Message", "File Downloaded")



def main_gui(s1,name,root1):
        root1.destroy()
        text_user="Welcome :"+ name
        root = Tk()
        root.title('File management System')
        root.geometry("500x600")
        root.configure(bg='#3b93ff')

        button_frame=Frame(root,bg='#3b93ff')
        button_frame.pack()

        create_label=Label(button_frame,text=text_user,font=('poppins',18,'bold'))
        create_label.grid(row=0,column=0,pady=10)

        create_button=Button(button_frame,text="Create File",command=lambda:create_file(s1),bg='black',fg='white')
        create_button.grid(row=1,column=0,pady=10)

        delete_button=Button(button_frame,text="Delete File",command=lambda:delete_file(s1),bg='black',fg='white')
        delete_button.grid(row=2,column=0,pady=10)

        open_button=Button(button_frame,text="Open a File",command=lambda:open_file(s1),bg='black',fg='white')
        open_button.grid(row=3,column=0,pady=10)

        read_button=Button(button_frame,text="Read a File",command=lambda:read_file(s1),bg='black',fg='white')
        read_button.grid(row=4,column=0,pady=10)

        close_button=Button(button_frame,text="Close a File",command=lambda:close_file(s1),bg='black',fg='white')
        close_button.grid(row=5,column=0,pady=10)

        write_button=Button(button_frame,text="Write to a File",command=lambda:write_file(s1),bg='black',fg='white')
        write_button.grid(row=6,column=0,pady=10)

        append_button=Button(button_frame,text="Append in a File",command=lambda:append_file(s1),bg='black',fg='white')
        append_button.grid(row=7,column=0,pady=10)

        write_specific_button=Button(button_frame,text="Write at specific point",command=lambda:write_specific_file(s1),bg='black',fg='white')
        write_specific_button.grid(row=8,column=0,pady=10)

        truncate_button=Button(button_frame,text="Truncate a File",command=lambda:truncate_file(s1),bg='black',fg='white')
        truncate_button.grid(row=9,column=0,pady=10)

        move_button=Button(button_frame,text="Move file",command=lambda:move_file(s1),bg='black',fg='white')
        move_button.grid(row=10,column=0,pady=10)

        showm_button=Button(button_frame,text="Show memory map",command=lambda:memory_map(s1),bg='black',fg='white')
        showm_button.grid(row=11,column=0,pady=10)

        download_button = Button(button_frame, text="Download Sample.dat file", command=lambda:download(s1),
                                      bg='black', fg='white')
        download_button.grid(row=12, column=0, pady=10)

        read_specific_button=Button(button_frame,text="Read a File from specific point",command=lambda:read_specific_file(s1),bg='black',fg='white')
        read_specific_button.grid(row=13,column=0,pady=10)

        root.mainloop()

# main_gui()


def username(s1):

    def user():
        name = create_text.get(1.0, 'end-1c')
        main_gui(s1,name,root1)




    root1 = Tk()
    root1.geometry("300x250")
    create_frame = Frame(root1, bg='#3b93ff')
    root1.configure(bg='#3b93ff')
    create_frame.pack()

    create_label = Label(create_frame,text="Enter Your Name", width=10, height=2,padx=30)
    create_label.pack(pady=10)

    create_text=Text(create_frame,width=20,height=1,padx=0)
    create_text.pack(pady=10)

    create_button = Button(create_frame, text="Save", command=user)
    create_button.pack(pady=10)



    root1.mainloop()




for i in range(2):
        thread = threading.Thread(target=connect, args=())  # Separate thread for output status reporting
        #thread.setDaemon(True)
        thread.start()