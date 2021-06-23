import os
import matplotlib.pyplot as plt


#Main function - showing menu and starting procces
def main():
    another_action = 'Y'
    
    #check if room file already exists, else make one (first use at the program or second..) 
    try: 
    
        freerooms = open('freerooms.txt','r+')
    
    #file doesnt exists error    
    except IOError:
        freerooms = open('freerooms.txt','w')
        
        #create list of rooms by list function
        listofrooms = list(range(1,11))
       
        for n in listofrooms:
            
            freerooms.write(str(n)+'\n')        
        
    
    finally:
        freerooms.close()
    
    
    #While loop for making the procces run until the user ask to stop
    while another_action == 'Y' or another_action == 'y':	
        
        print("WELCOME TO DAN PANORAMA HOTEL - TEL AVIV\n")
        #Gets choice from user
        choose = input("Hello dear soldier, please choose one of The following options:\n\n 1.For guest reception - press 1\n 2.For guest release - press 2\n 3.For guest details - press 3\n 4.For changing room numbers - press 4\n 5.To watch rooms status by pie chart - press 5\n 6.To add an app password to an existing guest - press 6\n") 
        
        if choose == '1':
            another_action = Create_profile()
        
        elif choose == '2':
            another_action = guest_release()
        
        elif choose == '3':
            another_action = guests_details()
        
        elif choose == '4':
            another_action = changing_rooms()
        
        elif choose == '5':
            another_action = Pie_chart()
        
        elif choose == '6':
            another_action = add_password_to_files()
            
#Function gets guest data and save it to files
def Create_profile():
    try:
        
        titles_list = ['ID number', 'Firstname', 'Lastname', 'Hometown', 'Age', 'Gender', 'Phone_number', 'Arrival date', 'password']
        
        temp_guest_list = [int(input('ID number: ')),
                           input('first name: '),
                           input('Last name: '),
                           input('Hometown: '),
                           int(input('age: ')),
                           input('Male/Female - enter M or F: '),
                           int(input('Phone number: ')),
                           input('Arrival day:\nday ') + '/' + input('month ') + '/' + input('year ')]
                           
         
        
        
    #Make sure no invalid data    
    except ValueError:
        print('\nyou have entered invalid values, please be careful not to combine verbal and numeric values ​​and start again\n')
        Create_profile()
    #Open exists guest file or make new one
    guest_file = open('guestfile.txt','a')
    #Counter for the titles list
    count = 0
    #Coping the guest information from the list to the file
    for item in temp_guest_list:
        
        guest_file.write(titles_list[count] + '\n')
        guest_file.write(str(item) + '\n')
        count = count + 1 
    
    
    print('\nThe information was successfully saved to files')
    print('\nThe guest can now be accommodated in one of the available rooms of the hotel, please select the room number: ')
    
    #open the rooms file
    rooms_options = open('freerooms.txt','r')
    #readlines from the file
    file_contents = rooms_options.readlines()
    #close the file
    rooms_options.close()
    
    index = 0
    #loop copy the file lines back to list
    while index < len(file_contents):
        file_contents[index] = int(file_contents[index].rstrip('\n'))
        index += 1
    
    #print available room numbers for the guest
    for item in file_contents:
        print(item)
    
    
    #Gets the choose room number
    room = int(input())
    boolian = 'false'
    while boolian == 'false':
        try:
            #remove the number from the list
            file_contents.remove(room)
            boolian = 'true'
            
            
        except:
            boolian = 'false'
            print("the room number is not available, please enter another number: ") 
            room = int(input())
    
    #Write the guest choice in the file
    guest_file.write('room number:\n' + str(room) + '\n')
            
    
    rooms_options = open('freerooms.txt','w')
    for item in file_contents:
        rooms_options.write(str(item) + '\n')
    

    
    rooms_options.close()
    print("The choice has saved")
    
    
    guest_file.write('password\n' + vaild_password_function())
    guest_file.close()
    return more_action()

#Function find data in guest by id number, and delete it 
def guest_release():
    
    #Get the id number of the guest
    Id = input("please enter the guest ID number - ")
    
    #open the guests file
    guest_file = open('guestfile.txt','r')
    #readlines from the file
    file_contents = guest_file.readlines()
    #close the file
     
    
    index = 0
    while index < len(file_contents):
        
        file_contents[index] = file_contents[index].rstrip('\n')
        index += 1
   
    
    #determine if the id number is exists
    if Id in file_contents:
        #get the index of the id in the list
        id_index = file_contents.index(Id)
        
        #open the rooms file
        rooms_options = open('freerooms.txt','r')
        #readlines from the file
        roomslist = rooms_options.readlines()
        #close the file
        rooms_options.close()
        
        roomindex = 0
        #loop copy the file lines back to list
        
        while roomindex < len(roomslist):
            roomslist[roomindex] = int(roomslist[roomindex].rstrip('\n'))
            roomindex += 1
        
        #get the released guest room number for putting it back in the list
        roomnum = int(file_contents[id_index + 16])
        
        #update the available rooms list       
        roomslist.append(roomnum)

        #sort the list        
        roomslist.sort()
        

        #open rooms file and update it
        rooms_options = open('freerooms.txt','w')
        
        for item in roomslist:
            
            rooms_options.write(str(item) + '\n')
        
        rooms_options.close()
        
        end_index = int(id_index)
        
        try:
            
            while file_contents[end_index] != 'ID number' and end_index < len(file_contents):
               
                end_index = end_index + 1

        except IndexError:
            
            end_index = end_index + 1 
        
        
        #delete the released guest information        
        del file_contents [id_index - 1 : end_index]

        #open the guests file and update it
        guest_file = open('guestfile.txt','w')
        
        for item in file_contents:
            guest_file.write(item + '\n')
        
        guest_file.close()
        print("\nprocces done - the guest information has deleted\n")
    
    #case the id number wasn't found    
    else:
        print("\nthe ID number you entered was not found\n")    
  
    return more_action()   


def guests_details():
    
    try:
        #open the relevant file
        guest_file = open('guestfile.txt','r')
    
        guest_file_contents = guest_file.readlines()
    
        #close the file
        guest_file.close()
    
    #file doesnt exists error    
    except IOError:
        
        print('\nthe hotel is empty of guests\n')
        
        return more_action()
    
    
    index = 0
    
    while index < len(guest_file_contents):
        
        guest_file_contents[index] = (guest_file_contents[index].rstrip('\n'))
        index += 1
    
    
    
    
    #Gets the id number from the user
    id_number = input("\nfor guest information, please enter his/her id number\n\n")
    
    
    if id_number in guest_file_contents:
        #get the id number index in the list
        id_index = int(guest_file_contents.index(id_number))
        #get the end of person information index
        end_index = int(id_index)
        
        try:
            
            while guest_file_contents[end_index] != 'ID number' and end_index < len(guest_file_contents):
               
               end_index = end_index + 1

        except IndexError:
            
            end_index = end_index + 1        
        
        #slice the list to the relevant information
        person_information = guest_file_contents[id_index - 1 : end_index]
        #print the relevant information 
        print('\n')        
        for item in person_information:
            print(item)
        
        
    elif len(id_number) != 9:
        print("\nthe id number you enter is missing/over digits")
    
    else:
        print("Unfortunately the ID number was not found. the guest was not found at the hotel or released\n")

    return more_action()


def changing_rooms():
    
    try:
        #open the relevant file
        guest_file = open('guestfile.txt','r')
        rooms_file = open('freerooms.txt','r')
    
        guest_file_list = guest_file.readlines()
        rooms_file_list = rooms_file.readlines()
    
        #close the file
        guest_file.close()
        rooms_file.close()
        
    
    
    #file doesnt exists error    
    except IOError:
        
        print('\nthe hotel is empty of guests\n')
        
        return more_action()
    
    index = 0
    
    while index < len(guest_file_list):
        
        guest_file_list[index] = (guest_file_list[index].rstrip('\n'))
        index += 1
    
    index = 0
    
    while index < len(rooms_file_list):
        
        rooms_file_list[index] = int((rooms_file_list[index].rstrip('\n')))
        index += 1
    
    
    #get the id number of the guest that want to change a room
    guest_id = input("please enter the guest id number\n")            
    
    if guest_id in guest_file_list:
        
        #get the id number index in the list
        id_index = int(guest_file_list.index(guest_id))
        
        #go to index of room number 
        room_num_index = id_index
        
        while guest_file_list[room_num_index] != 'room number:':
            room_num_index = room_num_index + 1
        
        room_num_index = room_num_index + 1
        
        
        #get the room number the guest want to move to(from the available room list)        
        print('\n')
        for item in rooms_file_list:
            print(item)        
            
        choice = int(input("please enter the new room number the guest like to move\n" ))
        
        #remove the number from the list
        rooms_file_list.remove(choice)
        
         #add his room number to the available room list 
        rooms_file_list.append(int(guest_file_list[room_num_index]))
        
        #add choice to guest profile
        guest_file_list[room_num_index] = choice        
        
        #sort the list        
        rooms_file_list.sort()
        
        #open the guests file and update it
        guest_file = open('guestfile.txt','w')
        
        for item in guest_file_list:
            guest_file.write(str(item) + '\n')
        
        guest_file.close()
          
        #open the rooms file and update it
        rooms_file = open('freerooms.txt','w') 
        
        for item in rooms_file_list:
            rooms_file.write(str(item) + '\n')
            
        rooms_file.close() 
        
    elif len(guest_id) != 9:
        print("\nthe id number you enter is missing/over digits")
    
    else:
        print("Unfortunately the ID number was not found.\n")   
        
    return more_action()


def Pie_chart(): 
    
    try:
        #open the relevant file
        rooms_file = open('freerooms.txt','r')
       
        rooms_file_list = rooms_file.readlines()
        
        #close the file
        rooms_file.close()
        
    
    #file doesnt exists error    
    except IOError:
        
        print('\nthere is a problem with the file\n')
        
        return more_action()
   
    index = 0
    
    while index < len(rooms_file_list):
        
        rooms_file_list[index] = int((rooms_file_list[index].rstrip('\n')))
        index += 1
    
    #the hotel contain 10 rooms
    TOTAL_ROOMS = 10
    
    #get the number of rooms in use
    Occupied_rooms = TOTAL_ROOMS - len(rooms_file_list)
    
    #get the number of available rooms
    available_rooms = len(rooms_file_list)
    
    # Create a list of values
    values = (available_rooms, Occupied_rooms) 
    
    #Add a title.
    plt.title('available/taken rooms status')
    
    #Create a list of labels for the slices.
    slice_labels = ['available rooms: ' +  str(available_rooms), 'taken rooms: ' + str(Occupied_rooms)]
    
    #choosing colors
    colors = ('yellowgreen', 'lightcoral')
    
    #explode 1st slice
    explode = (0, 0.2)  
    
    #Create a pie chart from the values.
    plt.pie(values, labels = slice_labels, explode = explode, colors = colors, shadow = True, startangle = 340, autopct=('%1.1f%%'))
    
    plt.legend(slice_labels, loc = 3)
    
    #Display the pie chart
    plt.show()
    
    return more_action() 

#The function checks password validity
def vaild_password_function():
    #gets the password from the user
    password = input('In order to gain access and start using the guest app, a password is required.\n'
    'The password must contain at least 7 characters, at least one digit,\n'
    'and at least one capital letter. Please enter the password: \n')
    
    bool = 'false'
    #create a loop of inputs until the user choose a vaild password
    while bool == 'false':
        #check length of password
        if len(password) < 7:
            print("the password must contain at least 7 characters, please try again:")
            password = input()
        #check if there is any digit
        elif password.isalpha():
            print("the password must contain at least one digit, please try again:")
            password = input()
        #check if there is any letter
        elif password.isdigit():
            print("the password must contain at least one letter, please try again:")
            password = input()            
        #check if there is any capital letter
        elif password.islower():
            print("the password must contain at least one capital letter, please try again:")
            password = input()
        #check if there is any letters and digits at all    
        elif password.isspace():
            print("the password must contain at least one capital letter and one digit, please try again:")
            password = input()
        
        #password is good
        else:
            
            bool = 'true'
    
    return password
    

#function add password to existing guest
def add_password_to_files():
    
    #gets the id number of guest
    id_number = input("please enter the guest id number:\n")
    #check vaild id number
    while not id_number.isdigit():
        
        print("the id number must contain only digits!")
        id_number = input()
    
    
    #open the guests file
    guest_file = open('guestfile.txt','r')
    #readlines from the file
    guest_list = guest_file.readlines()
    #close the file
    guest_file.close()
    
    #convert file to a list
    index = 0
    while index < len(guest_list):
        
        guest_list[index] = guest_list[index].rstrip('\n')
        index += 1
   
    
    #determine if the id number is exists
    if id_number in guest_list:
        
        #get the index of the id in the list
        id_index = guest_list.index(id_number)
        
        #get the end of person information index
        end_index = int(id_index)
        
        try:
            
            while guest_list[end_index] != 'ID number' and end_index < len(guest_list):
               
               end_index = end_index + 1

        except IndexError:
            
            end_index = end_index + 1        
        
        if str(guest_list[end_index - 3]) == 'password':
            print("the guest already have a password\n" + guest_list[end_index - 2])         
            return more_action()
        
        
        #insert password to guest information
        guest_list.insert(end_index, 'password')
        guest_list.insert(end_index + 1, vaild_password_function())
        
        #open the guests file and update it
        guest_file = open('guestfile.txt','w')
        
        for item in guest_list:
            
            guest_file.write(item + '\n')
        
        guest_file.close()
        
        print("password has saved")
        return more_action()
    
    else:
        print("the id number has not found")
        return more_action()        


        
def more_action():
    print("\nwould you like to do another action? please enter Y for yes, or N for no")
    answer = input()
    return answer
                
main()