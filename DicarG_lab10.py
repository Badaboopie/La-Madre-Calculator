import tkinter as tk

###main###
window = tk.Tk()        #ROOT WINDOW

window.geometry("600x800")
window.title("La Madre's Grocery List Calculator")
window.configure(background = "antiquewhite1")

#Key down function
g_list = {}
            #For Adding Items
def additem_click():
    try:
        duplicate = False
        text_entry = str(item_name.get())  #gets the content of entry text box
        price = float(item_price.get())
        quantity = int(item_quantity.get())
            
        item_name.delete(0,"end")   
        item_price.delete(0,"end")
        item_quantity.delete(0,"end")
        output.delete(0.0,tk.END)

        Add_price.config(text="Enter the item Price", font=('Arial',12), fg='black')
        Add_quant.config(text="Enter the item Quantity", font=('Arial',12), fg='black')
            
        for keys in g_list.keys(): #will check for duplicates
                if text_entry.upper() in keys.upper():
                    result = "Sorry... We do not accept duplicates... Please Enter Again. XD"
                    duplicate = True
                    output.insert(tk.END, result)

        if duplicate is False:
                g_list[text_entry] = [price, quantity]
                result = g_list

    except ValueError:
        item_name.delete(0,"end")   #will clear the entry text box
        item_price.delete(0,"end")
        item_quantity.delete(0,"end")
        Add_price.config(text="Item Price: \n (Please Input a Float)", font=('Arial',12), fg= 'red')
        Add_quant.config(text="Item Quantity: \n (Please Input an Integer)", font=('Arial',12), fg= 'red')
        
            #For Removing Items    
def remove_click():
    checker = False
    remove_item = remove.get()
    remove.delete(0,'end')
    output.delete(0.0,tk.END)
    
    for keys in g_list.keys():
            if remove_item.upper() == keys.upper():
                remover = keys
                checker = True
    if checker == True:
        del g_list[remover]
    else:
        pass


            #imprimer(Print)
def print_click():
    output.delete(0.0,tk.END)
    title = "Item Name:\t Item Price:\t Item Quantity:\t \n"
    output.insert(tk.END, title)
    for keys,values in g_list.items(): # names, prices, quantity
            txt = keys,": \t",str("%.2f"% values[0]),": \t",str(values[1]),"\n"
            output.insert(tk.END, txt)

            ###CALCULATE COST
def calc_cost():
    totalcost = 0
    output.delete(0.0,tk.END)
    title = "Item Name: \t Item Price: \t Item Quantity: \t \n"
    output.insert(tk.END, title)
    for keys,values in g_list.items(): # names, prices, quantity
            txt = keys,": \t","%.2f"% values[0],": \t",values[1],"\n"
            output.insert(tk.END, txt)

    for keys,values in g_list.items():                          # prints the total cost
            totalcost += values[0] * values[1]

    total = "Total Cost: ","%.2f"% totalcost         
    output.insert(tk.END,total)

            ###EXIT BUTTON
def Exit_click():
    window.destroy()
    exit()
    
### Label
Label_title = tk.Label(window, text="La Madre's Grocery List Calculator", font = ("Arial", 18), bg='antiquewhite1')  #TITLE
Label_title.pack(padx=20, pady=20)



## label for textbox Item Name
Add_Item = tk.Label(window, text='Enter the item Name:', font= ('arial',12), bg='antiquewhite1')
Add_Item.pack()

### textbox entry for Add item Name
item_name = tk.Entry(window, width= 30, bg ='ivory2')
item_name.pack(padx=10, pady=10)




## label for textbox Item price
Add_price = tk.Label(window, text='Enter the item Price:', font= ('arial',12), bg='antiquewhite1')
Add_price.pack()

### textbox entry for price

item_price = tk.Entry(window, width= 30, bg ='ivory2')
item_price.pack(padx=10, pady=10)




## label for textbox Item Quantity
Add_quant = tk.Label(window, text='Enter the item Quantity:', font= ('arial',12), bg='antiquewhite1')
Add_quant.pack()

### textbox entry for quantity
item_quantity = tk.Entry(window, width= 30, bg ='ivory2')
item_quantity.pack(padx=10, pady=10)


### ADD ITEM BUTTON
add_button = tk.Button(window, text="Add Item", height=0 ,width=0, font=("Arial",14), command=additem_click)
add_button.pack()

### Remove Label
remove_L = tk.Label(window, text='Remove Item:', font= ('arial',12), bg='antiquewhite1')
remove_L.pack()

### Remove Entry Box
remove = tk.Entry(window, width= 30, bg ='ivory2')
remove.pack(padx=10, pady=10)

### REMOVE ITEM BUTTON
remove_button = tk.Button(window, text="Remove Item", height=0 ,width=0, font=("Arial",14), command=remove_click)
remove_button.pack()


### Third Row Button
buttonframe2 = tk.Frame(window)
buttonframe2.columnconfigure(0, weight=1)
buttonframe2.columnconfigure(1, weight=1)
buttonframe2.columnconfigure(2, weight=1)

#Print Button
btn1 = tk.Button(buttonframe2, text="Print Entire List", font=("Arial",14), command=print_click)
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)

#Calculate Cost Button
btn2 = tk.Button(buttonframe2, text="Calculate Cost", font=("Arial",14), command=calc_cost)
btn2.grid(row=1, column=1, sticky=tk.W+tk.E)

#Exit Program Button
btn2 = tk.Button(buttonframe2, text="Exit Program", font=("Arial",14), command=Exit_click)
btn2.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe2.pack(pady = 10)


#OUTPUT LABEL

label = tk.Label(window, font=("Arial", 14), text='Output:', bg='antiquewhite1')
label.pack(pady=10)

output = tk.Text(window, font=("Arial",14), bg='linen')
output.pack()


window.mainloop()
