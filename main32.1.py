a = "Total 5 question all correct answer and won you 1cr rs."
print(a)
questions = [
    ["1 Apko kya banna hai?",
     ["Doctor", "Engineer", "Hijra", "Bussnes man"], "C", 5000],

    ["2 Aap kya ho?",
     ["Student", "Man", "Boy", "Chhaka"], "D", 10000],

    ["3 Tum kon se Categri me aate ho?",
     ["Marriage", "Raduwa", "Unmarrige", "Single"], "B", 50000],

    ["4 Aap din bhar kya karte hai?",
     ["Reelsscrol", "Kaam", "Ghumana", "Laundiya baji"], "D", 150000],

    ["5 Aap ka ladka ka kya naam hai?",
     ["Barmunda bur kumar", "Muthi lal dhakar", "Netaha", "Langra"], "D", 10000000]
]

money = 0

for q in questions:
    print("\n", q[0])

    print("A.", q[1][0])
    print("B.", q[1][1])
    print("C.", q[1][2])
    print("D.", q[1][3])

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q[2]:
        money = q[3]
        print("Correct Answer!")
        print("You won Rs.", money)
    else:
        print("Wrong Answer!")
        print("Correct answer is:", q[2])
        break

print("\nGame Over!")
print("Your final take-home amount is Rs.", money)