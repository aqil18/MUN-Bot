countries = ["🇦🇫", "🇦🇱", "🇦🇺", "🇧🇷", "🇨🇦", "🇨🇳", "🇪🇨","🇫🇷", "🇬🇦", "🇩🇪", "🇬🇭", "🇮🇳", "🇮🇩", "🇮🇪", "🇰🇪", "🇲🇽", "🇳🇴", "🇵🇸", "🇷🇺", "🇬🇧", "🇦🇪", "🇺🇸", "🇵🇱", "🇲🇱", "🇹🇩", "🇳🇱", "🇲🇦"]
sc = ["🇦🇱", "🇧🇷", "🇨🇳", "🇫🇷", "🇬🇦", "🇬🇭", "🇮🇳", "🇮🇪", "🇰🇪", "🇲🇽", "🇳🇴", "🇷🇺", "🇬🇧", "🇦🇪", "🇺🇸", "🇧🇪", "🇬🇾"]

countries_1 = print(countries[:14])
countries_2 = print(countries[14:])

msg = "!placards"
if msg.lower().count("!"):
    print(2)
print(len(sc))

committees = []
with open("final_server_roles.txt", "r") as f:
    for line in f:
        (key, value) = line.split()
        committees.append(key)
print(committees)
