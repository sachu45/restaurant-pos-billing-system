# restaurant-pos-billing-system
A Python Tkinter-based Restaurant POS Billing System with order management, PDF invoice generation, receipt printing, and real-time billing.

This application allows restaurant staff to quickly create customer orders, generate bills, print receipts, and export invoices as PDF files.

---

## 📌 Features

### 🍴 Menu Management
- South Indian Menu
- Dosa Grill Menu
- Uthappam Menu
- Meals Section
- Chinese Appetizers
- Chinese Wok
- Curry Pot
- Freshly Tandoor Bread

### 🛒 Order Processing
- Add items with one click
- Automatic quantity updates
- Real-time receipt preview
- Dynamic bill calculation

### 💰 Billing System
- Automatic subtotal calculation
- 5% GST/Tax calculation
- Grand total generation
- Date & Time stamping

### 📄 PDF Invoice
- Export customer bills as PDF
- Auto-save generated invoices
- Professional bill format

### 🖨️ Printing Support
- Windows printing support
- Linux printing support
- macOS printing support

### ⏰ Live Clock
- Real-time clock display
- Current date and time updates every second

### 🧹 Order Management
- Clear current order
- Start new customer billing instantly

---

## 📸 Application Preview

### Main Interface

- Category Selection Panel
- Menu Items Display
- Receipt Preview Window
- Billing Controls

```
+------------------+----------------------+----------------+
| Categories       | Menu Items           | Receipt        |
|------------------|----------------------|----------------|
| South Indian     | Idli                 | Order Preview  |
| Dosa Grill       | Masala Dosa          | Total Amount   |
| Uthappam         | Ghee Roast           | GST            |
| Meals            | Fried Rice           | Grand Total    |
+------------------+----------------------+----------------+
```

---

## 🏗️ Project Structure

```bash
Restaurant-POS/
│
├── Restaurant_pos.py
├── README.md
├── requirements.txt
├── screenshots/
│   ├── home.png
│   ├── billing.png
│   └── receipt.png
│
└── generated_bills/
```

---

## ⚙️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Programming |
| Tkinter | GUI Development |
| ReportLab | PDF Generation |
| Datetime | Date & Time |
| OS Module | File Handling |
| Tempfile | Temporary Printing Files |

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/restaurant-pos.git
```

### 2. Move Into Project

```bash
cd restaurant-pos
```

### 3. Install Dependencies

```bash
pip install reportlab
```

### 4. Run Application

```bash
python Restaurant_pos.py
```

---

## 📦 Requirements

Create a file named:

### requirements.txt

```txt
reportlab
```

Install:

```bash
pip install -r requirements.txt
```

---

## 🔄 Workflow

### Step 1
Select a category from the left panel.

### Step 2
Click menu items to add them to the customer's order.

### Step 3
Review the live receipt preview.

### Step 4
Click:

- Generate Bill

System calculates:
- Subtotal
- GST (5%)
- Grand Total

### Step 5
Invoice PDF is automatically generated.

### Step 6
Print receipt using the Done button.

---

## 🧾 Sample Receipt

```txt
Restaurant
Anna Nagar, Lalgudi - 621651

--------------------------------
Item              Qty   Amount
--------------------------------
Masala Dosa       x2    ₹238
Idli              x1    ₹38

Tax (5%)          ₹13.80

Total             ₹289.80

Thank you!
Visit Again
```

---

## 🎯 Key Functionalities

### Order Management

```python
add_to_order()
```

Adds selected menu item.

### Receipt Preview

```python
update_receipt_preview()
```

Updates live bill view.

### Bill Generation

```python
generate_bill()
```

Calculates GST and final amount.

### PDF Export

```python
save_pdf()
```

Generates invoice PDF.

### Receipt Printing

```python
print_bill()
```

Prints bill across operating systems.

---

## 🌟 Future Enhancements

### Database Integration
- SQLite
- MySQL

### Authentication
- Admin Login
- Staff Login

### Dashboard
- Daily Sales
- Monthly Reports
- Revenue Analytics

### Customer Features
- Customer Database
- Loyalty Points
- Order History

### Inventory Management
- Stock Tracking
- Low Stock Alerts

### Cloud Support
- Online Backup
- Multi-Branch Access

### QR Billing
- UPI Payments
- QR Invoice Generation

---

## 🛡️ Error Handling

Current application handles:

- Empty Orders
- PDF Generation
- Cross-platform Printing
- File Creation

---

## 👨‍💻 Author

**Sarrvesh J R**

- GitHub: https://github.com/sachu45
- LinkedIn: https://www.linkedin.com/in/sarrvesh-jr

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork the project

📢 Share it with others

---

### Made with ❤️ using Python & Tkinter
