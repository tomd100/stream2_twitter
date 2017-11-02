import json

def show_menu():
    print("1. Add a Person")
    print("2. View People")
    print("3. Stats")
    print("4. Clear File")
    print("5. Exit")
    
    option = input("Enter option: ")
    return option

def add_person(person_tags, questions, teams):
    
    person = {}
    
    print("Please enter the following information:")
    i = 0
    while i <= 3: 
    # for i, question in enumerate(questions):
        question = questions[i]
        answer = input(question + "> ")
        
        if i == 2:
            if not IsInt(answer):
                print("Please enter age as an integer:")
            else:
                person[person_tags[i]] = answer
                i += 1    
        elif i == 3: 
            answer = answer.lower()
            answer = answer.capitalize()
            print(answer)
            if not answer in teams:
                print("Please enter a team from the following: ", teams )
            else:
                person[person_tags[i]] = answer
                i += 1
        else:
            person[person_tags[i]] = answer
            i += 1
        
    with open("questions.txt", 'a') as outfile:
        person = json.dumps(person)
        outfile.write(person)
        outfile.write("\n")

def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def view_people(person_tags):

    i = 0
    with open("questions.txt", 'r') as infile:
        print("\n")
        print("List of people:")
        print("\n")
        print("First Name      Last Name       Age             Team")
        print("\n")
        
        for line in infile:
            person = json.loads(line)
            first_name = "{:<15}".format(person[person_tags[0]])
            last_name = "{:<15}".format(person[person_tags[1]])
            age = "{:<15}".format(person[person_tags[2]])
            team = "{:<15}".format(person[person_tags[3]])
            
            print(first_name, last_name, age, team)
            
def stats(person_tags, teams):

    i = 0
    
    with open("questions.txt", 'r') as infile:
        
        average_ages = {}
        
        for team in teams:
            average_ages[team]= {"age_total": 0, "num_people":0}
            
        for line in infile:
            person = json.loads(line)
            first_name = person[person_tags[0]]
            last_name = person[person_tags[1]]
            age = person[person_tags[2]]
            team = person[person_tags[3]]
            
            average_ages[team]["age_total"] += int(age) 
            average_ages[team]["num_people"] += 1
        
        print("\n")    
        for team in average_ages:
            num_people = average_ages[team]["num_people"]
            average_age = round(average_ages[team]["age_total"] / num_people, 2)
            print("In team {0} the average age is {1} from {2} people".format(team, average_age, num_people))
            
def clear_file():
    f = open("questions.txt", "+w")
    f.close()
    print("The file has been cleared")

def app_loop(person_tags, questions, teams):
    while True:
        option = show_menu()
        
        if option == "1":
            add_person(person_tags, questions, teams)
        elif option == "2":
            view_people(person_tags)
        elif option == "3":
            stats(person_tags, teams)
        elif option == "4":
            clear_file()
        elif option == "5":
            break
        else:
            print("Invalid Option")
        print("")

person_tags = ["FirstName","LastName", "Age","Team"]
questions = ["First name: ", "Last name: ", "Age: ", "Team Name: "]
teams = ["Red", "Blue", "Green", "Orange"]

app_loop(person_tags, questions, teams)

    
    