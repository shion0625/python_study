import admin_page
import students_page


def menu_top_page():
    menu_char = input(
        "--------------------------------\n"
        "1. login\n"
        "2. register\n"
        "3. view details of sport\n"
        "4. view details of sport schedule\n"
        "5. exit\n"
        "please enter number: ")
    return menu_char


def main():
    print("--------------------------------------")
    print("\\\\\\welcome to System\\\\\\")
    top_section = "y"
    while top_section == "y":
        menu_char = menu_top_page()
        if menu_char == "1":
            is_exists_user = False
            print("------------------------------------------")
            user_name = input("please enter user name: ").strip()
            user_password = input("please enter your password: ").strip()
            users_file = open("users.txt")
            for user_record in users_file:
                user_record = user_record.split(':')
                user_record_name = user_record[0].strip()
                user_record_password = user_record[1].strip()
                if user_name == user_record_name and user_name == "admin" and user_password == user_record_password:
                    print("**************************")
                    print(f"successful admin")
                    print("**************************")
                    is_exists_user = True
                    admin_page.admin_func()
                    break
                elif user_name == user_record_name and user_password == user_record_password:
                    print("*******************************")
                    print(f"welcome {user_record_name}")
                    print("*******************************")
                    is_exists_user = True
                    students_page.student_func(user_name)
                    break
            if not is_exists_user:
                print("*******************************")
                print("you can't join this System")
                print("*******************************")

        elif menu_char == "2":
            is_used = False
            new_register_name = input("please enter your name: ")
            users_file = open("users.txt", "r")
            count = 0
            for user in users_file:
                if user.split(":")[0] == new_register_name:
                    print("**************************")
                    print("this name is already used")
                    print("**************************")
                    is_used = True
                count += 1
            if not is_used:
                users_file.close()
                new_register_pass = input("please enter your password: ")
                users_file = open("users.txt", "a")
                users_file.write(f"{new_register_name}:{new_register_pass}:gender:old:sport:address:phone:e-mail:TP{count}s\n")
                users_file.close()
                print("**************************")
                print("totally accepted")
                print("**************************")
        elif menu_char == "3":
            sport_info_file = open("sports.txt", "r")
            print("*****************************")
            for sport_data in sport_info_file:
                print(sport_data.split(":")[0].strip())
            print("*****************************")
            sport_info_file.close()
            
        elif menu_char == "4":
            is_exists_schedule = False
            sport_info_file = open("sports.txt", "r")
            print("*****************************")
            for sport_data in sport_info_file:
                if sport_data.split(":")[1].strip() != "":
                    print(sport_data.strip())
                    is_exists_schedule = True
            if not is_exists_schedule:
                print("is not registered")
            print("*****************************")
            sport_info_file.close()
        elif menu_char == "5":
            top_section = "n"


main()
