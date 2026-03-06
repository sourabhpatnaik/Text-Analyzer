from text_analysis import get_text_data
from menu import print_menu,print_text_analysis

while True:
    print_menu()
    print()
    user_choice = int(input("Enter your choice (1-3): "))
    print()

    if user_choice == 1:
        text = get_text_data()
        print_text_analysis(text)
        print()

    elif user_choice == 2:
        texts = input("Enter Your Text Here: ")
        print()
        print_text_analysis(texts)
        print()

    elif user_choice == 3:
        break
        
