"""
===1. 跟昨天一樣 ===
商品後台/ 公司職員的  ERP

請多使用以下的東西

107-GUI-Spinbox-數入框有上下按鈕
104-GUI-combobox-下拉式選單
106-GUI-Text-多行顯示輸入
100-GUI-statusBar-easy

日期
"""

import tkinter as tk
from tkinter import ttk

# 視窗設定
root=tk.Tk()
root.wm_title("彤媽媽麵食館點餐系統")
root.resizable(0,0)
root.geometry("1100x500")
root.configure(bg="#EBBC4E")
# 函數設定: 根據選取資料輸出

def food():

    global fookOrderingTree
    text_content = text.get('1.0', 'end')
    foodOrderingTree.insert("", tk.END, values=(foodnameCB.get(), foodtypeRadioVar.get(), optionsRadioVar.get(),current_value.get(), text_content))
def  foodselected(event):
    print()
# 按鈕，按下後 修改資料到treeview
counter1=0
def  changeselected():
   global counter1
   global foodOrderingTree
   selected = foodOrderingTree.focus()
   foodOrderingTree.item(selected, text="", values=( foodnameCB.get(), foodtypeRadioVar.get(), optionsRadioVar.get(),  current_value.get()))

   # foodOrderingTree.item(selected, text="", values=(str(counter1),str(counter1)+'@example.com'))
   counter1=counter1+1

# 函數設定: 根據 Tree 資料輸出
def foodselected2(event):
    for selected_item in foodOrderingTree.selection():
        item = foodOrderingTree.item(selected_item)
        record = item['values']
        print(record)
        currentOrderVar.set(record)

def delectData():
    global foodOrderingTree
    for selected_item in foodOrderingTree.selection():
        foodOrderingTree.delete(selected_item)





# Menu 選單設定
mainmenu = tk.Menu()        # 創造主選單
menu1=tk.Menu(tearoff=0)    # 創造子選單 1
menu2=tk.Menu(tearoff=0)    # 創造子選單 2
root.config(menu=mainmenu)
mainmenu.add_cascade(label="功能",menu=menu1)
mainmenu.add_cascade(label="設定",menu=menu2)
menu1.add_command(label="查詢")
menu1.add_command(label="離開",command=root.destroy)
menu2.add_command(label="更新")

# 標籤設定
foodname=tk.Label(text="品名",font=("Arial",18),bg="#EBBC4E")
foodname.place(x=10,y=10)
foodtype=tk.Label(text="種類",font=("Arial",18),bg="#EBBC4E")
foodtype.place(x=10,y=70)
options=tk.Label(text="選項",font=("Arial",18),bg="#EBBC4E")
options.place(x=210,y=10)
orderquantity=tk.Label(text="訂購數量",font=("Arial",18),bg="#EBBC4E")
orderquantity.place(x=380,y=10)
orderquantity=tk.Label(text="備註",font=("Arial",18),bg="#EBBC4E")
orderquantity.place(x=423,y=50)
currentGood=tk.Label(root,text="目前訂單: ",font=("Arial",12),bg="#EBBC4E")
currentGood.place(x=10,y=230)
currentOrderVar=tk.StringVar()
currentOrder=tk.Label(root,textvariable=currentOrderVar,font=("Arial",14),bg="#EBBC4E")
currentOrderVar.set("無訂單")
currentOrder.place(x=85,y=227)

# 品名 ComboBox
foodnameCBVar=tk.IntVar()
foodnameCBVar.set("牛肉")
foodnameCB=ttk.Combobox(root,width=8,textvariable=foodnameCBVar)
foodnameCB["values"]=("牛肉","肉絲","宮保雞丁","干貝醬","蝦仁","海鮮") # 其他方法?
foodnameCB.place(x=70,y=10)

# 種類 Radiobutton
foodtypeRadioVar=tk.StringVar()
foodtypeRadioVar.set("炒飯")
foodtypeRadio=tk.Radiobutton(root,text="炒飯",variable=foodtypeRadioVar,value="炒飯",font=("Arial",14),bg="#EBBC4E")
foodtypeRadio.place(x=60,y=70)
foodtypeRadio=tk.Radiobutton(root,text="炒黃麵",variable=foodtypeRadioVar,value="炒黃麵",font=("Arial",14),bg="#EBBC4E")
foodtypeRadio.place(x=60,y=110)
foodtypeRadio=tk.Radiobutton(root,text="炒烏龍麵",variable=foodtypeRadioVar,value="炒烏龍麵",font=("Arial",14),bg="#EBBC4E")
foodtypeRadio.place(x=60,y=150)

# 選項1 Radiobutton
optionsRadioVar=tk.StringVar()
optionsRadioVar.set("加辣")
optionsRadio=tk.Radiobutton(root,text="加辣",variable=optionsRadioVar,value="加辣",font=("Arial",14),bg="#EBBC4E")
optionsRadio.place(x=270,y=10)
optionsRadio=tk.Radiobutton(root,text="不加辣",variable=optionsRadioVar,value="不加辣",font=("Arial",14),bg="#EBBC4E")
optionsRadio.place(x=270,y=50)


# 選項2 Radiobutton
optionssRadioVar=tk.StringVar()
optionssRadioVar.set("加蔥")
optionssRadio=tk.Radiobutton(root,text="加蔥",variable=optionssRadioVar,value="加蔥",font=("Arial",14),bg="#EBBC4E")
optionssRadio.place(x=270,y=90)
optionssRadio=tk.Radiobutton(root,text="不加蔥",variable=optionssRadioVar,value="不加蔥",font=("Arial",14),bg="#EBBC4E")
optionssRadio.place(x=270,y=130)


# 訂購數量數字調整 Spinbox
def value_changed():
    print(current_value.get())

current_value = tk.StringVar(value=0)
spin_box = ttk.Spinbox(
    root,width=8,
    from_=0,
    to=30,
    textvariable=current_value,
    command=value_changed)
spin_box.place(x=490,y=10)

# 建立訂單 Button
placingOrder=tk.Button(root,text="建立訂單",font=("Arial",12),command=food)
placingOrder.place(x=685,y=200)

# Tree
colname=("品名","種類","選項","訂購數量","備註") # 欄位名稱供下參數使用
foodOrderingTree=ttk.Treeview(root,columns=colname,show="headings") # headings vs tree 設定是否僅顯示資料


foodOrderingTree.place(x=10,y=260,width=1100)
#foodOrderingtree.colname()
foodOrderingTree.heading("品名",text="品名")
foodOrderingTree.heading("種類",text="種類")
foodOrderingTree.heading("選項",text="選項")
foodOrderingTree.heading("訂購數量",text="訂購數量")
foodOrderingTree.heading("備註",text="備註")
# 選取 Tree 的值時執行函式
foodOrderingTree.bind('<<TreeviewSelect>>',foodselected)

# 備註多行的輸入元件
text = tk.Text(root,width=39,height=10)
text.place(x=490,y=50)
text.insert('7.0', '請輸入備註')
# text['state'] = 'disabled'  # 顯示專用，不能寫資料

# 備註按鈕
def fun1():
    text_content = text.get('1.0', 'end')
    print(text_content)


button1 = tk.Button(root, text="press me",command=fun1)
button1.place(x=595,y=160)

#頁面拉桿
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")


#新增修改刪除按鍵
btn1=tk.Button(root,text="新增產品",command=food).place(x=340,y=200)
btn2=tk.Button(root,text="修改產品",command=changeselected).place(x=420,y=200)
btn3=tk.Button(root,text="刪除產品",command=delectData).place(x=500,y=200)



#頁面底下文字
foodselectedbar = tk.Label(root, text="E0612系統", bd=1, relief=tk.SUNKEN, anchor=tk.W)
foodselectedbar.pack(side=tk.BOTTOM, fill=tk.X)






root.mainloop()
