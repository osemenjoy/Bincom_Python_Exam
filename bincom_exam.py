from collections import Counter
import psycopg2
import random

data = {
    "MONDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "TUESDAY": "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "WEDNESDAY": "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "THURSDAY": "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "FRIDAY": "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
}

# Get all the colors in a list
colors = []
for day in data.values():
    colors.extend(day.split(", "))

# count all the colors in the list
color_counts = Counter(colors)

# 1. mean color of shirt
color_frequencies = list(color_counts.values())
mean_frequency = sum(color_frequencies) / len(color_frequencies)
mean_color = min(color_counts.keys(), key=lambda color: abs(color_counts[color] - mean_frequency))
print(f"1. Mean color: {mean_color}")

# 2. Mode color
mode_color = max(color_counts, key=color_counts.get)
print(f"2. Mode color (most frequent): {mode_color}")

# 3. median Color
sorted_colors = sorted(color_counts.items(), key=lambda x: x[1])
median_color = sorted_colors[len(sorted_colors) // 2][0]
print(f"3. Median color: {median_color}")

# 4. Variance of colors (how much the counts vary)
variance = sum((x - mean_frequency) ** 2 for x in color_frequencies) / len(color_frequencies)
print(f"4. Variance: {variance}")

# 5. probability of getting red 
prob_red = color_counts.get("RED", 0) / sum(color_counts.values())
print(f"5. The probability of getting red is {prob_red}")

# 6. saving colors to database
def save_to_db():
    try:
        # fill in correct user credentials to connect postgres database 
        conn = psycopg2.connect(database="colors", user="postgres", password="password", host="localhost", port="5432")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Colors (color VARCHAR(50), frequency INT)")
        for color, freq in color_counts.items():
            cur.execute("INSERT INTO Colors (color, frequency) VALUES (%s, %s)", (color, freq))
        conn.commit()
        conn.close()
        print("6. Data saved to database successfully!")
    except Exception as e:
        print("6. Error saving to database:", e)

save_to_db()

# 8. generate 4 random numbers and convert to base 10
binary_number = "".join(str(random.randint(0, 1)) for i in range(4))
base_10 = int(binary_number, 2)
print(f"8. {binary_number}, converted to base 10 is {base_10}")

# 9. sum of the first 50 fibonacci series
def fibonacci_series(n):
    a = 0
    b = 1
    sum = 0
    for i in range(n):
        sum += a
        next = a + b
        a = b
        b = next
    return sum
fifty_fibonacci_series = fibonacci_series(50)
print(f"9. The sum of the first 50 fibonacci series is {fifty_fibonacci_series}")

