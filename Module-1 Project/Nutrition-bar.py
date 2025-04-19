# What’s the data provided?

# 45g of raisins
# 65g of almonds
# 30g of apricots

# You need to create an ingredient percentage list using Python.

# That means:

# For each ingredient, find what percentage of the total weight it represents in the bar.


# Define a function that takes ingredients as parameter:

def percentage ( raisins, almonds, apricots):

    # To find percentage
    total_weight = raisins + almonds + apricots

    # raisins
    per_raisin = round(raisins / total_weight * 100, 2)

    # almonds
    per_almond = round(almonds / total_weight * 100, 2)

    # apricots
    per_apricot = round(apricots / total_weight * 100, 2)

    return {
        f"Raisins: {per_raisin}",
        f"Almonds: {per_almond}",
        f"Apricots: {per_apricot}"
    }

print(percentage(45, 65, 30))