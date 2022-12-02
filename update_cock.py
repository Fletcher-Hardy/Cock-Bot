from replit import db

def update_cock(person):
  if person == "squid":
    db["squid"] += 1
  elif person == "landri":
    db["landri"] += 1
  elif person == "floochoo":
    db["floochoo"] += 1
  else:
    print("Invalid Member")
    
print(db.keys())
print(db["squid"])
print(db["landri"])
print(db["floochoo"])
