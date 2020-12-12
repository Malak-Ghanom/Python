# Ask the user for a lowercase string (s) as input.
# Create a function called check_palindrome(s) which returns the longest substring which is palindrome.

# Input: "I love python.nohtyp evol I Python is never odd or even"
# Return: "never odd or even"

lines = "I love python.nohtyp evol I Python is never odd or even"
# lines=lines.replace(" ","")
print(lines)
length = len(lines)
a = [lines[i:j+1] for i in range(length) for j in range(i, length)]
print(a)
total = []
for string in a:
    list(string).reverse()
    reverse_String = "".join(string)

    if reverse_String == string.lower():
      total.append(reverse_String)
print(max(total))