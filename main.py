# subject: who / what
# action: e.g declares, rides, spotted etc.
# places/ objects : where / with whom or with what
# lets keep it bollywood
import random
subjects_list = ['SRK', 'Salman Khan', 'Kajol', 'Alia Bhatt', 'Katrina Kaif', 'Ranbir Kapoor', 'Vicky Kaushal', 'Kriti Sanon' ]
actions_list = ['spotted juggling NCERT books', 'dancing Tango blindfold', 'ate Chicken Noodle Soup with Soda on the side', 'wore Doraemon print shirt', 'riding Buffalo', 'crossed bridge on one leg']
places_list = ['at the India Gate', 'near the pollution control house', 'between a Cherry Blosson Tree and a Palas Tree', 'over the train', 'near Red Fort']

while True:
    subject = random.choice(subjects_list)
    action = random.choice(actions_list)
    place = random.choice(places_list)

    print(f"{subject} {action} {place}")
    user_input = input("Do you want another headline? (yes/no): ").strip().lower()
    if user_input == 'no':
        break
print("Thank you for using our Fake News Headline Generator. Bye!")