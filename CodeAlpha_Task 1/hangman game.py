import random

# Step 1: Word list
words = ["apple", "python", "banana", "hangman", "orange","water","mecury"]

# Step 2: Pick a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)  # Placeholders
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Guess the word:", " ".join(guessed_word))

# Step 3: Game loop
while attempts > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("✅ Good guess!", " ".join(guessed_word))
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")
        print(" ".join(guessed_word))

# Step 4: Game result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)