import inheritance

billy_cyrus = inheritance.Parent("Cyrus", "blue")

print(billy_cyrus.eye_color)

miley_cyrus = inheritance.Child("Cyrus", "Green", 5)
print(miley_cyrus.last_name)

billy_cyrus.show_info()

miley_cyrus.show_info() #because the show_info method exists in class Parent, it can also be called by class Child

