from utils import get_customer_input, calculate_total


def main():

    name, coffee, tea, sandwich = get_customer_input()

    
    total = calculate_total(coffee, tea, sandwich)

    
    print("\n===== RECEIPT =====")
    print(f"Customer : {name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("--------------------")
    print(f"Total = RM {total:.2f}")


if __name__ == "__main__":
    main()