"""
Title: Palindrome Word Checker
Description: Prompts the user for a word, normalizes it by stripping spaces and converting to lowercase, and checks whether it reads the same forwards and backwards.
"""

word = input("Koi word daalein: ").strip().lower()

if word == word[::-1]:
  print(f"'{word}' ek Palindrome hai!")
else:
  print(f"'{word}' Palindrome nahi hai.")