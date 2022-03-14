from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import *
from tkinter.font import Font
from PIL import ImageTk,Image
import datetime as dt

root = Tk()
root.title('Products Manager')
root.geometry('2000x1000')
# root.iconbitmap('images/app icon.ico')

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')
notebook.pack(fill='both', expand=1)

Home = Frame(notebook, width=750, height=450, bg='white')
Home.pack(fill='both', expand=1)
Products = Frame(notebook, width=750, height=450, bg='white')
Products.pack(fill='both', expand=1)
FAQ = Frame(notebook, width=750, height=450, bg='white')
FAQ.pack(fill='both', expand=1)
About = Frame(notebook, width=750, height=450, bg='white')
About.pack(fill='both', expand=1)

notebook.add(Home, text=f'{"Home":^20s}')
notebook.add(Products, text=f'{"Products":^20s}')
notebook.add(FAQ, text=f'{"FAQ":^20s}')
notebook.add(About, text=f'{"About":^20s}')


def saveProduct() :
    pass
    # x=dt.datetime.now()
    # isSuccessful = addProduct(
    #     name=txt_name.get(),
    #     quantity=txt_quantity.get(),
    #     price=txt_price.get(),
    #     time=(x.strftime('%x' + "  " + '%X'))
    # )
    #
    # if isSuccessful:
    #     messagebox.showinfo('Successful', "Product successfully added")
    #     add.destroy()
    # else:
    #     messagebox.showerror('Empty Field', 'All fields are required')


def createProducts():
    global add
    add = Toplevel()
    add.title('Add User')
    add.iconbitmap('images/app icon.ico')

    x = root.winfo_x()
    y = root.winfo_y()
    add.geometry("+%d+%d" % (x + 100, y + 100))

    global txt_quantity
    global txt_price
    global txt_name

    login_frame = Frame(
        add,
        width=550,
        height=550,
        bg='white',
        padx=20, pady=20,
    )
    login_frame.pack(padx=50, fill='both', expand=1)

    lbl_add = Label(
        login_frame,
        text='Add Product',
        font='verdana 25 bold',
        bg='white'
    )
    lbl_add.pack(pady=(10, 10))

    lbl_name = Label(
        login_frame,
        text='Product name',
        font='verdana 18', bg='white',
    )
    lbl_name.pack(anchor=W, pady=10)

    txt_name = Entry(
        login_frame,
        font='verdana 18', bg='white'
    )
    txt_name.pack(fill=X)

    lbl_price = Label(
        login_frame,
        text='Price',
        font='verdana 18', bg='white',
    )
    lbl_price.pack(anchor=W, pady=10)

    txt_price = Entry(
        login_frame,
        font='verdana 18', bg='white'
    )
    txt_price.pack(fill=X)

    lbl_quantity = Label(
        login_frame,
        text='Quantity',
        font='verdana 18', bg='white',
    )
    lbl_quantity.pack(anchor=W, pady=10)

    txt_quantity = Entry(
        login_frame,
        font='verdana 18', bg='white'
    )
    txt_quantity.pack(fill=X)

    btn_add = Button(
        login_frame,
        text='Add Product',
        width=20,
        bg='navy',
        font='verdana 20 bold', fg='black',
        command=saveProduct
    )
    btn_add.pack(pady=(50, 0))

    add.grab_set()


#                                             Home Screen
appBarFont = Font(
    family='Times',
    size=40,
    weight='bold',
)

appBar = Frame(Home, height=70, width=Home.winfo_screenwidth(), bg='navy', padx=0, pady=0)
appBar.pack()

spacer = Label(appBar, text=' ', bg='navy')
spacer.grid(row=0, column=0)
icon1 = ImageTk.PhotoImage(Image.open('images/shopping-cart.png'))

appIcon = Label(appBar, image=icon1, bg='navy')
appIcon.grid(row=0, column=1)
appName = Label(appBar, text='  PRODUCTS MANAGER INVENTORY SYSTEM                                                                                          ', bg='navy', font=appBarFont, fg='white')
appName.grid(row=0, column=2)

secAppBar = Frame(Home, height=30, width=Home.winfo_screenwidth(), bg='slate grey', padx=0, pady=0)
secAppBar.pack()

presentTime = dt.datetime.now()
Date = 'Date: ' + str(presentTime.date())
time = 'Time: ' + str(presentTime.strftime('%X'))

appTime = Label(secAppBar, text=time, fg='white', bg='slate grey', font=(50))
appTime.place(x=1150, y=0)
appDate = Label(secAppBar, text=Date, fg='white', bg='slate grey', font=(50))
appDate.place(x=1000, y=0)

container_frame = Frame(Home, padx=10, pady=10, bg='white')
container_frame.pack(pady=(50, 0))

lbl_title = Label(
    container_frame,
    text='WELCOME TO PRODUCTS MANAGER',
    font='verdana 30 bold',
    bg='white'
)
lbl_title.grid(row=0, column=0, columnspan=2, pady=(10, 60))

btn_add = Button(
    container_frame,
    text='Add Product',
    width=15,
    bg='navy',
    font='verdana 15', fg='black',
    command=createProducts
)
btn_add.grid(row=1, column=0, pady=(10, 60), padx=(200, 60))

#                                           Products Screen
styles = ttk.Style()
styles.theme_use('default')
styles.configure(
    "TreeView",
    background='#D3D3D3',
    foreground='black',
    rowheight=25,
    fieldbackground='#D3D3D3'
)

styles.map(
    'TreeView',
    background=[
        (
            'selected',
            '#347083'
        )
    ]
)

appBarFont = Font(
    family='Times',
    size=40,
    weight='bold',
)

appBar = Frame(Products, height=70, width=Home.winfo_screenwidth(), bg='navy', padx=0, pady=0)
appBar.pack()

spacer = Label(appBar, text=' ', bg='navy')
spacer.grid(row=0, column=0)
icon2 = ImageTk.PhotoImage(Image.open('images/shopping-cart.png'))

appIcon = Label(appBar, image=icon2, bg='navy')
appIcon.grid(row=0, column=1)
appName = Label(appBar, text='  PRODUCTS MANAGER INVENTORY SYSTEM                                                    '
                             '                                      ', bg='navy', font=appBarFont, fg='white')
appName.grid(row=0, column=2)

secAppBar = Frame(Products, height=30, width=Home.winfo_screenwidth(), bg='slate grey', padx=0, pady=0)
secAppBar.pack()

productsList = Label(secAppBar, text='Products Information', bg='slate grey', fg='white', font='verdana 15')
productsList.place(x=550, y=0)

productsFrame = Frame(Products, width=400)
productsFrame.pack()

frameScroll = Scrollbar(productsFrame)
frameScroll.pack(side=RIGHT, fill=Y)

productsTable = ttk.Treeview(
    productsFrame,
    show='headings',
    height=250,
    yscrollcommand=frameScroll.set,
    selectmode="extended"
)
productsTable.pack()
frameScroll.config(command=productsTable.yview())

productsTable['columns'] = ("S/N", 'Products Name', 'Quantity In Stock', 'Price per 1', 'Time')

productsTable.column("#0", width=50, stretch=NO)
productsTable.column("S/N", anchor=W, width=80)
productsTable.column('Products Name', anchor=W, width=400)
productsTable.column('Quantity In Stock', anchor=CENTER, width=400)
productsTable.column('Price per 1', anchor=CENTER, width=400)
productsTable.column('Time', anchor=CENTER, width=280)

productsTable.heading('#0', text='', anchor=W)
productsTable.heading("S/N", text="S/N", anchor=W)
productsTable.heading('Products Name', text='Products Name', anchor=CENTER)
productsTable.heading('Quantity In Stock', text='Quantity In Stock', anchor=CENTER)
productsTable.heading('Price per 1', text='Price per 1', anchor=CENTER)
productsTable.heading('Time', text='Date Added', anchor=CENTER)

productsTable.tag_configure('oddrow', background='white')
productsTable.tag_configure('evenrow', background='lightblue')


#                                           FAQ Screen
appBarFont = Font(
    family='Times',
    size=40,
    weight='bold',
)

appBar = Frame(FAQ, height=70, width=Home.winfo_screenwidth(), bg='navy', padx=0, pady=0)
appBar.pack()

spacer = Label(appBar, text=' ', bg='navy')
spacer.grid(row=0, column=0)
icon3 = ImageTk.PhotoImage(Image.open('images/shopping-cart.png'))

appIcon = Label(appBar, image=icon3, bg='navy')
appIcon.grid(row=0, column=1)
appName = Label(appBar, text='  PRODUCTS MANAGER INVENTORY SYSTEM                                                    '
                             '                                      ', bg='navy', font=appBarFont, fg='white')
appName.grid(row=0, column=2)

secAppBar = Frame(FAQ, height=35, width=Home.winfo_screenwidth(), bg='slate grey', padx=0, pady=0)
secAppBar.pack()

FAQLbl = Label(
    secAppBar,
    text='''Frequently Asked Questions''',
    bg='slate grey',
    fg='white',
    pady=5,
    font='verdana 15'
)
FAQLbl.place(x=550, y=0)

FAQ_question_Frame = Frame(FAQ, bg='white', height=FAQ.winfo_screenheight())
FAQ_question_Frame.place(x=430, y=150)

quest1 = Label(FAQ_question_Frame, text='-- How do i add a product in Product Manager ?', bg='white',
               font='Arial 12 bold')
quest1.grid(row=0, column=0)
ans1 = Label(FAQ_question_Frame, text="""In the home page you will see a button at the center click on the button, 
then fill out the required fields and click add product, the product should be added successfully.
""", bg='white', font='Arial 11')
ans1.grid(row=1, column=0)

quest2 = Label(FAQ_question_Frame, text='-- Where do i see the added product ?', bg='white',
               font='Arial 12 bold')
quest2.grid(row=2, column=0)
ans2 = Label(FAQ_question_Frame, text="""At the top left conner you will see a menu in the menu click on Products, 
it will navigate you to the Products page.
""", bg='white', font='Arial 11')
ans2.grid(row=3, column=0)

quest3 = Label(FAQ_question_Frame, text='-- How the see the application About page ?', bg='white',
               font='Arial 12 bold')
quest3.grid(row=4, column=0)
ans3 = Label(FAQ_question_Frame, text="""At the top left conner you will see a menu in the menu click on About, 
it will navigate you to the About page.
""", bg='white', font='Arial 11')
ans3.grid(row=5, column=0)

#                                           About Screen
appBarFont = Font(
    family='Times',
    size=40,
    weight='bold',
)

appBar = Frame(About, height=70, width=Home.winfo_screenwidth(), bg='navy', padx=0, pady=0)
appBar.pack()

spacer = Label(appBar, text=' ', bg='navy')
spacer.grid(row=0, column=0)
icon4 = ImageTk.PhotoImage(Image.open('images/shopping-cart.png'))

appIcon = Label(appBar, image=icon4, bg='navy')
appIcon.grid(row=0, column=1)
appName = Label(appBar, text='  PRODUCTS MANAGER INVENTORY SYSTEM                                                    '
                             '                                      ', bg='navy', font=appBarFont, fg='white')
appName.grid(row=0, column=2)

secAppBar = Frame(About, height=35, width=Home.winfo_screenwidth(), bg='slate grey', padx=0, pady=0)
secAppBar.pack()

AboutLbl = Label(
    secAppBar,
    text='About Project Manager',
    bg='slate grey',
    fg='white',
    font='verdana 15'
)
AboutLbl.place(x=550, y=0)

aboutContextFrame = Frame(About, bg='white', height=About.winfo_screenheight())
aboutContextFrame.place(x=200, y=300)

aboutContext = Label(aboutContextFrame, text='''
PRODUCT MANAGER INVENTORY SYSTEM is an inventory system made by New Horizon Software Development company. 
It is used to maintain and organise products all in one place. We hope you enjoy. 
Credits to Ariyo the developer''', bg='white', fg='black', font='verdana 15 bold')
aboutContext.pack()


def getData():
    global count
    # count = 0
    # db_cursor.execute("SELECT * FROM products")
    # productDetails = db_cursor.fetchall()
    #
    # for detail in productDetails:
    #     if count % 2 == 0:
    #         productsTable.insert(parent='', index='end', iid=count, text='',
    #                              values=(detail[0], detail[1], detail[2], '₦ ' + str(detail[3]), detail[4]),
    #                              tags=('evenrow',))
    #     else:
    #         productsTable.insert(parent='', index='end', iid=count, text='',
    #                              values=(detail[0], detail[1], detail[2], '₦ ' + str(detail[3]), detail[4]),
    #                              tags=('oddrow',))
    #     count += 1


getData()

root.mainloop()
