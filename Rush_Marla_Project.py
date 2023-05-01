import tkinter as tk
from tkinter import messagebox

class PizzaOrder:
    def __init__(self, master):
        self.master = master
        master.title("Chicago's Style Pizza Order Form")

        # Create input labels and entry boxes
        self.cheese_pizza_lbl = tk.Label(master, text="Cheese Pizza ($8.99)")
        self.cheese_pizza_ent = tk.Entry(master)
        self.chicken_pizza_lbl = tk.Label(master, text="Chicken Pizza ($8.99)")
        self.chicken_pizza_ent = tk.Entry(master)
        self.sausage_pizza_lbl = tk.Label(master, text="Sausage Pizza ($8.99)")
        self.sausage_pizza_ent = tk.Entry(master)
        self.mild_wings_lbl = tk.Label(master, text="Mild Wings ($9.99)")
        self.mild_wings_ent = tk.Entry(master)
        self.hot_wings_lbl = tk.Label(master, text="Hot Wings ($9.99)")
        self.hot_wings_ent = tk.Entry(master)
        self.BBQ_wings_lbl = tk.Label(master, text="BBQ Wings ($9.99)")
        self.BBQ_wings_ent = tk.Entry(master)

        # Create order button
        self.order_btn = tk.Button(master, text="Place Order", command=self.calculate_total)

        # Create exit button
        self.exit_btn = tk.Button(master, text="Exit", command=master.quit)

        # Pack labels, entry boxes and buttons to the form
        self.cheese_pizza_lbl.pack()
        self.cheese_pizza_ent.pack()
        self.chicken_pizza_lbl.pack()
        self.chicken_pizza_ent.pack()
        self.sausage_pizza_lbl.pack()
        self.sausage_pizza_ent.pack()
        self.mild_wings_lbl.pack()
        self.mild_wings_ent.pack()
        self.hot_wings_lbl.pack()
        self.hot_wings_ent.pack()
        self.BBQ_wings_lbl.pack()
        self.BBQ_wings_ent.pack()
        self.order_btn.pack()
        self.exit_btn.pack()

    def calculate_total(self):
        try:
            # Get input values and calculate total price
            cheese_pizza = int(self.cheese_pizza_ent.get())
            chicken_pizza = int(self.chicken_pizza_ent.get())
            sausage_pizza = int(self.sausage_pizza_ent.get())
            mild_wings = int(self.mild_wings_ent.get())
            hot_wings = int(self.hot_wings_ent.get())
            BBQ_wings = int(self.BBQ_wings_ent.get())

            total_price = (cheese_pizza + chicken_pizza + sausage_pizza) * 8.99 + \
                          (mild_wings + hot_wings + BBQ_wings) * 9.99
            total_price *= 1.07 # Add 7% sales tax

            # Display total price in a message box
            messagebox.showinfo("Total Price", f"Your total bill is ${total_price:.2f}")
        except ValueError:
            # Display error message if input is invalid
            messagebox.showerror("Invalid Input", "Please enter a valid integer for each item.")

# Create main window
root = tk.Tk()

# Create pizza order form
order_form = PizzaOrder(root)

# Run main loop
root.mainloop()
