gifts = [
    "Book", "Toy", "Gadget", "Video Game", "Headphones", 
    "Smartphone", "Laptop", "Watch", "Shoes", "Wallet", 
    "Headset", "Camera", "Drone", "Smart Watch", "Bluetooth Speaker"
]

print("Available Gifts:")
for i, gift in enumerate(gifts):
    print(f"{i}: {gift}")


selected_indices = input("Enter gift indices separated by commas (e.g., 0, 2): ")
selected_indices = [int(i) for i in selected_indices.split(",")]

# Calculate the unique gift code using bitwise OR
gift_code = 0
selected_gifts = []
for index in selected_indices:
    gift_code |= (1 << index)
    selected_gifts.append(gifts[index])

# Output the selected gifts and unique gift code
print("\nSelected Gifts:", ", ".join(selected_gifts))
print("Unique Gift Code:", gift_code)
