import os
import subprocess


class EmptyProject:
  """
  Using this class you can create project directory for specific
  programming language
  """

  def __init__(self, project_name, author, lang) -> None:
    self.project_name = project_name
    self.author = author
    self.lang = lang

  def create_dir(self, directory: str = "") -> bool:
    """
    Creates directory if not exists

    args:
      directory:
        Name of directory
    """

    if os.path.exists(directory):
      return False
    else:
      os.makedirs(directory)
      return True

  def create(self) -> None:
    """
    Creates all that need for project, for example, directory,
    environment, scripts and etc.
    """

    print()
    print("=====Project info=====")
    print(f"Project name: {self.project_name}")
    print(f"Project author: {self.author}")
    print(f"Project language: {self.lang}")
    print("==========")

    print()
    print("=====Logs=====")

    # Create project directory in current directory
    project_dir = f"{os.getcwd()}/{self.project_name}"
    print(f"Project directory: {project_dir}")

    if self.create_dir(project_dir):
      print("Directory created")
    else:
      print("Project directory already exists!")

      recreate = input("Recreate project? [y/N]: ")
      if recreate == "y" or recreate == "Y":
        print("Recreating project...")
      else:
        print("Cancel")
        return False

    print()

    # Open project dir
    os.chdir(project_dir)

    # Create local git repo
    subprocess.run(["git", "init"])

    # Create README.md file
    with open("README.md", 'w', encoding="utf-8") as readme_file:
      readme_file.write(f"# {self.project_name}\n")

    print("README.md created")

    # Create .gitignore file
    gitignore_file = open(".gitignore", 'w', encoding="utf-8")

    if self.lang == "python":
      gitignore_file.write("venv/\n")

      # Create python venv
      subprocess.run(["python3", "-m", "venv", "venv"])

      print("Python venv created")

      # Create main.py file
      self.create_dir("scripts")

      main_script = """def main():
  print("huy")

if __name__ == "__main__":
  main()"""

      with open("scripts/main.py", 'w', encoding="utf-8") as main_file:
        main_file.write(main_script)

      print("File main.py created!")

    gitignore_file.close()

    print(".gitignore created")

    print("==========")
    print()
    print("Project created!")
    print()
