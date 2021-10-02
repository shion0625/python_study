def menu_top():
    menu_char = input(
        "--------------------------------\n"
        "1. view detail of Coach\n"
        "2. view detail of Self-Record\n"
        "3. view Registered Sport Schedule only\n"
        "4. modify record \n"
        "5. Provide feedback and Star to Coach.\n"
        "6. exit\n"
        "please enter number: ")
    return menu_char


def menu_self():
    menu_char = input(
        "--------------------------------\n"
        "a. modify name\n"
        "b. modify gender\n"
        "c. modify old\n"
        "d. modify sports\n"
        "e. modify  address\n"
        "f. modify  phone number\n"
        "g. modify  e-mail\n"
        "h. exit\n"
        "please enter number: ")
    return menu_char
  
    
def display_detail_coach():
    coach_info_file = open("coach_info.txt", "r").readlines()
    for coach_info_data in coach_info_file:
        coach_info = coach_info_data.strip().split(":")
        print(f"name: \"{coach_info[1]}\" sports in charge: \"{coach_info[9]}\" sports center: \"{coach_info[7]}\" sports fee: \"{coach_info[4]}\" "
              f"rating"
              f": \"{coach_info[11]}\" phone number: \"{coach_info[5]}\"")


def display_detail_self(user_name):
    users_file = open("users.txt", "r").readlines()
    for user_line in users_file:
        user_data = user_line.split(":")
        if user_data[0] == user_name:
            print(f"\nusername: {user_data[0]}\nname: {user_data[2]}\ngender: {user_data[3]}\nold: {user_data[4]}\nsport: {user_data[5]}\naddress:"
                  f" {user_data[6]}\nphone "
                  f"number: {user_data[7]}\nemail: {user_data[8]}")
            break


def display_detail_schedule(user_name):
    users_file = open("users.txt", "r").readlines()
    sport = ""
    is_sport = False
    for user_line in users_file:
        user_data = user_line.split(":")
        if user_data[0] == user_name:
            sport = user_data[5]
            break
    if not sport == "":
        sports_file = open("sports.txt", "r").readlines()
        for sport_line in sports_file:
            sport_data = sport_line.split(":")
            if sport.strip() == sport_data[0].strip():
                print(sport_data[1])
                is_sport = True
        if not is_sport:
            print("this sport schedule didn't post")
    else:
        print("you didn't registered sport")


def modify_self_record(user_name):
    users_file = open("users.txt", "r")
    lines = users_file.readlines()
    users_file.close()
    users_file = open("users.txt", "w")
    user = " "
    for line in lines:
        line_array = line.split(":")
        if line_array[0].strip() != user_name.strip():
            users_file.write(f"{line.strip()}\n")
        elif line_array[0].strip() == user_name.strip():
            user = line.strip()
    user_array = user.split(":")
    section_modify_record_of = "y"
    while section_modify_record_of == "y":
        menu_char = menu_self()
        if menu_char == "a":
            user_array[2] = input("please enter name: ").strip()
        elif menu_char == "b":
            gender = input("please enter gender: ").strip()
            user_array[3] = gender
        elif menu_char == "c":
            old = input("please enter old: ").strip()
            user_array[4] = old
        elif menu_char == "d":
            sports = input("please enter sport: ").strip()
            user_array[5] = sports
        elif menu_char == "e":
            address = input("please enter address: ").strip()
            user_array[6] = address
        elif menu_char == "f":
            phone = input("please enter phone: ").strip()
            user_array[7] = phone
        elif menu_char == "g":
            email = input("please enter e-mail: ").strip()
            user_array[8] = email
        elif menu_char == "h":
            section_modify_record_of = "n"
            user = ":".join(user_array)
            users_file.write(f"{user.strip()}\n")
            users_file.close()
  
        
def provide_feedback_star():
    coach_name = input("please enter your coach: ").strip()
    score = int(input("please enter score: "))
    if 1 > score or score > 5:
        print("invalid number (1 <= score <= 5)")
    coach_info_file = open("coach_info.txt", "r")
    lines = coach_info_file.readlines()
    coach_info_file.close()
    coach_info_file = open("coach_info.txt", "w")
    coach = " "
    is_exist_coach = False
    for line in lines:
        line_array = line.split(":")
        if line_array[1].strip() != coach_name:
            coach_info_file.write(f"{line.strip()}\n")
        elif line_array[1].strip() == coach_name:
            coach = line.strip()
            is_exist_coach = True
    if not is_exist_coach:
        print("this coach isn't found")
    else:
        coach_array = coach.split(":")
        old_score = float(coach_array[11])
        voted_num = int(coach_array[12])
        new_score = (old_score * voted_num + score)/(voted_num+1)
        coach_array[11] = str(new_score)
        coach_array[12] = str(int(coach_array[12])+1)
        coach_array[11] = str(coach_array[11])
        coach_array[12] = str(coach_array[12])
        coach = ":".join(coach_array)
        coach_info_file.write(f"{coach.strip()}\n")
        score_array = coach_array[11].split(".")
        if int(score_array[1][0]) >= 5:
            score_array[0] = str(int(score_array[0])+1)
        print(score_array[0])
    coach_info_file.close()


def student_func(user_name):
    top_section = "y"
    while top_section == "y":
        menu_num = menu_top()
        if menu_num == '1':
            display_detail_coach()
        elif menu_num == '2':
            display_detail_self(user_name)
        elif menu_num == '3':
            display_detail_schedule(user_name)
        elif menu_num == '4':
            modify_self_record(user_name)
        elif menu_num == '5':
            provide_feedback_star()
        elif menu_num == '6':
            top_section = "n"
        else:
            print("not acceptable number")
