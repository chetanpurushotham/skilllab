role = "patient Python tutor"
topic = "for loops"
level = "beginner"
example_limit = 80

prompt = f"""
You are a {role}.
Explain {topic} for a {level}.
Give one example in at most {example_limit} words.
"""

print(prompt)