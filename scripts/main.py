import os


class EmptyProject:
  def __init__(self, project_name, author, lang):
    self.project_name = project_name
    self.author = author
    self.lang = lang

  def create(self):
    print()
    print(f"Project name: {self.project_name}")
    print(f"Project author: {self.author}")
    print(f"Project language: {self.lang}")
    print()
    print("==========")
    print()

    if self.lang == "python":
      # Create project directory in current directory
      project_dir = f"{os.getcwd()}/{self.project_name}"
      print(f"Project directory: {project_dir}")

      if os.path.exists(project_dir):
        print("Project directory is exists!")
      else:
        os.makedirs(project_dir)
        print("Directory created")


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
        print("Language not found!")
        continue
    except ValueError:
      # Error
      print("Please select number!")
      continue

    break

  empty_project = EmptyProject(project_name, author, language)
  empty_project.create()

if __name__ == "__main__":
  main()
