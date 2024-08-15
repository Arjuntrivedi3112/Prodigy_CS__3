import re

def assess_password_strength(password):
    # Criteria for password strength
    criteria = {
        "length": len(password) >= 8,
        "lowercase": bool(re.search(r'[a-z]', password)),
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "number": bool(re.search(r'[0-9]', password)),
        "special_char": bool(re.search(r'[\W_]', password))
    }

    # Count how many criteria are met
    criteria_met = sum(criteria.values())

    # Determine password strength
    strength_levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    strength_index = min(criteria_met, len(strength_levels) - 1)
    strength = strength_levels[strength_index]

    # Feedback on which criteria are not met
    feedback = []
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["lowercase"]:
        feedback.append("Password should include at least one lowercase letter.")
    if not criteria["uppercase"]:
        feedback.append("Password should include at least one uppercase letter.")
    if not criteria["number"]:
        feedback.append("Password should include at least one number.")
    if not criteria["special_char"]:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

# Loop to continuously check password strength until it's "Strong" or "Very Strong"
while True:
    password = input("Enter your password: ")
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    if strength == "Strong" or strength == "Very Strong":
        print("Your password meets the criteria.")
        print(f"Your password is: {password}")
        break
    else:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")
        print("Please try again.")
