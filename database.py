from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine("sqlite:///sales.db", echo=True)
Base = declarative_base()


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    salesman_id = Column(Integer, ForeignKey("salesmen.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
    amount = Column(Integer)

    salesman = relationship("Salesmen", back_populates="sales")
    customer = relationship("Customers", back_populates="sales")


class Salesmen(Base):
    __tablename__ = "salesmen"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sales = relationship("Sales", back_populates="salesman")


class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sales = relationship("Sales", back_populates="customer")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def display_sales():
    sales = session.query(Sales).all()
    for sale in sales:
        print(f"ID: {sale.id}, Salesman: {sale.salesman.name}, Customer: {sale.customer.name}, Amount: {sale.amount}")


def display_max_sale():
    max_sale = session.query(Sales).order_by(Sales.amount.desc()).first()
    print(f"Max Sale: {max_sale.amount}")


def display_min_sale():
    min_sale = session.query(Sales).order_by(Sales.amount).first()
    print(f"Min Sale: {min_sale.amount}")


def display_max_sale_by_salesman():
    salesmen = session.query(Salesmen).all()
    for salesman in salesmen:
        max_sale = session.query(Sales).filter(Sales.salesman_id == salesman.id).order_by(Sales.amount.desc()).first()
        print(f"Max Sale by {salesman.name}: {max_sale.amount}")


def display_min_sale_by_salesman():
    salesmen = session.query(Salesmen).all()
    for salesman in salesmen:
        min_sale = session.query(Sales).filter(Sales.salesman_id == salesman.id).order_by(Sales.amount).first()
        print(f"Min Sale by {salesman.name}: {min_sale.amount}")


def display_max_sale_by_customer():
    customers = session.query(Customers).all()
    for customer in customers:
        max_sale = session.query(Sales).filter(Sales.customer_id == customer.id).order_by(Sales.amount.desc()).first()
        print(f"Max Sale by {customer.name}: {max_sale.amount}")


def display_min_sale_by_customer():
    customers = session.query(Customers).all()
    for customer in customers:
        min_sale = session.query(Sales).filter(Sales.customer_id == customer.id).order_by(Sales.amount).first()
        print(f"Min Sale by {customer.name}: {min_sale.amount}")


def display_salesman_max_sales():
    salesman_max_sales = session.query(Sales.salesman_id, Salesmen.name, Sales.amount).join(Salesmen).group_by(
        Sales.salesman_id).order_by(Sales.amount.desc()).first()
    print(f"Salesman with Maximum Sales: {salesman_max_sales[1]}, Maximum Sales: {salesman_max_sales[2]}")


def display_salesman_min_sales():
    salesman_min_sales = session.query(Sales.salesman_id, Salesmen.name, Sales.amount).join(Salesmen).group_by(
        Sales.salesman_id).order_by(Sales.amount).first()
    print(f"Salesman with Minimum Sales: {salesman_min_sales[1]}, Minimum Sales: {salesman_min_sales[2]}")


def display_customer_max_purchases():
    customer_max_purchases = session.query(Sales.customer_id, Customers.name, Sales.amount).join(Customers).group_by(
        Sales.customer_id).order_by(Sales.amount.desc()).first()
    print(
        f"Customer with Maximum Purchases: {customer_max_purchases[1]}, Maximum Purchase: {customer_max_purchases[2]}")


def calculate_average_purchase_for_customer():
    customer_id = int(input("Enter Customer ID: "))
    total_sales = session.query(Sales).filter(Sales.customer_id == customer_id).count()
    total_amount = session.query(Sales).filter(Sales.customer_id == customer_id).with_entities(Sales.amount).all()
    total_amount = sum([amount[0] for amount in total_amount])
    average_purchase = total_amount / total_sales
    print(f"Average Purchase for Customer ID {customer_id}: {average_purchase}")


def calculate_average_purchase_for_salesman():
    salesman_id = int(input("Enter Salesman ID: "))
    total_sales = session.query(Sales).filter(Sales.salesman_id == salesman_id).count()
    total_amount = session.query(Sales).filter(Sales.salesman_id == salesman_id).with_entities(Sales.amount).all()
    total_amount = sum([amount[0] for amount in total_amount])
    average_purchase = total_amount / total_sales
    print(f"Average Purchase for Salesman ID {salesman_id}: {average_purchase}")


def add_sale():
    salesman_id = int(input("Enter Salesman ID: "))
    customer_id = int(input("Enter Customer ID: "))
    amount = int(input("Enter Sale Amount: "))

    sale = Sales(salesman_id=salesman_id, customer_id=customer_id, amount=amount)
    session.add(sale)
    session.commit()
    print("Sale")


def update_sale():
    sale_id = int(input("Enter Sale ID: "))
    sale = session.query(Sales).get(sale_id)
    if sale:
        salesman_id = int(input("Enter new Salesman ID (0 to keep the same): "))
        customer_id = int(input("Enter new Customer ID (0 to keep the same): "))
        amount = int(input("Enter new Sale Amount (0 to keep the same): "))

        if salesman_id != 0:
            sale.salesman_id = salesman_id
        if customer_id != 0:
            sale.customer_id = customer_id
        if amount != 0:
            sale.amount = amount

        session.commit()
        print("Sale updated successfully.")
    else:
        print("Sale not found.")


def delete_sale():
    sale_id = int(input("Enter Sale ID: "))
    sale = session.query(Sales).get(sale_id)
    if sale:
        session.delete(sale)
        session.commit()
        print("Sale deleted successfully.")
    else:
        print("Sale not found.")


def save_sales_to_file():
    sales = session.query(Sales).all()
    with open("sales.txt", "w") as file:
        file.write("Sales data:\n")
        file.write("ID\tSalesman\tCustomer\tAmount\n")
        for sale in sales:
            file.write(f"{sale.id}\t{sale.salesman.name}\t{sale.customer.name}\t{sale.amount}\n")
    print("Sales data saved to file.")


def menu():
    while True:
        print("\n--------- MENU ---------")
        print("1. Display all sales")
        print("2. Display maximum sale")
        print("3. Display minimum sale")
        print("4. Display maximum sale by salesman")
        print("5. Display minimum sale by salesman")
        print("6. Display maximum sale by customer")
        print("7. Display minimum sale by customer")
        print("8. Display salesman with maximum sales")
        print("9. Display salesman with minimum sales")
        print("10. Display customer with maximum purchases")
        print("11. Calculate average purchase for a customer")
        print("12. Calculate average purchase for a salesman")
        print("13. Add a sale")
        print("14. Update a sale")
        print("15. Delete a sale")
        print("16. Save sales to a file")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_sales()
        elif choice == 2:
            display_max_sale()
        elif choice == 3:
            display_min_sale()
        elif choice == 4:
            display_max_sale_by_salesman()
        elif choice == 5:
            display_min_sale_by_salesman()
        elif choice == 6:
            display_max_sale_by_customer()
        elif choice == 7:
            display_min_sale_by_customer()
        elif choice == 8:
            display_salesman_max_sales()
        elif choice == 9:
            display_salesman_min_sales()
        elif choice == 10:
            display_customer_max_purchases()
        elif choice == 11:
            calculate_average_purchase_for_customer()
        elif choice == 12:
            calculate_average_purchase_for_salesman()
        elif choice == 13:
            add_sale()
        elif choice == 14:
            update_sale()
        elif choice == 15:
            delete_sale()
        elif choice == 16:
            save_sales_to_file()
        elif choice == 0:
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    menu()
