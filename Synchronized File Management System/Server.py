import threading
import time
import socket
from file_handling import fileHandling


host=socket.gethostname()
IP=socket.gethostbyname(host)
print(IP)
port=9999

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.bind((IP, port))
s1.listen()
print("server is listening")

object = fileHandling()
dic_for_w={}
dic_for_r={}



def create_msg(conn):
    # while True:
      msg = conn.recv(64).decode("utf-8")
      print("File Name : ",msg)
      dic_for_w[msg]="0"
      dic_for_r[msg]=0

      object.create_file(msg)




      # msg1 = conn.recv(64).decode("utf-8")
      # print(msg1)

def write_msg(conn):
    msg = conn.recv(64).decode("utf-8")
    print("File text : ", msg)
    object.write_to_file(msg)

def open_file(conn):
    name = conn.recv(64).decode("utf-8")
    mode = conn.recv(64).decode("utf-8")
    print("File name : ", name)
    print("File mode : ", mode)
    print(dic_for_w)
    print(dic_for_r)
    if mode=="w" or mode=="a":
        if dic_for_w[name]=="0" and dic_for_r[name]==0:
            dic_for_w[name]="1"
            dic_for_r[name]=1
            object.open_file(name, mode)
            msg = "Opened!"
            conn.send(msg.encode("utf-8"))

        else:

            msg = "This file is opened by another client please try again!"
            conn.send(msg.encode("utf-8"))

    elif mode=="r":
        if dic_for_w[name]=="1":
            msg = "This file is opened by another client please try again!"
            conn.send(msg.encode("utf-8"))

        else:

           dic_for_r[name]+=1
           object.open_file(name, mode)
           msg = "Opened!"
           conn.send(msg.encode("utf-8"))



def delete_file(conn):
    msg = conn.recv(64).decode("utf-8")
    print("File deleted : ", msg)
    object.delete_file(msg)

def close_file(conn):
    print("close")
    msg = conn.recv(64).decode("utf-8")
    print("File closed : ", msg)
    object.close_file(msg)
    dic_for_w[msg]="0"
    dic_for_r[msg]-=1



def append_file(conn):
    msg = conn.recv(64).decode("utf-8")
    print("File appended : ", msg)
    object.append_file(msg)

def write_spec_file(conn):
    data = conn.recv(64).decode("utf-8")
    file_data = conn.recv(64).decode("utf-8")
    ques = conn.recv(64).decode("utf-8")
    print("File name : ", data)
    print("File data : ", file_data)
    print("File data : ", ques)

    object.Write_to_File(data, file_data, ques)

def truncate(conn):
    msg = conn.recv(64).decode("utf-8")
    print("File size : ", msg)
    object.truncate(msg)

def move(conn):
    start = conn.recv(64).decode("utf-8")
    length= conn.recv(64).decode("utf-8")
    point = conn.recv(64).decode("utf-8")
    print("File start : ", start)
    print("File length : ", length)
    print("File point : ", point)
    object.Move_within_file(start, length, point)



def read(conn):

    data=object.Read_From_File()
    conn.send(data.encode("utf-8"))


def reads(conn):
    start = conn.recv(64).decode("utf-8")
    time.sleep(0.2)

    end = conn.recv(64).decode("utf-8")

    print("File start : ", start)
    print("File end : ", end)
    text = object.read_from_file(start, end)
    conn.send(text.encode("utf-8"))

def showm(conn):
    object.show_memory_map()
    output = open("outputfile.txt", 'r')
    content = output.read()
    conn.send(content.encode("utf-8"))
    output.close()

def download(conn):
    file = open("sample.dat", 'rb')
    chunk = file.read(500000)
    conn.send(chunk)

def accept(s1):

    while True:
        conn, addr = s1.accept()
        print("server has accepted request")
        while True:
            msg=conn.recv(64).decode("utf-8")
            if msg=="create":
                create_msg(conn)
            if msg=="write":
                write_msg(conn)

            if msg=="open":
                open_file(conn)

            if msg=="delete":
                delete_file(conn)

            if msg=="close":
                close_file(conn)

            if msg=="append":
                append_file(conn)

            if msg=="writes":
                write_spec_file(conn)

            if msg=="truncate":
                truncate(conn)

            if msg=="move":
                move(conn)

            if msg=="read":
                read(conn)

            if msg=="reads":
                reads(conn)

            if msg=="showm":
                showm(conn)

            if msg=="download":
                download(conn)



for i in range(5):
        thread = threading.Thread(target=accept, args=(s1,))  # Separate thread for output status reporting
        #thread.setDaemon(True)
        thread.start()
