import random

def roll_stat():
    """Rolls 4d6, drops the lowest die, and sums the rest."""
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))  # Drop the lowest roll
    return sum(rolls)

def generate_stats():
    """Generates six ability scores for a D&D character."""
    return [roll_stat() for _ in range(6)]

def main():
    print("Rolling D&D stats (4d6, drop lowest)...")
    stats = generate_stats()
    print("Your stats:", stats)

if __name__ == "__main__":
    main()