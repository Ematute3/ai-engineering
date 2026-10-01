# Week 1 — Exercise 8: Initials
# Goal: ask for a full name, print initials in uppercase.
# Example: "evan matute" -> "E.M."

full_name = input("enter your full name")
initials = "".join([name[0].upper() for name in full_name.split()])
print(".".join(initials) + ".")
