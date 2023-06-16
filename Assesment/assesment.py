from tkinter import*

def quit():
    main_window.destroy()

def print_hire_details ():
    name_count=0
    print("Row\tName\t\tReceipt number\t\tItem Hired\tNumber Hired")
    while name_count < counters ['total_entries'] :
        print(name_count,"\t", customer_details[name_count][0], "\t\t",customer_details[name_count][2],"\t",customer_details[name_count][3])
        name_count += 1
        counters['name_count'] = name_count
        Label(main_window, font='bold', text="Row").grid(column=0, row=7)
        Label(main_window, font='bold', text="Full Name").grid(column=1, row=7)
        Label(main_window, font='bold', text="Item hired").grid(column=2, row=7)
        Label(main_window, font='bold', text="Amount Hired").grid(column=3, row=7)
        Label(main_window, font='bold', text="Receipt Number").grid(column=4, row=7)
        name_count = 0
        while name_count < counters['total_entries']:
            Label(main_window, text=name_count).grid(column=0, row=name_count + 8)
            Label(main_window, text=customer_details[name_count][0]).grid(column=1, row=name_count + 8)
            Label(main_window, text=customer_details[name_count][2]).grid(column=2, row=name_count + 8)
            Label(main_window, text=customer_details[name_count][3]).grid(column=3, row=name_count + 8)
            Label(main_window, text=customer_details[name_count][1]).grid(column=4, row=name_count + 8)
            name_count += 1

def append_name ():
    customer_details.append([entry_customer_name.get(),entry_receipt_number.get(),entry_hire_item.get(),entry_number_hired.get()])
    current_customer_name = entry_customer_name.get()
    entry_customer_name.delete(0,'end')
    entry_receipt_number.delete(0,'end')
    entry_hire_item.delete(0,'end')
    entry_number_hired.delete(0,'end')
    counters['total_entries'] += 1

def delete_row ():
    del customer_details[int(delete_item.get())]
    counters['total_entries'] -= 1
    delete_item.delete(0,'end')

def main():
    total_entries=0
    Label(main_window, text="Customer Name") .grid(column=0, row=0)
    Label(main_window, text="Receipt Number") .grid(column=0, row=1)
    Label(main_window, text="Item Hired") .grid(column=0, row=2)
    Label(main_window, text="Number Hired") .grid(column=0, row=3)
    Label(main_window, text="Row #") .grid(column=0, row=4)

    Button(main_window, text="Quit" , command=quit, width=10).grid(column=2, row=0)
    Button(main_window, text="Append Details",command=append_name) .grid(column=2, row=1)
    Button(main_window, text="Print Details",command=print_hire_details,width=10) .grid(column=2, row=2)
    Button(main_window, text="Delete Row",command=delete_row,width=10) .grid(column=2, row=3)
    main_window.mainloop()

counters = {'total_entries': 0, 'name_count': 0}

def validate_letter_space_input(new_value):
    if new_value.replace(" ", "").isalpha() or new_value == "":
        return True
    return False

def validate_number(new_value):
    if new_value.isdigit() or new_value == "":
        return True
    return False

main_window=Tk()
customer_details=[]
counters = {'total_entries':0,'name_count':0}
entry_customer_name = Entry(main_window, validate="key")
entry_customer_name['validatecommand'] = (entry_customer_name.register(validate_letter_space_input), '%P')
entry_customer_name.grid(column=1, row=0)
entry_receipt_number = Entry(main_window, validate="key")
entry_receipt_number['validatecommand'] = (entry_receipt_number.register(validate_number), '%P')
entry_receipt_number.grid(column=1, row=1)
entry_item_hired = Entry(main_window, validate="key")
entry_item_hired['validatecommand'] = (entry_item_hired.register(validate_letter_space_input), '%P')
entry_item_hired.grid(column=1, row=2)
entry_number_hired = Entry(main_window, validate="key")
entry_number_hired['validatecommand'] = (entry_number_hired.register(validate_number), '%P')
entry_number_hired.grid(column=1, row=3)
delete_item = Entry(main_window)
delete_item.grid(column=1,row=4)

total_entries=0

main_window.config(bg="#FF91AF")
main()