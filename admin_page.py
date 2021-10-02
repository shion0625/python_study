def menu_top():
    menu_char = input(
        "--------------------------------\n"
        "1. add\n"
        "2. display\n"
        "3. search\n"
        "4. sort\n"
        "5. modify\n"
        "6. exit\n"
        "please enter number: ")
    return menu_char


def menu_add_records():
    menu_char = input(
        "--------------------------------\n"
        "a. coach\n"
        "b. sport\n"
        "c. sport schedule\n"
        "d. exit\n"
        "please enter character: ")
    return menu_char


def menu_display_all():
    menu_char = input(
        "--------------------------------\n"
        "a. coach\n"
        "b. sport\n"
        "c. registered student\n"
        "d. exit\n"
        "please enter character: ")
    return menu_char


def menu_search():
    menu_char = input(
        "----------------------------------------------\n"
        "a. coach by coach ID\n"
        "b. coach by overall performance(Rating)\n"
        "c. sport by sport ID\n"
        "d. student by student ID\n"
        "e. exit\n"
        "please enter character: ")
    return menu_char


def menu_sort_display():
    menu_char = input(
        "-----------------------------------------------------\n"
        "a. Coaches in ascending order by names.\n"
        "b. Coaches Hourly Pay Rate in ascending order\n"
        "c. Coaches Overall Performance in ascending order\n"
        "e. exit\n"
        "please enter character: ")
    return menu_char


def menu_modify():
    menu_char = input(
        "--------------------------------------\n"
        "a. modify records of Coach: \n"
        "b. modify records of sport: \n"
        "c. modify records of sport schedule: \n"
        "e. exit\n"
        "please enter character: ")
    return menu_char


def modify_menu():
    menu_char = input(
        "----------------------------------------------------------\n"
        "a. do you want to changes coach's name: \n"
        "b. do you want to changes coach's date Terminated: \n"
        "c. do you want to changes coach's hourly wage: \n"
        "d. do you want to changes coach's telephone number: \n"
        "e. do you want to changes coach's address: \n"
        "f. do you want to changes sports center code: \n"
        "g. do you want to changes sports center name: \n"
        "h. do you want to changes sports code: \n"
        "i.do you want to changes coach's sports: \n"
        "j. exit\n"
        "please enter character: ")
    return menu_char


def fun_section_exit():
    section = "n"
    return section


def fun_list_len(array):
    count = 0
    for _ in array:
        count += 1
    return count


def fun_set(array):
    unique = []
    for x in array:
        if not x in unique:
            unique.append(x)
    return unique


def fun_sort(num, max_char):
    array = []
    coach_info_file = open("coach_info.txt", "r")
    coach_info_array = coach_info_file.readlines()
    coach_info_file.close()
    for info in coach_info_array:
        array.append(info.strip().split(":")[num])
    length = fun_list_len(array)
    array.append(max_char)
    if num == 4:
        array = fun_set(array)
        length = fun_list_len(array) - 1
        array = [int(n) for n in array]
    if num == 11:
        array = fun_set(array)
        length = fun_list_len(array) - 1
        array = [float(n) for n in array]
    i = 0
    while i < length:
        j = 1
        while j < length - i:
            if array[i] > array[i + j]:
                array[length] = array[i]
                array[i] = array[i + j]
                array[i + j] = array[length]
                array[length] = max_char
                j = j + 1
            else:
                j = j + 1
        i = i + 1
    array.remove(max_char)
    array = [str(n) for n in array]
    i = 0
    coach_info_file = open("coach_info.txt", "w")
    while i < length:
        for coach_data in coach_info_array:
            if array[i].strip() == coach_data.split(":")[num].strip():
                print(f"{coach_data.strip()}")
                coach_info_file.write(f"{coach_data.strip()}\n")
        i += 1
    coach_info_file.close()
    return


def add_records_of():
    add_records_section = "y"
    while add_records_section == "y":
        menu_char = menu_add_records()
        if menu_char == "a":
            coach_id = input("please enter coach's ID: ").strip()
            coach_name = input("please enter coach's name: ").strip()
            coach_start = input("please enter coach's date Joined: ").strip()
            coach_end = input("please enter coach's date Terminated: ").strip()
            coach_wage = input("please enter coach's hourly wage: ").strip()
            coach_tell = input("please enter coach's telephone number: ").strip()
            coach_address = input("please enter coach's address: ").strip()
            coach_center_code = input("please enter sports center code: ").strip()
            coach_center_name = input("please enter sports center name: ").strip()
            coach_sport_code = input("please enter sports code: ").strip()
            coach_sport_name = input("please enter coach's sports: ").strip()
            coach_info_file = open("coach_info.txt", "a")
            coach_info_file.write(
                f"{coach_id}:{coach_name}:{coach_start}:{coach_end}:{coach_wage}:{coach_tell}:{coach_address}:{coach_center_code}:"
                f"{coach_center_name}:{coach_sport_code}:{coach_sport_name}:0.0:0")
            coach_info_file.close()
        
        elif menu_char == "b":
            is_not_sports_exist = True
            sport_input = input("please enter sports in center: ").strip()
            sports_file = open("sports.txt", "r")
            print("*************************************")
            for sport in sports_file:
                if sport.split(":")[0].strip() == sport_input:
                    print("this is already exist")
                    is_not_sports_exist = False
                    break
            sports_file.close()
            print("*************************************")
            if is_not_sports_exist:
                sports_file = open("sports.txt", "a")
                sports_file.write(f"{sport_input}:\n")
                sports_file.close()
                print("*************************************")
                print(f"{sport_input} is added")
                print("*************************************")
        
        elif menu_char == "c":
            sport_schedules = []
            is_not_exist_sport = True
            sport_name = input("what's sport do you want to add schedule: ")
            sports_file = open("sports.txt", "r")
            for sport in sports_file:
                if sport.split(":")[0].strip() == sport_name:
                    is_not_exist_sport = False
            if is_not_exist_sport:
                print("*************************************")
                print("this sport isn't registered")
                print("*************************************")
            else:
                sports_file.close()
                sports_file = open("sports.txt", "r")
                lines = sports_file.readlines()
                sports_file.close()
                sports_file = open("sports.txt", "w")
                for line in lines:
                    if line.split(":")[0].strip() != sport_name:
                        sports_file.write(f"{line.strip()}\n")
                day_of_week = int(input("how many day of week do you want to put: "))
                print(f"I'll take {day_of_week} times")
                while 0 < day_of_week:
                    sport_schedule = input(f"please enter {sport_name}'s date: ")
                    print(f"added {sport_schedule} into {sport_name}")
                    sport_schedules.append(sport_schedule)
                    day_of_week -= 1
                sports_file.write(f"{sport_name}:{sport_schedules}\n")
                sports_file.close()
                print(f"{sport_name}:{sport_schedules} is added")
        elif menu_char == "d":
            add_records_section = fun_section_exit()


def display_all_records_of():
    display_all_section = "y"
    while display_all_section == "y":
        menu_char = menu_display_all()
        if menu_char == "a":
            coach_info_file = open("coach_info.txt", "r")
            for coach_info_data in coach_info_file:
                print(coach_info_data.strip())
            coach_info_file.close()
        elif menu_char == "b":
            sport_info_file = open("sports.txt", "r")
            for sport_info_data in sport_info_file:
                print(sport_info_data.strip())
            sport_info_file.close()
        elif menu_char == "c":
            users_file = open("users.txt", "r")
            lines = users_file.readlines()
            users_file.close()
            for line in lines:
                if line.split(":")[0].strip() != "admin":
                    print(line.split(":")[0].strip())
        elif menu_char == "d":
            display_all_section = fun_section_exit()
        else:
            print("this character is not acceptable")


def search_specific():
    search_section = "y"
    while search_section == "y":
        menu_char = menu_search()
        if menu_char == "a":
            id_is_not_exist = True
            coach_id_input = input("please enter coach ID: ")
            coach_info_file = open("coach_info.txt", "r")
            for coach_data in coach_info_file:
                if coach_data.split(":")[0].strip() == coach_id_input:
                    id_is_not_exist = False
                    print(f"{coach_data.strip()}")
                    break
            if id_is_not_exist:
                print(f"{coach_id_input} is not found")
        elif menu_char == "b":
            is_exist_coach = False
            input_rate = input("please enter search rating: ")
            coach_info_file = open("coach_info.txt", "r").readlines()
            for coach_data in coach_info_file:
                now_rate = coach_data.split(":")[11]
                now_rate = now_rate.split(".")
                decimal = now_rate[1]
                if int(decimal[0]) >= 5:
                    now_rate[0] = str(int(now_rate[0]) + 1)
                if now_rate[0].strip() == input_rate:
                    print(coach_data.strip())
                    is_exist_coach = True
            if not is_exist_coach:
                print("not exist")
            print("finish")
        elif menu_char == "c":
            code_is_not_exist = True
            sport_code_input = input("please enter sport code: ")
            coach_info_file = open("coach_info.txt", "r")
            for coach_data in coach_info_file:
                if coach_data.split(":")[9].strip() == sport_code_input:
                    code_is_not_exist = False
                    print(f"{coach_data.split(':')[10].strip()}")
                    break
            if code_is_not_exist:
                print(f"{sport_code_input} is not found")
        elif menu_char == "d":
            is_not_exist = True
            student_id_input = input("please enter student ID: ")
            users_file = open("users.txt", "r").readlines()
            for user_data in users_file:
                if user_data.split(":")[8].strip() == student_id_input:
                    is_not_exist = False
                    print(f"{user_data.strip()}")
                    break
            if is_not_exist:
                print(f"{student_id_input} is not found")
        elif menu_char == "e":
            search_section = fun_section_exit()
        else:
            print("this is not acceptable")


def sort_and_display_record_of():
    section_sort_and_display = "y"
    while section_sort_and_display == "y":
        menu_char = menu_sort_display()
        if menu_char == "a":
            fun_sort(1, "zzzzzzzzzzzzzzzzzzz")
            print("finish")
        elif menu_char == "b":
            fun_sort(4, 999999999)
            print("finish")
        elif menu_char == "c":
            fun_sort(11, 999999999)
            print("finish")
        elif menu_char == "e":
            section_sort_and_display = fun_section_exit()
        else:
            print("this is not acceptable")


def modify_record_of():
    section_modify_record_of = "y"
    while section_modify_record_of == "y":
        menu_char = menu_modify()
        if menu_char == "a":
            is_not_exist_coach = True
            coach_id = input("please enter coach's ID: ").strip()
            coach_info_file = open("coach_info.txt", "r")
            for coach_info in coach_info_file:
                if coach_info.split(":")[0].strip() == coach_id:
                    is_not_exist_coach = False
            if is_not_exist_coach:
                print("this coach' ID isn't registered")
            else:
                coach_info_file.close()
                coach_info_file = open("coach_info.txt", "r")
                lines = coach_info_file.readlines()
                coach_info_file.close()
                coach_info_file = open("coach_info.txt", "w")
                coach = " "
                for line in lines:
                    if line.split(":")[0].strip() != coach_id:
                        coach_info_file.write(f"{line.strip()}\n")
                    elif line.split(":")[0].strip() == coach_id:
                        coach = line.strip()
                coach_array = coach.split(":")
                section_modify_loop = "y"
                while section_modify_loop == "y":
                    modify_menu_char = modify_menu()
                    if modify_menu_char == "a":
                        coach_name = input("please enter coach's name: ")
                        coach_array[1] = coach_name
                    elif modify_menu_char == "b":
                        coach_fin = input("please enter coach's date Terminated mm/dd: ")
                        coach_array[3] = coach_fin
                    elif modify_menu_char == "c":
                        coach_wage = input("please enter coach's hourly wage: ")
                        coach_array[4] = coach_wage
                    elif modify_menu_char == "d":
                        coach_tel = input("please enter coach's telephone number: ")
                        coach_array[5] = coach_tel
                    elif modify_menu_char == "e":
                        coach_address = input("please enter coach's address: ")
                        coach_array[6] = coach_address
                    elif modify_menu_char == "f":
                        coach_center_code = input("please enter sports center code: ")
                        coach_array[7] = coach_center_code
                    elif modify_menu_char == "g":
                        coach_center_name = input("please enter sports center name: ")
                        coach_array[8] = coach_center_name
                    elif modify_menu_char == "h":
                        coach_code = input("please enter coach's sports code: ")
                        coach_array[9] = coach_code
                    elif modify_menu_char == "i":
                        coach_sports = input("please enter coach's sports: ")
                        coach_array[10] = coach_sports
                    elif modify_menu_char == "j":
                        section_modify_loop = fun_section_exit()
                        coach = ":".join(coach_array)
                        coach_info_file.write(f"{coach.strip()}\n")
                        coach_info_file.close()
            print("finish")
        elif menu_char == "b":
            is_not_exist_sport = True
            sport_input = input("please enter sport name: ").strip()
            sport_file = open("sports.txt", "r")
            for sport_info in sport_file:
                if sport_info.split(":")[0].strip() == sport_input:
                    is_not_exist_sport = False
                    print(sport_info)
            if is_not_exist_sport:
                print("this sport name isn't registered")
            else:
                sport_file.close()
                sport_menu = input("a. modify\nb. delete\nplease enter character: ")
                sport_file = open("sports.txt", "r")
                lines = sport_file.readlines()
                sport_file.close()
                if sport_menu == "a":
                    new_sport_input = input("please enter new sport name: ").strip()
                    sport_file = open("sports.txt", "w")
                    for line in lines:
                        if line.split(":")[0].strip() != sport_input:
                            sport_file.write(f"{line.strip()}\n")
                        elif line.split(":")[0].strip() == sport_input:
                            sport_file.write(f"{new_sport_input}:{line.split(':')[1]}")
                    sport_file.close()
                elif sport_menu == "b":
                    sport_file = open("sports.txt", "w")
                    for line in lines:
                        if line.split(":")[0].strip() != sport_input:
                            sport_file.write(f"{line.strip()}\n")
                    sport_file.close()
            print("finish")
        elif menu_char == "c":
            is_not_exist_sport = True
            sport_input = input("please enter sport name: ").strip()
            sport_file = open("sports.txt", "r")
            for sport_info in sport_file:
                if sport_info.split(":")[0].strip() == sport_input and sport_info.split(":")[1].strip() != "":
                    is_not_exist_sport = False
                    print(sport_info)
            if is_not_exist_sport:
                print("this sport name or schedule isn't registered")
            else:
                sport_file.close()
                sport_menu = input("a. modify\nb. delete\nplease enter character: ")
                sport_file = open("sports.txt", "r")
                lines = sport_file.readlines()
                sport_file.close()
                if sport_menu == "a":
                    new_schedule_input = []
                    new_num_input = int(input("how many enter sport schedules: "))
                    i = 0
                    while i < new_num_input:
                        input_schedule = input(f"please enter new {i + 1}. sport schedule: ")
                        new_schedule_input.append(input_schedule)
                        i += 1
                    print(new_schedule_input)
                    sport_file = open("sports.txt", "w")
                    for line in lines:
                        if line.split(":")[0].strip() != sport_input:
                            sport_file.write(f"{line.strip()}\n")
                        elif line.split(":")[0].strip() == sport_input:
                            print(True)
                            sport_file.write(f"{line.split(':')[0]}:{new_schedule_input}\n")
                    sport_file.close()
                elif sport_menu == "b":
                    sport_file = open("sports.txt", "w")
                    for line in lines:
                        if line.split(":")[0].strip() != sport_input:
                            sport_file.write(f"{line.strip()}\n")
                    sport_file.write(f"{sport_input}:\n")
                    sport_file.close()
            print("finish")
        elif menu_char == "e":
            section_modify_record_of = fun_section_exit()


def admin_func():
    top_section = "y"
    while top_section == "y":
        menu_num = menu_top()
        if menu_num == '1':
            add_records_of()
        elif menu_num == '2':
            display_all_records_of()
        elif menu_num == '3':
            search_specific()
        elif menu_num == '4':
            sort_and_display_record_of()
        elif menu_num == '5':
            modify_record_of()
        elif menu_num == '6':
            top_section = fun_section_exit()
        else:
            print("not acceptable number")
