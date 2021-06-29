name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format("Rolf")
with_name_two = greeting.format("Bob")


print(with_name)
print(with_name_two)

##Another Example.

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)