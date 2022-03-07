"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# Solve for maximum heart rate
age = int(input("What is your age? "))
max_rate = 220-age

# Solve for exercising heart rate
low_rate = max_rate*(0.65)
high_rate = max_rate*(0.85)

# Display solution to user
print(f"When you exercise to strgthen your heart,\nyou should keep your heart rate between {low_rate :.0f} and {high_rate :.0f} beats per minute")