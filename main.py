# from spy_details import spy_salutation,spy_age,spy_rating,spy_name
#
# question = "continue as " + spy_salutation + " " + spy_name + "Yes/No ?"
# existing = input("question_string")
#
# if existing == "Y":
#     #Proceed with Default user
#     #Start Chat Application Step 1
#     #Start Chat Application 2
#     #Start Chat Application 3
#     #Start Chat Application 4
# else:
#     #Input new user details
#     #Start Chat Application 1
#     #Start Chat Application 2
#     #Start Chat Application 3
#     #Start Chat Application 4
#     spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
#
#     if len(spy_name) > 0:
#
#         print ('Welcome ' + spy_name + '. Glad to have you back with us.')
#
#         spy_salutation = input("Should I call you Mister or Miss?: ")
#
#         spy_name = spy_salutation + " " + spy_name
#
#         print ("Alright " + spy_name + ". I'd like to know a little bit more about you before we proceed...")
#
#         spy_age = 0
#         spy_rating = 0.0
#         spy_is_online = False
#
#         spy_age = input("What is your age? : ")
#
#         spy_age = int(spy_age)
#
#         if spy_age > 12 and spy_age < 50:
#
#             spy_rating = input("What is your spy rating?")
#
#             if spy_rating > str(4.5):
#                 print ('Great ace!')
#             elif spy_rating > str(3.5) and spy_rating <= str(4.5):
#                 print ('You are one of the good ones.')
#             elif spy_rating >= str(2.5) and spy_rating <= str(3.5):
#                 print ('You can always do better')
#             else:
#                 print ('We can always use somebody to help in the office.')
#
#             spy_is_online = True
#
#             # This will not work, it will throw an error
#             print ("Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(
#             spy_rating) + " Proud to have you onboard")
#
#
#
#         else:
#             print ('Sorry you are not of the correct age to be a spy')
#
#
#     else:
#         print ("A spy needs to have a valid name. Try again please.")



def start_chat(spy_name,spy_age, spy_rating):
    menu_choices = "What do you want to do? \n 1. Add a status update\n 2. Exit"
    menu_choice = input(menu_choices)

    if menu_choice == 1:
        status = "what is your status ?"
        get_status = input(status)

        print (get_status)
    else:
        return False

while True:
    start_chat()
