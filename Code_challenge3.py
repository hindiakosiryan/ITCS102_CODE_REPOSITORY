#assignmefnt

sender_name = input("Enter sender name: ")
item_type = input("Enter type of item: ")

is_fragile = bool(input("Is it fragile? (type anything for True, leave blank for False): "))
weight = float(input("Enter weight in kg: "))
distance = float(input("Enter distance in km: "))

is_express = bool(input("Is it express? (type anything for True, leave blank for False): "))
is_international = bool(input("Is it international? (type anything for True, leave blank for False): "))


# just showing what the booleans are
print("Fragile:", is_fragile)
print("Express:", is_express)
print("International:", is_international)


# calculate base cost
base_cost = (weight * 2.50) + (distance * 0.15)


# pricing
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
    total = 0.00
    shipping_type = "Free Shipping"

elif is_international and is_express:
    total = (base_cost * 1.40) + 50
    shipping_type = "International Express"

elif is_express or (is_international and weight > 20):
    total = (base_cost * 1.20) + 25
    shipping_type = "Express or Heavy International"

elif weight > 30 or distance > 1000:
    total = base_cost + 30
    shipping_type = "Oversized"

else:
    total = base_cost
    shipping_type = "Standard Rate"


print("\n--- Shipping Result ---")
print("Sender:", sender_name)
print("Item:", item_type)
print("Shipping Type:", shipping_type)
print("Total Shipping Cost: $" + format(total, ".2f"))

