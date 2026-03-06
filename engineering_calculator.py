from openpyxl import Workbook

results = []

while True:

    print("\n===== ENGINEERING CALCULATOR =====")
    print("1 - Calculate Stress")
    print("2 - Calculate Strain")
    print("3 - Calculate Young's Modulus")
    print("4 - Exit\n")

    choice = input("Select option: ")

    # Calculate Stress
    if choice == "1":

        force = float(input("Enter Force (N): "))
        area = float(input("Enter Area (m^2): "))

        stress = force / area

        print("Stress =", stress, "Pa")

        results.append(["Stress", force, area, stress])

    # Calculate Strain
    elif choice == "2":

        deltaL = float(input("Enter change in length ΔL (m): "))
        originalL = float(input("Enter original length L0 (m): "))

        strain = deltaL / originalL

        print("Strain =", strain)

        results.append(["Strain", deltaL, originalL, strain])

    # Calculate Young's Modulus
    elif choice == "3":

        stress = float(input("Enter Stress (Pa): "))
        strain = float(input("Enter Strain: "))

        young = stress / strain

        print("Young's Modulus =", young, "Pa")

        results.append(["Young Modulus", stress, strain, young])

    elif choice == "4":
        break

    else:
        print("Invalid option")

# Show all results
print("\n===== FINAL RESULTS =====")

for r in results:
    print(r)

# Export results to Excel
wb = Workbook()
ws = wb.active
ws.title = "Engineering Results"

ws.append(["Type", "Value 1", "Value 2", "Result"])

for r in results:
    ws.append(r)

wb.save("engineering_results.xlsx")

print("\nExcel file created: engineering_results.xlsx")