import re

def criteria(password):
    criteria = {
        'length': len(password) >= 8,
        'uppercase': re.search(r'[A-Z]', password) is not None,
        'lowercase': re.search(r'[a-z]', password) is not None,
        'digit': re.search(r'\d', password) is not None,
        'special': re.search(r'[\W_]', password) is not None,
    }

    match_criteria = sum(criteria.values())

    if match_criteria == 5:
        complexity = 'Very Strong'
    elif match_criteria == 4:
        complexity = 'Strong'
    elif match_criteria == 3:
        complexity = 'Moderate'
    elif match_criteria == 2:
        complexity = 'Weak'
    else:
        complexity = 'Very Weak'

    return complexity, criteria

password = input("Enter a password: ")
complexity, criteria = criteria(password)

print(f"Password Complexity: {complexity}")
print("Criteria :")
for criterion, met in criteria.items():
    print(f"  {criterion.capitalize()}: {'Yes' if met else 'No'}")