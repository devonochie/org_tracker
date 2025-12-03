from migrations import run_migrations
from services.organization import create_organization, list_organization
from services.department import create_department, list_department_by_organization, list_department
from services.employee import create_employee


run_migrations()

def menu():
    print("\nOrganization Tracker")
    print("1. Add Organization")
    print("2. List Organizations")
    print("3. Add Department to Organization")
    print("4. List Departments by Organization")
    print("5. List Departments")
    print("6. Add Users")
    print("0. Exit")
    
  
while True:
    menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your organization name: ")
        country = input("Enter your country: ")
        create_organization(name, country)
        print("Companies name registered successfully")
    elif choice == "2":
        orgs = list_organization()
        for org in orgs:
            print(org["name"])
    elif choice == "3":
        orgs = list_organization()
        if not orgs:
            print("No organization is found")
        print("\nSelect Organization:")
        for org in orgs:
            print(f"{org["id"]}: {org["name"]}")   
        org_id = int(input("Select organization ID: "))
        dept_name = input("Select Department: ")
        create_department(org_id, dept_name)
        print("department created successfully")
    elif choice == "4":
        org_id = int(input("Input organization_id: "))
        deptartment = list_department_by_organization(org_id)
        if not deptartment: 
            print("No department exist")
        else:
            for dept in deptartment:
                print(dept)
    elif choice == "5":
        dept = list_department()
        for d in dept:
            print(d)
    elif choice == "6":
        deptartmentalList = list_department()
        if not deptartmentalList:
            print("No deptartmentalList  is found")
        print("\nSelect Deptartment :")
        for dept in deptartmentalList:
            print(f"{dept["id"]}: {dept["name"]}")
            
        dept_id = int(input("Select deptartment ID: "))
        user_name = input("Enter your name: ")
        user_email = input("Enter your email: ")
        create_employee(department_id=dept_id, name=user_name, email=user_email)
        print("Employee created successfully")
    elif choice == 0:
        break
    else:
        print("❌ Invalid choice")
        
        