class Node:

    def __init__(this, data):
        this.data = data
        this.index = None
        this.total_size = 100
        this.id = None
        this.next = None


class linked_list_class:

    def __init__(this):
        this.l_size = 10000
        this.head = None
        this.total_nodes = 100
        this.nodes = 0


    def insert_node(this, new_data, n_id):

        new_node = Node(new_data)
        new_node.id = n_id
        i = 0
        if this.nodes <= this.total_nodes:
            if len(new_data) <= new_node.total_size:
                if this.head is None:
                    new_node.index = i
                    # new_node.size = len(new_data)
                    this.nodes = this.nodes + 1
                    i = i + 1
                    this.head = new_node
                    return

                last = this.head

                while (last.next):
                    last = last.next
                    i = i + 1

                last.next = new_node
                new_node.index = i + 1
                this.nodes = this.nodes + 1
            else:
                this.data_management(new_node, new_data, n_id)
        else:
            print("There no more new sectors available")

    def data_management(this, node, new_data, n_id):
        total_nodes = (len(new_data) // node.total_size) + 1

        for i in range(total_nodes):
            data_to_add = new_data[i * 100:(i + 1) * 100]
            this.insert_node(data_to_add, n_id)

    # append function

    def add_data(this, new_data, n_id):
        temp = this.head
        while temp:
            if temp.id == n_id:
                temp_size = temp.total_size - len(temp.data)
                if temp_size > 0:
                    temp.data = temp.data + new_data[:temp_size]

            temp = temp.next
        if temp_size < len(new_data):
            this.data_management(this.head, new_data[temp_size:], n_id)


    def print_list(this):
        temp = this.head
        text = ""
        while (temp):
            text = text + temp.data + "#" + temp.id + "\n"
            temp = temp.next
        return text

    def calculate_size(this):
        size_val = 1
        temp = this.head
        while (temp):
            size_val = size_val + 1
            temp = temp.next
        return (size_val * 100)



    def indices_order(this):
        temp = this.head
        i = 0
        while (temp):
            temp.index = i
            i = i + 1
            temp = temp.next

    def move_data_ll(this, start, to, size, n_id):
        temp = this.head
        text = ""
        while (temp):
            if (temp.id == n_id):
                text = text + temp.data
            temp = temp.next

        part_text = text[start:start + size]
        text = text[0:start:] + text[start + size::]
        text = text[0:to] + part_text + text[to:]
        r_text = text
        temp = this.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = text[i * 100:(i + 1) * 100]
                i = i + 1
                temp.data = data_to_add
            temp = temp.next
        return r_text

    def write_data_without_overwrite(this, write_at, text, n_id):
        temp = this.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        this.add_data(text, n_id)
        r_text = this.move_data_ll(len(o_text), write_at, len(text), n_id)
        return r_text

    def write_data_overwrite(this, write_at, text, n_id):
        temp = this.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        o_text = o_text[0:write_at:] + o_text[write_at + len(text)::]
        o_text = o_text[0:write_at] + text + o_text[write_at + len(text):]
        r_text = o_text
        temp = this.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = o_text[i * 100:(i + 1) * 100]
                i = i + 1
                temp.data = data_to_add
            temp = temp.next
        return r_text

    def delete_one_node(this, key):
        # Store head node
        temp = this.head

        if temp is not None:
            if temp.data == key:
                this.head = temp.next
                temp = None
                this.nodes = this.nodes - 1
                return

        while temp is not None:
            if temp.data == key:
                this.nodes = this.nodes - 1
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next

        temp = None

    def deleteNode(this, n_id):

        temp = this.head
        prev = None

        while (temp != None and temp.id == n_id):
            this.head = temp.next
            temp = this.head
            this.nodes = this.nodes - 1
        while (temp != None):

            while (temp != None and temp.id != n_id):
                prev = temp
                temp = temp.next
                this.nodes = this.nodes - 1

            if (temp == None):
                return this.head

            prev.next = temp.next

            temp = prev.next
        this.indices_order()



    def read_file(this, n_id):
        temp = this.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        return o_text

    # read data at a particular point
    def read_file_at_point(this, n_id, start, size):
        text = this.read_file(n_id)
        part_text = text[start:start + size]
        return part_text

    def turncate(this, maxSize, n_id):
        temp = this.head
        o_text = ""
        while (temp):
            if (temp.id == n_id):
                o_text = o_text + temp.data
            temp = temp.next
        part_text = o_text[0:maxSize]
        temp = this.head
        i = 0
        while (temp):
            if (temp.id == n_id):
                data_to_add = part_text[i * 100:(i + 1) * 100]
                i = i + 1
                temp.data = data_to_add
            temp = temp.next

        temp = this.head
        del_text = "The_Text_to_be_Truncated"
        while temp:
            if temp.id == n_id:
                if len(temp.data) < 1:
                    temp.data = del_text
                    this.delete_one_node(del_text)
            temp = temp.next

        temp = this.head
        while temp:
            if (temp.id == n_id):
                this.delete_one_node(del_text)
            temp = temp.next
        return part_text

    def memory_map(this):
        temp = this.head
        total_size = 0
        output = open("outputfile.txt", 'w')
        exlist = []
        while (temp):
            total_size = total_size + len(temp.data)
            print("File Name:", temp.id,
                  " Size of node occupying:" + str(len(temp.data)) + ' bytes', file=output)
            exlist.append(temp.id)
            temp = temp.next
        exlist = list(set(exlist))
        print("Memory Consumed: ", total_size, file=output)
        print("Memory alloted by user: ", this.calculate_size() - 100, file=output)
        print("Total Size: ", this.l_size, file=output)
        print("Total number of nodes : ", this.total_nodes, file=output)
        print("Remaining Divisions: ", this.total_nodes - this.nodes, file=output)
        print("Remaining Size : ", (100 + this.l_size - this.calculate_size()), file=output)

    def get_data(this, text):
        for line in text.splitlines():
            a_l = line.split("#")
            this.insert_node(a_l[0], a_l[1])
        this.indices_order()


