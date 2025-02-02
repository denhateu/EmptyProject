"""
EmptyProject

Author: Danil Aksenow (@denhateu)
Version: 0.0.0-alpha
"""

import sys

from emptyproject import EmptyProject
from functions import show_message, get_lang


def main():
  if len(sys.argv) <= 1:
    # No arguments
    project_name = input("Enter project name: ")
    author = input("Enter project author: ")
    language = ""

    # Gets project language
    while True:
      print()
      print("[ 0 ] Python")
      print()

      language_number = input("Select project language: ")

      language = get_lang(language_number)
      if language is not False:
        break
      else:
        show_message("Select language number!")
        continue
  else:
    # Arguments found, parse

    # List for errors
    errors = []

    # Get project name
    try:
      project_name = sys.argv[1]
    except IndexError:
      errors.append("Input project name!")

    # Get author name
    try:
      author = sys.argv[2]
    except IndexError:
      errors.append("Where project author name blyat?")

    # Get project language
    try:
      language = get_lang(sys.argv[3])
      if language is False:
        errors.append("Choose correct language!")
    except IndexError:
      errors.append("Enter project language uebok")

    if len(errors) >= 1:
      # No errors
      show_message(errors[0])
      print()
      
      sys.exit(1)

  # Create project
  empty_project = EmptyProject(project_name, author, language)
  empty_project.create()

if __name__ == "__main__":
  main()
