from ascii_art import vs
import my_function as mf


score = 0
keep_going = True
person_b = mf.new_person()

while keep_going:
    mf.refresh()
    if score > 0:
        print(f"You're right! Current score: {score}.")
    person_a = person_b
    person_b = mf.new_person()
    if person_b == person_a:
        person_b = mf.new_person()
    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")
    player_guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()
    keep_going = mf.check_answer(player_guess, person_a, person_b)
    if keep_going:
        score += 1

mf.refresh()
print(f"Sorry, that's wrong. Final score: {score}.")