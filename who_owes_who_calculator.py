def main():
    # my girlfriend and I are still separate in terms of finances, so this is a small "cute" 
    # script to help us figure out who owes who when we balance our purchases that 
    # involve each other.
    print("Welcome to the Who Owes Who Calculator!")
    print("-----------------------------------------`")
    # person 1's information
    person1_name = input("Enter the name of person 1: ")
    num_purchases_p1 = int(input(f"How many purchases did {person1_name} make? "))
    
    person1_purchases = []
    for i in range(num_purchases_p1):
        purchase = float(input(f"Enter purchase {i+1} amount for {person1_name}: $"))
        person1_purchases.append(purchase)
    
    # person 2's information
    person2_name = input("\nEnter the name of person 2: ")
    num_purchases_p2 = int(input(f"How many purchases did {person2_name} make? "))
    
    person2_purchases = []
    for i in range(num_purchases_p2):
        purchase = float(input(f"Enter purchase {i+1} amount for {person2_name}: $"))
        person2_purchases.append(purchase)
    
    #  sums
    person1_total = sum(person1_purchases)
    person2_total = sum(person2_purchases)
    
    # Display totals
    print(f"\n{person1_name} spent: ${person1_total:.2f}")
    print(f"{person2_name} spent: ${person2_total:.2f}")
    
    # who owes who?
    difference = abs(person1_total - person2_total)
    
    if person1_total > person2_total:
        print(f"\n{person2_name} owes {person1_name} ${difference:.2f}")
    elif person2_total > person1_total:
        print(f"\n{person1_name} owes {person2_name} ${difference:.2f}")
    else:
        print(f"\n{person1_name} and {person2_name} are even! No one owes anything.")

if __name__ == "__main__":
    main()

