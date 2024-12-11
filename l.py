def calculate_due_amount(total_bill, amount_paid):
    due = total_bill - amount_paid

    if due > 0:
        return "Due: $" + str(due)
    elif due < 0:
        return "Overpaid: $" + str(-due)
    else:
        return "Fully paid."

if __name__ == "__main__":
    total_bill = float(input("Total bill: "))
    amount_paid = float(input("Paid: "))
    print(calculate_due_amount(total_bill, amount_paid))
