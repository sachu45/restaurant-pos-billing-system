# Restaurant POS Billing System

A desktop-based Restaurant Point of Sale (POS) and Billing System developed using Python and Tkinter. The application helps restaurant staff manage customer orders, calculate bills automatically, generate PDF invoices, and print receipts through a simple graphical interface.

## About the Project

This project was built to understand how restaurant billing systems work in real-world environments. The application allows users to select food items from different menu categories, generate customer bills, calculate taxes automatically, and save invoices as PDF files.

The system provides a clean and user-friendly interface that makes billing faster and reduces manual calculations.

## Features

### Menu Management

* Categorized food menu
* South Indian dishes
* Dosa varieties
* Uthappam varieties
* Meals section
* Chinese dishes
* Curry selections
* Tandoor bread items

### Order Management

* Add items with a single click
* Automatic quantity updates
* Real-time order tracking
* Live receipt preview
* Multiple item billing

### Billing System

* Automatic bill generation
* Subtotal calculation
* GST calculation (5%)
* Grand total calculation
* Date and time stamping

### PDF Invoice Generation

* Generate customer invoices as PDF files
* Automatically save bills locally
* Printable invoice format

### Receipt Printing

* Print customer bills directly
* Supports Windows, Linux, and macOS

### User Interface

* Category-based navigation
* Dynamic menu display
* Live receipt window
* Simple and easy-to-use layout
* Real-time clock display

## Technologies Used

* Python
* Tkinter
* ReportLab
* Datetime Module
* OS Module
* Tempfile Module

## Project Structure

```text
Restaurant-POS-Billing-System/
│
├── Restaurant_pos.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── screenshots/
    ├── dashboard.png
    ├── order_page.png
    └── bill_preview.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/sachu45/restaurant-pos-billing-system.git
```

Move into the project folder:

```bash
cd restaurant-pos-billing-system
```

Install the required package:

```bash
pip install reportlab
```

Run the application:

```bash
python Restaurant_pos.py
```

## Requirements

Create a requirements.txt file:

```txt
reportlab
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

## How the System Works

1. Launch the application.
2. Select a food category from the left panel.
3. Click menu items to add them to the order.
4. Review the live receipt preview.
5. Click **Generate Bill**.
6. The application calculates GST and total amount automatically.
7. A PDF invoice is generated and saved.
8. Print the bill if required.

## Sample Workflow

* Customer orders Masala Dosa and Idli.
* Items are added to the receipt window.
* The system calculates the subtotal.
* GST is applied automatically.
* Final bill is displayed.
* PDF invoice is generated.
* Receipt can be printed directly.

## What I Learned

While developing this project, I learned:

* GUI development using Tkinter
* Event-driven programming
* Working with dictionaries and data structures
* PDF generation using ReportLab
* File handling in Python
* Receipt and billing system design
* Desktop application development

## Future Improvements

Some features that can be added in future versions:

* Customer database
* SQLite integration
* Admin login system
* Inventory management
* Sales analytics dashboard
* QR code payments
* UPI payment integration
* Daily sales reports
* Multi-user support
* Cloud backup support

## Author

**Sarrvesh J R**

GitHub:
https://github.com/sachu45

LinkedIn:
https://www.linkedin.com/in/sarrvesh-jr

## License

This project is available for educational and learning purposes.
