import customtkinter as ctk
from tkinter import messagebox
import os
import tempfile
import subprocess

# Appearance setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# === MAIN DASHBOARD WINDOW ===
app = ctk.CTk()
app.title("Payslip Generator Dashboard")
app.geometry("400x300")
app.after(100, lambda: app.state('zoomed'))

def open_payslip_window():
    app.destroy()  # Close the dashboard window

    # === PAYSLIP GENERATOR WINDOW ===
    payslip_window = ctk.CTk()
    payslip_window.title("Generate Payslip")
    payslip_window.geometry("800x600")
    payslip_window.after(100, lambda: payslip_window.state('zoomed'))

    # Grid layout frame
    frame = ctk.CTkFrame(payslip_window, fg_color="transparent")
    frame.pack(pady=20)
    
    def home():
        subprocess.Popen(["python", r"C:\Users\Jhon Harold\OneDrive\Documentos\PAYROLL\PROGRESS\BACKHOME.py"])
        payslip_window.destroy()

    # Labels and entries
    labels = [
        "Employee Name:", "Position:",
        "Days Worked:", "Hours/Day:",
        "Hourly Rate:", "Overtime Hours:",
        "SSS:", "PHILHEALTH:",
        "BIR:", "PAGIBIG:",
    ]

    entries = []

    for i in range(5):
        label1 = ctk.CTkLabel(frame, text=labels[i * 2])
        entry1 = ctk.CTkEntry(frame, width=200)
        label2 = ctk.CTkLabel(frame, text=labels[i * 2 + 1])
        entry2 = ctk.CTkEntry(frame, width=200)

        label1.grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry1.grid(row=i, column=1, padx=10, pady=5)
        label2.grid(row=i, column=2, padx=10, pady=5, sticky="e")
        entry2.grid(row=i, column=3, padx=10, pady=5)

        entries.extend([entry1, entry2])

    # Additional date fields: Date of Cut-Off and Pay Date
    cutoff_label = ctk.CTkLabel(frame, text="Date of Cut-Off:")
    cutoff_entry = ctk.CTkEntry(frame, width=200)
    paydate_label = ctk.CTkLabel(frame, text="Pay Date:")
    paydate_entry = ctk.CTkEntry(frame, width=200)

    cutoff_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
    cutoff_entry.grid(row=5, column=1, padx=10, pady=5)
    paydate_label.grid(row=5, column=2, padx=10, pady=5, sticky="e")
    paydate_entry.grid(row=5, column=3, padx=10, pady=5)

    entries.extend([cutoff_entry, paydate_entry])

    # Result Label
    result_label = ctk.CTkLabel(payslip_window, text="", justify="left", font=ctk.CTkFont(size=14))
    result_label.pack(pady=10)

    # Salary computation logic
    def compute_salary():
        try:
            name = entries[0].get().strip()
            position = entries[1].get().strip()
            days_worked = int(entries[2].get())
            hours_per_day = float(entries[3].get())
            hourly_rate = float(entries[4].get())
            overtime_hours = float(entries[5].get())

            # Salary calculations
            regular_pay = days_worked * hours_per_day * hourly_rate
            overtime_pay = overtime_hours * 91  # Fixed rate
            gross_salary = regular_pay + overtime_pay
            net_salary = gross_salary

            # Deduction computation
            def get_deduction(entry):
                val = entry.get().strip()
                if val.endswith("%"):
                    return (float(val.strip('%')) / 100) * net_salary
                return float(val) if val else 0.0

            sss = get_deduction(entries[6])
            philhealth = get_deduction(entries[7])
            bir = get_deduction(entries[8])
            pagibig = get_deduction(entries[9])
            cutoff_date = entries[10].get().strip()
            pay_date = entries[11].get().strip()

            total_deductions = sss + philhealth + bir + pagibig
            final_salary = net_salary - total_deductions

            payslip = f"""
            -------------------------- EMPLOYEE PAYSLIP --------------------------

            FUSIONLINK NETWORK AND DATA SOLUTIONS
            Date of Cut-Off: {cutoff_date}    |   Pay Date: {pay_date}

            Employee: {name}        |   Position: {position}
            Days Worked: {days_worked}     |   Hours/Day: {hours_per_day}
            Hourly Rate: ₱{hourly_rate:.2f}     |   Overtime Hours: {overtime_hours}
            Overtime Pay: ₱{overtime_pay:.2f}

            Regular Pay: ₱{regular_pay:.2f}
            Gross Salary: ₱{gross_salary:.2f}
            Total Deductions: ₱{total_deductions:.2f}

            Deductions:
            - SSS: ₱{sss:.2f}
            - PhilHealth: ₱{philhealth:.2f}
            - BIR: ₱{bir:.2f}
            - Pag-IBIG: ₱{pagibig:.2f}

            FINAL NET SALARY: ₱{final_salary:.2f}
            ---------------------------------------------------------------------
            """
            result_label.configure(text=payslip)

        except Exception:
            messagebox.showerror("Input Error", "Please ensure all numeric fields are properly filled.")

    # Print payslip logic
    def print_payslip():
        payslip_text = result_label.cget("text").strip()
        if not payslip_text:
            messagebox.showwarning("No Payslip", "Please generate the payslip first.")
            return

        try:
            with tempfile.NamedTemporaryFile("w", delete=False, suffix=".txt", encoding="utf-8") as temp:
                temp.write(payslip_text)
                temp_path = temp.name

            os.startfile(temp_path, "print")
            messagebox.showinfo("Print", "Payslip sent to printer.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to print payslip: {str(e)}")

    # Action buttons
    generate_btn = ctk.CTkButton(payslip_window, text="Generate Payslip", command=compute_salary)
    print_btn = ctk.CTkButton(payslip_window, text="Print Payslip", command=print_payslip)
    home_btn = ctk.CTkButton(payslip_window, text="Home", command=home)

    generate_btn.pack(pady=10)
    print_btn.pack(pady=5)
    home_btn.pack(pady=10)

    # Company logo text
    logo_label = ctk.CTkLabel(payslip_window, text="FUSIONLINK NETWORK AND DATA SOLUTIONS", text_color="skyblue", font=ctk.CTkFont(size=18, weight="bold"))
    logo_label.pack(pady=20)

    payslip_window.mainloop()

# Dashboard UI
dashboard_label = ctk.CTkLabel(app, text="FUSIONLINK PAYROLL SYSTEM", font=ctk.CTkFont(size=18, weight="bold"))
dashboard_label.pack(pady=30)

open_btn = ctk.CTkButton(app, text="Open Payslip Generator", command=open_payslip_window)
open_btn.pack(pady=10)

# Start dashboard
app.mainloop()
