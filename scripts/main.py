"""
EmptyProject

Author: Danil Aksenow (@denhateu)
Version: 0.0.0-alpha
"""

from emptyproject import EmptyProject
from functions import show_message


def main():
  project_name = input("Enter project name: ")
  author = input("Enter project author: ")
  language = ""

  # Gets project language
  while True:
    print()
    print("[ 0 ] Python")
    print()

    language_number = input("Select project language: ")
    try:
      if int(language_number) == 0:
        # Selected python
        language = "python"
      else:
        # Language not found
        show_message("Language not found!")
        continue
    except ValueError:
      # Error
      show_message("Please select number!")
      continue

    break

  empty_project = EmptyProject(project_name, author, language)
  empty_project.create()

if __name__ == "__main__":
  main()
