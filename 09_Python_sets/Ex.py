# Movie sets
action = {"Don", "Pathaan", "Jawan", "Mad Max"}
comedy = {"Chennai Express", "Deadpool"}
scifi = {"Interstellar", "Matrix"}
romance = {"DDLJ", "Kal Ho Naa Ho"}

genres = {
    "action": action,
    "comedy": comedy,
    "scifi": scifi,
    "romance": romance
}

print("Available: action, comedy, scifi, romance")

# user input
user = input("Enter genres: ").lower().split(",")

# clean spaces
user = [g.strip() for g in user]

# valid sets list
sets = []

for g in user:
    if g in genres:
        sets.append(genres[g])
    else:
        print(f"⚠️ '{g}' not available.")

# no valid genre
if not sets:
    print("❌ No valid genre selected.")
    exit()

# union & intersection
recommend = set.union(*sets)
common = set.intersection(*sets) if len(sets) > 1 else set()

print("\n🎥 Recommended:", recommend)

if common:
    print("🔥 Popular:", common)
