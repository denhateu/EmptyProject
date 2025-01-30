import os
import subprocess


class EmptyProject:
  def __init__(self, project_name, author, lang):
    self.project_name = project_name
    self.author = author
    self.lang = lang

  def create_project_dir(self, directory):
    if os.path.exists(directory):
      return False
    else:
      os.makedirs(directory)
      return True

  def create(self):
    print()
    print(f"Project name: {self.project_name}")
    print(f"Project author: {self.author}")
    print(f"Project language: {self.lang}")
    print()
    print("==========")
    print()

    # Create project directory in current directory
    project_dir = f"{os.getcwd()}/{self.project_name}"
    print(f"Project directory: {project_dir}")

    if self.create_project_dir(project_dir):
      print("Directory created")
    else:
      print("Project directory already exists!")

    # Open project dir
    os.chdir(project_dir)

    # Create local git repo
    if os.path.exists(f"{project_dir}/.git/"):
      print("Git repo is exists!")
    else:
      subprocess.run(["git", "init"])
      print("Local git repo created!")

    if self.lang == "python":
      # Create README.md file
      with open("README.md", 'w', encoding="utf-8") as readme_file:
        readme_file.write(f"# {self.project_name}\n")

      print("README.md created")

      # Create .gitignore file
      with open(".gitignore", 'w', encoding="utf-8") as gitignore_file:
        gitignore_file.write("venv/\n")

      print(".gitignore created")

      # Create python venv
      subprocess.run(["python3", "-m", "venv", "venv"])

      print("Python venv created")


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
