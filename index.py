phone_input = input("Enter a U.S. phone number (any format): ")

cleaned = phone_input.strip()

for ch in ["-", "(", ")", "."]:
    cleaned = cleaned.replace(ch, " ")
    
parts = cleaned.split()
digits_only = "".join(parts)

if len(digits_only) == 10:
    area = digits_only[0:3]
    mid = digits_only[3:6]
    end = digits_only[6:]
    print(f"Formatted number: ({area}) {mid}-{end}")
else:
    print("Error: Please enter exactly 10 digits.")
