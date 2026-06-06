import tkinter as tk
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
import tempfile
import platform


menu_items = {
    "South Indian": {
        "Idli (2 Pcs)": 38, "Sambar Idli (Mini)": 84,
        "Vada": 34,"Idiyappam Coconut Milk": 57, 
        "Ghee Pongal": 84, "Poori Aloo": 84,
        "Sambar Vada": 49
    },
    "Dosa Grill": {
        "Plain Dosa": 79, "Masala Dosa": 119,
        "Butter Dosa": 124,"Ghee Roast": 124,
        "Ghee Podi Dosa": 129,"Mysoor Dosa": 119,
        "Onion Dosa": 119,"Podi Dosa": 119,
        "Kal Dosa": 119,"Gobi Peace Dosa": 144, 
        "Mushroom Dosa": 149,"Paneer Dosa": 159,
        "Khelvaragu Dosa":129,"Cashewnut Rava Dosa": 144,
        "Ghee Roast": 124,"Butter Dosa": 124,
    },
    "Uthappam": {
        "Plain Uthappam": 84, "Onion Uthappam": 134,
        "Podi Uthappam": 129,"Veg Uthappam": 139,
        "Mushroom Uthappam": 134,"Onion Uthappam": 134,
        "Peas Uthappam": 139
    },

    "Meals": {
        "Parcel Meal Spl":143,"Parcel Meal Budget":86},

    "Chinese Appetizers": {
        "Gobi Munchurian": 194, "Mushrom Munchurian": 199,
        "Chilli Panner": 209
    },    
    
    "Chinese Wok": {
        "Veg Fried Rice": 184, "Gobi Fried Rice": 189,"Mushroom Fried Rice":189,"Panner Fried Rice":199,
        "Schezhuan Noodle": 189, "Schezhuan Paneer Noodle": 204
    },
    "Curry Pot": {
        "Gobi Varutharacha Curry": 199,
        "Kalan Milakattahu Gravy": 209,
        "Kalan Kurma": 199
    },
    "Freshly Tandoor Bread": {
        "Nan/Butter NAN": 63.5,
        "Roti": 62,
        "Pulka(2pcs)": 54,
        "Cheese Nan": 89,
        "Kashmiri Nan": 89
        
    }
}

BG_COLOR = "#D1ecff"
BTN_COLOR = "#ffffff"
TXT_COLOR = "#34729c"
order = {}

# CORE FUNCTIONS 

def add_to_order(item, price):
    if item in order:
        qty, unit_price = order[item]
        order[item] = (qty + 1, unit_price)
    else:
        order[item] = (1, price)
    update_receipt_preview()

def update_receipt_preview():
    receipt.delete("1.0", tk.END)
    receipt.insert(tk.END, "Restaurant\n")
    receipt.insert(tk.END, "  Anna Nagar, Lalgudi - 621651\n")
    receipt.insert(tk.END, "-"*40 + "\n")
    receipt.insert(tk.END, "Item                  Qty   Amount\n")
    receipt.insert(tk.END, "-"*40 + "\n")
    for item, (qty, price) in order.items():
        line_total = qty * price
        receipt.insert(tk.END, f"{item:<20} x{qty:<2} ₹{line_total:>6.2f}\n")

def generate_bill():
    update_receipt_preview()
    total = sum(q * p for q, p in order.values())
    tax = total * 0.05
    grand_total = total + tax
    now = datetime.datetime.now()
    receipt.insert(tk.END, "-"*40 + "\n")
    receipt.insert(tk.END, f"Tax (5%){'':<22} ₹{tax:>6.2f}\n")
    receipt.insert(tk.END, f"Total{'':<25} ₹{grand_total:>6.2f}\n")
    receipt.insert(tk.END, "-"*40 + "\n")
    receipt.insert(tk.END, f"Date: {now.strftime('%d-%b-%Y')}   Time: {now.strftime('%I:%M:%S %p')}\n")
    receipt.insert(tk.END, "       Thank you! Visit again! 🙂    ")
    receipt.insert(tk.END, "   Ph:78459 27934")
    save_pdf()

def clear_order():
    order.clear()
    show_default_receipt()

def save_pdf():
    now = datetime.datetime.now()
    filename = f"bill_{now.strftime('%d%b%Y_%H-%M-%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=A4) # type: ignore
    text = receipt.get("1.0", tk.END).splitlines()
    text_obj = c.beginText(40, 800)
    text_obj.setFont("Helvetica", 12)
    for line in text:
        text_obj.textLine(line)
    c.drawText(text_obj)
    c.save()
    try:
        os.startfile(filename)
    except AttributeError:
        os.system(f'xdg-open "{filename}"')

def print_bill():
    bill_text = receipt.get("1.0", tk.END)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8') as temp:
        temp.write(bill_text)
    if platform.system() == "Windows":
        os.startfile(temp.name, "print")
    elif platform.system() == "Darwin":
        os.system(f"lp '{temp.name}'")
    elif platform.system() == "Linux":
        os.system(f"lp {temp.name}")

def show_default_receipt():
    receipt.delete("1.0", tk.END)
    now = datetime.datetime.now()
    receipt.insert(tk.END, "     Restaurant\n")
    receipt.insert(tk.END, "   Welcome! Select items to begin\n")
    receipt.insert(tk.END, "  Anna Nagar, Lalgudi - 621651\n")
    receipt.insert(tk.END, "-"*40 + "\n")
    receipt.insert(tk.END, f"Date: {now.strftime('%d-%b-%Y')}   Time: {now.strftime('%I:%M:%S %p')}\n")
    receipt.insert(tk.END, "-"*40 + "\n")

def show_category(category):
    for widget in scrollable_frame.winfo_children():
        widget.destroy()
    for item, price in menu_items[category].items():
        tk.Button(scrollable_frame, text=f"{item} - ₹{price}", bg=BTN_COLOR, fg=TXT_COLOR,
                  anchor='w', width=40,
                  command=lambda i=item, p=price: add_to_order(i, p)).pack(pady=1)

# GUI SETUP 
root = tk.Tk()
root.title(" Restaurant POS")
root.geometry("1100x680")
root.config(bg=BG_COLOR)

#  HEADER 
top_frame = tk.Frame(root, bg=BG_COLOR)
top_frame.pack(fill=tk.X)

tk.Label(top_frame, text="Restaurant POS", bg=BG_COLOR, fg=TXT_COLOR,
         font=("Helvetica", 20, "bold")).pack(side=tk.LEFT, padx=10, pady=10)
clock_label = tk.Label(top_frame, bg=BG_COLOR, fg=TXT_COLOR, font=("Helvetica", 12, "bold"))
clock_label.pack(side=tk.RIGHT, padx=10)

def update_time():
    clock_label.config(text=datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p"))
    root.after(1000, update_time)
update_time()

#  MAIN AREA 
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Category Panel
category_frame = tk.Frame(main_frame, bg=BG_COLOR)
category_frame.pack(side=tk.LEFT, fill=tk.Y)
for category in menu_items:
    tk.Button(category_frame, text=category, bg="#1e5470", fg="white",
              font=("Helvetica", 12, "bold"), width=20,
              command=lambda c=category: show_category(c)).pack(pady=5)

# Scrollable Menu Items
canvas = tk.Canvas(main_frame, bg=BG_COLOR, highlightthickness=0)
scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=BG_COLOR)

scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) # type: ignore
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT, fill=tk.Y, expand=False)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

# Receipt Window
receipt = tk.Text(main_frame, height=25, width=40, bg="#fffaf0", fg="#333")
receipt.pack(side=tk.RIGHT, padx=10)

# Right-side Buttons
right_button_frame = tk.Frame(main_frame, bg=BG_COLOR)
right_button_frame.pack(side=tk.RIGHT, anchor="se", pady=10, padx=10)

tk.Button(right_button_frame, text="Generate Bill", bg="#22C030", fg="white",
          command=generate_bill).pack(pady=5)

tk.Button(right_button_frame, text="Clear Order", bg="#e70d0d", fg="white",
          command=clear_order).pack(pady=5)

tk.Button(right_button_frame, text="Done", bg="#3A95CE", fg="white",
          command=print_bill).pack(pady=5)

# Initial View
first_category = list(menu_items.keys())[0]
show_category(first_category)
show_default_receipt()

root.mainloop()

