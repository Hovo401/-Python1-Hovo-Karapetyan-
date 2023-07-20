import random

def main():
    print("Welcome to the Story Generator!\n")
    print("Choose a template:")
    print("1. Hospital Adventure")
    print("2. Camping Adventure")
    print("3. Enchanted Forest Adventure")

    choice = input("Enter the number of the template you want to use: ")

    if choice == '1':
        story = generate_hospital_adventure()
    elif choice == '2':
        story = generate_camping_adventure()
    elif choice == '3':
        story = generate_enchanted_forest_adventure()
    else:
        print("Invalid choice. Please enter a valid number.")
        return

    print("\nYour Adventure Story:\n")
    print(story)


def generate_hospital_adventure():
    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    mode_of_transportation = input("Enter a mode of transportation: ")
    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun = input("Enter a noun: ")
    color = input("Enter a color: ")
    part_of_the_body = input("Enter a part of the body: ")
    verb = input("Enter a verb: ")
    number2 = input("Enter another number: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    verb2 = input("Enter a verb: ")
    adjective3 = input("Enter an adjective: ")
    silly_word = input("Enter a silly word: ")

    story = (
        f"It was about {number} {measure_of_time} ago when I arrived at the hospital in a {mode_of_transportation}. "
        f"The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. There are nurses here "
        f"who have {color} {part_of_the_body}. If someone wants to come into my room, I told them that they have to "
        f"{verb} first. I’ve decorated my room with {number2} {noun2}. Today I talked to a doctor and they were wearing "
        f"a {noun3} on their {part_of_the_body}. I heard that all doctors {verb2} {noun3} every day for breakfast. The "
        f"most {adjective3} thing about being in the hospital is the {silly_word} {noun}!"
    )

    return story


def generate_camping_adventure():
    name = input("Enter a person's name: ")
    noun = input("Enter a noun: ")
    adjective_feeling = input("Enter an adjective for how you feel: ")
    verb = input("Enter a verb: ")
    adjective_feeling2 = input("Enter another adjective for how you feel: ")
    animal = input("Enter an animal: ")
    verb2 = input("Enter a verb: ")
    color = input("Enter a color: ")
    verb_ing = input("Enter a verb ending in 'ing': ")
    adverb = input("Enter an adverb ending in 'ly': ")
    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    color_animal = input("Enter a color of an animal: ")
    noun2 = input("Enter another noun: ")
    silly_word = input("Enter a silly word: ")
    noun3 = input("Enter one more noun: ")

    story = (
        f"This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun}. "
        f"I am so {adjective_feeling} to {verb} in a tent. I am {adjective_feeling2} we might see a(n) {animal}, "
        f"I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}. "
        f"I have heard that the {color} lake is great for {verb_ing}. Then we will {adverb} hike through the forest "
        f"for {number} {measure_of_time}. If I see a {color_animal} {animal} while hiking, I am going to bring it "
        f"home as a pet! At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!"
    )

    return story


def generate_enchanted_forest_adventure():
    person_name = input("Enter a person's name: ")
    adjective = input("Enter an adjective: ")
    color = input("Enter a color: ")
    animal = input("Enter an animal: ")
    place = input("Enter a place: ")
    adjective2 = input("Enter an adjective: ")
    magical_creature_plural = input("Enter a plural magical creature: ")
    adjective3 = input("Enter another adjective: ")
    magical_creature_plural2 = input("Enter another plural magical creature: ")
    room_in_a_house = input("Enter a room in a house: ")
    noun = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun_plural3 = input("Enter a plural noun: ")
    adjective4 = input("Enter another adjective: ")
    noun_plural4 = input("Enter another plural noun: ")
    number = input("Enter a number: ")
    measure_of_time = input("Enter a measure of time: ")
    verb_ing = input("Enter a verb ending in 'ing': ")
    adjective5 = input("Enter an adjective: ")
    noun5 = input("Enter a noun: ")

    story = (
        f"Dear {person_name}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here "
        f"one day after going for a ride on a {color} {animal} in {place}. There are {adjective2} {magical_creature_plural} "
        f"and {adjective3} {magical_creature_plural2} here! In the {room_in_a_house} there is a pool full of {noun}. "
        f"I fall asleep each night on a {noun2} of {noun_plural3} and dream of {adjective4} {noun_plural4}. It feels as "
        f"though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the only way to "
        f"get here now is {verb_ing} on a {adjective5} {noun5}!!"
    )

    return story


if __name__ == "__main__":
    main()
