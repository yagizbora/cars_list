import sqlite3
from tkinter import messagebox
import tkinter as tk


root = tk.Tk()
root.title('Cars')
root.geometry('+50+50')
root.resizable(False, False)
root.configure(bg='cyan')




def createtable():
    conn = sqlite3.connect('Cars.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cars (
        ID INTEGER PRIMARY KEY,
        Cars_Name TEXT NOT NULL,
        Model TEXT NOT NULL,
        NumberPlate INTEGER NOT NULL,
        Color TEXT NOT NULL,
        Price REAL NOT NULL
    )
    ''')

    conn.commit()
    conn.close()


def add_car():
    Cars_name = entry_Cars_name.get()
    Model = entry_Model.get()
    NumberPlate = entry_NumberPlate.get()
    Color = entry_Color.get()
    Price = entry_Price.get()

    if Cars_name and Model and NumberPlate and Color and Price:
        conn = sqlite3.connect('Cars.db')
        cursor = conn.cursor()

        sql_query = 'INSERT INTO Cars(Cars_Name, Model, NumberPlate, Color, Price) VALUES (?, ?, ?, ?, ?)'
        values = (Cars_name, Model, NumberPlate, Color, Price)

        cursor.execute(sql_query, values)
        conn.commit()
        conn.close()

        messagebox.showinfo('Mesaj', 'Araba başarı ile listeye eklendi')
        show_employees()

    else:
        messagebox.showerror('Hata', 'Lütfen tüm alanları doldurun')


def delete_car():
    selected_id = entry_id.get()
    conn = sqlite3.connect('Cars.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Cars WHERE ID = ?', (selected_id,))
    messagebox.showwarning("Mesaj", "Araba silindi!")
    conn.commit()
    conn.close()

    show_employees()


def update_employee():
    selected_id = entry_id.get()
    Cars_name = entry_Cars_name.get()
    Model = entry_Model.get()
    NumberPlate = entry_NumberPlate.get()
    Color = entry_Color.get()
    Price = entry_Price.get()

    conn = sqlite3.connect('Cars.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE Cars SET Cars_Name = ?, Model = ?, NumberPlate = ?, Color = ?, Price = ? WHERE ID = ?',
                   (Cars_name, Model, NumberPlate, Color, Price, selected_id))
    messagebox.showwarning("Mesaj", "Araba güncellendi")
    conn.commit()
    conn.close()

    show_employees()


def show_employees():
    conn = sqlite3.connect('Cars.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Cars')
    Cars = cursor.fetchall()

    Cars_list.delete(0, tk.END)
    for car in Cars:  # Dikkat: cars yerine car olarak değiştirildi
        Cars_list.insert(tk.END, f"ID:{car[0]} CarsName:{car[1]}, Model:{car[2]}, NumberPlate:{car[3]}, Color:{car[4]}, Price:{car[5]}")

    conn.close()
    
    
    
    
    
    
createtable()



label_Cars_name = tk.Label(root, text="Araç Adı:")
label_Cars_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_Cars_name = tk.Entry(root)
entry_Cars_name.grid(row=0, column=1, padx=10, pady=5)

label_Model = tk.Label(root, text="Model:")
label_Model.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_Model = tk.Entry(root)
entry_Model.grid(row=1, column=1, padx=10, pady=5)


label_NumberPlate = tk.Label(root, text="Plaka:")
label_NumberPlate.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_NumberPlate = tk.Entry(root)
entry_NumberPlate.grid(row=3, column=1, padx=10, pady=5)

label_Color = tk.Label(root, text="Renk:")
label_Color.grid(row=4, column=0, padx=10, pady=5, sticky="e")

entry_Color = tk.Entry(root)
entry_Color.grid(row=4, column=1, padx=10, pady=5)

label_Price = tk.Label(root, text="Fiyat:")
label_Price.grid(row=5, column=0, padx=10, pady=5, sticky="e")

entry_Price = tk.Entry(root)
entry_Price.grid(row=5, column=1, padx=10, pady=5)

button_add = tk.Button(root, text="Araç Ekle", command=add_car)
button_add.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

button_delete = tk.Button(root, text="Araç Sil", command=delete_car)
button_delete.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

button_update = tk.Button(root, text="Araç Güncelle", command=update_employee)
button_update.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

entry_id = tk.Entry(root, width=5)
entry_id.grid(row=9, column=1, padx=10, pady=5, sticky="w")

button_show_cars = tk.Button(root, text="Araçları Görüntüle", command=show_employees)
button_show_cars.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

label_id = tk.Label(root, text="ID:")
label_id.grid(row=9, column=0, padx=10, pady=5, sticky="e")

Cars_list = tk.Listbox(root, height=10, width=100)
Cars_list.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()