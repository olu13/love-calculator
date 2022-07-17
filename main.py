# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()
no_of_t = name1_lower.count("t") + name2_lower.count("t")
no_of_r = name1_lower.count("r") + name2_lower.count("r")
no_of_u = name1_lower.count("u") + name2_lower.count("u")
no_of_e = name1_lower.count("e") + name2_lower.count("e")
no_of_l = name1_lower.count("l") + name2_lower.count("l")
no_of_o = name1_lower.count("o") + name2_lower.count("o")
no_of_v = name1_lower.count("v") + name2_lower.count("v")
no_of_e = name1_lower.count("e") + name2_lower.count("e")
total_1 = no_of_t + no_of_r + no_of_u + no_of_e
total_2 = no_of_l + no_of_o + no_of_v + no_of_e
love_score = str(total_1) + str(total_2)
final_love_score = int(love_score)


if final_love_score < 10 or final_love_score> 90:
  print(f"Your score is {final_love_score}, you go together like coke and mentos.")
elif final_love_score >= 40 and final_love_score <= 50:
  print(f"Your score is {final_love_score}, you are alright together.")
else:
  print(f"Your score is {final_love_score}.")
  
