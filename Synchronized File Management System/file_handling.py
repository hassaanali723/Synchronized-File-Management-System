from linked_list import linked_list_class


class fileHandling:

    def __init__(this):
        p = ""
        try:
            this.file = open("sample.dat", "r+")
            p = this.file.read()
            this.file.close()
        except:
            pass
        this.file = open("sample.dat", "a+")
        this.file_name = ""
        this.llist = linked_list_class()
        this.llist.get_data(p)

    def create_file(this, fname):
        this.file_name = fname + ".txt"
        try:
            this.file.close()
            this.file = open("sample.dat", "a+")
            this.file.write("#" + fname)
            this.file.close()
            this.file = open("sample.dat", "w+")
        except:
            pass
        print("File is Created\n")

    def delete_file(this, fname):
        this.file_name = ""
        try:
            this.file.close()
            this.file = open("sample.dat", "w+")

            this.llist.deleteNode(fname + ".txt")
            text = this.llist.print_list()
            this.file.write(text)
            this.file.close()
            this.file = open("sample.dat", "a+")
            print("File is Deleted\n")
        except:
            pass

    def open_file(this, fname, mode):
        this.file_name = fname + ".txt"
        print("File is Opened\n")
        # return f

    def close_file(this, fname):
        this.file_name = fname + ".txt"
        print("File is Closed\n")


    def Write_to_File(this, write_at, text,ques):
        print("Do you want to Overwrite? If Yes then write y ")
        # cond = input("Enter you answer : ")
        if ques == "y":
            this.write_at_overwrite(int(write_at), text)
        else:
            this.write_at_no_overwrite(int(write_at), text)

        # write_at_first_time
    def write_to_file(this, text):
            try:
                this.file.close()
                this.file = open("sample.dat", "w+")
                v = this.file
                this.llist.insert_node(text, this.file_name)
                text = this.llist.print_list()
                v.write(text)
                this.file.close()
                this.file = open("sample.dat", "a+")
                print("Text has been written\n")
            except:
                pass

    def write_at_overwrite(this, write_at, text):
            try:
                this.file.close()
                this.file = open("sample.dat", "w+")
                v = this.file
                s = text
                p = write_at
                this.llist.write_data_overwrite(int(p), s, this.file_name)
                t = this.llist.print_list()
                v.write(t)
                this.file.close()
                this.file = open("sample.dat", "a+")
                print("Text has been written\n")
            except:
                pass

    def write_at_no_overwrite(this, write_at, text):
            try:
                this.file.close()
                this.file = open("sample.dat", "w+")
                v = this.file
                s = text
                p = write_at
                this.llist.write_data_without_overwrite(int(p), s, this.file_name)
                t = this.llist.print_list()
                v.write(t)
                this.file.close()
                this.file = open("sample.dat", "a+")
                print("Text has been written\n")
            except:
                pass

    def Read_From_File(this):
        t = this.llist.read_file(this.file_name)
        print(t)
        return t

    # Write in End

    def append_file(this, text):
        try:
            this.file.close()
            this.file = open("sample.dat", "w+")
            v = this.file
            s = text
            this.llist.add_data(s, this.file_name)
            t = this.llist.print_list()
            v.write(t)
            this.file.close()
            this.file = open("sample.dat", "a+")
            print("Text Has been Appended\n")
        except:
            pass

    def Move_within_file(this, start, size, target):
        try:
            this.file.close()
            this.file = open("sample.dat", "w+")
            v = this.file
            p = start
            s = target
            size = size
            this.llist.move_data_ll(int(p), int(s), int(size), this.file_name)
            t = this.llist.print_list()
            v.write(t)
            this.file.close()
            this.file = open("sample.dat", "a+")
            print("Text Has been Moved\n")
        except:
            pass

    def read_from_file(this, start, size):
        try:
            this.file.close()
            this.file = open("sample.dat", "r+")
            v = this.file.name
            p = start
            size = size
            try:
                text = this.llist.read_file_at_point(this.file_name, int(p), int(size))
                print(text)
                return text
                this.file.close()
                this.file = open("sample.dat", "a+")
            except:
                this.file.close()
                this.file = open("sample.dat", "a+")
                print("")
        except:
            pass

    def truncate(this, maxSize):
        v = this.file
        name = v.name
        try:
            this.file.close()
            this.file = open("sample.dat", "w+")
            this.llist.turncate(int(maxSize), this.file_name)
            v = this.file
            t = this.llist.print_list()
            this.file.write(t)
            this.file.close()
            this.file = open("sample.dat", "a+")
            print("File has been Truncated\n")
        except:
            this.file = open("sample.dat", "w+")
            this.llist.turncate(int(maxSize), this.file_name)
            t = this.llist.print_list()
            v = this.file
            this.file.write(t)
            this.file.close()
            this.file = open("sample.dat", "a+")
            print("File has been Truncated\n")

    def show_memory_map(this):
        try:
            this.llist.memory_map()
        except:
            pass

    def system_exit(this):
        this.file.close()

