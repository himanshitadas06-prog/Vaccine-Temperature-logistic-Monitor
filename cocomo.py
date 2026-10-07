# Vaccine Temperature & Logistics + COCOMO

def cocomo():
    k = float(input("Enter KLOC: "))
    salary = float(input("Enter monthly salary: "))

    effort = 2.4 * k**1.05
    time = 2.5 * effort**0.38
    developers = effort / time
    cost = effort * salary

    print("\n--- COCOMO RESULT ---")
    print("Effort:", round(effort, 2), "Person-Months")
    print("Time:", round(time, 2), "Months")
    print("Developers:", round(developers, 2))
    print("Cost: Rs.", round(cost, 2))


def temperature():
    t = float(input("Enter temperature: "))

    print("\n--- TEMPERATURE ---")
    if 2 <= t <= 8:
        print("Status: SAFE")
        print("Temperature is NORMAL")
    else:
        print("Status: ALERT")
        print("Temperature is NOT SAFE")


def logistics():
    print("\n--- LOGISTICS ---")

    vaccine = input("Vaccine Name: ")
    source = input("Source: ")
    destination = input("Destination: ")

    print("\n1. In Transit")
    print("2. Delivered")
    print("3. Delayed")

    s = input("Enter status: ")

    if s == "1":
        status = "In Transit"
    elif s == "2":
        status = "Delivered"
    elif s == "3":
        status = "Delayed"
    else:
        status = "Unknown"

    print("\nVaccine:", vaccine)
    print("Source:", source)
    print("Destination:", destination)
    print("Status:", status)


while True:

    print("\n==============================")
    print(" VACCINE MONITORING SYSTEM")
    print("==============================")
    print("1. COCOMO Cost Estimation")
    print("2. Temperature Monitoring")
    print("3. Logistics Monitoring")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        cocomo()

    elif choice == "2":
        temperature()

    elif choice == "3":
        logistics()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
