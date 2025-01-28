class EmptyProject:
  def __init__(self, project_name, author, lang):
    self.project_name = project_name
    self.author = author
    self.lang = lang

  def create(self):
    print(self.project_name)
    print(self.author)
    print(self.lang)


def main():
  project_name = input("Enter project name: ")
  author = input("Enter project author: ")

  # Gets project language
  while True:
    print()
    print("[ 0 ] Python")
    print()

    language = input("Select project language: ")
    try:
      if int(language) == 0:
        # Selected python
        pass
      else:
        # Language not found
        print("Language not found!")
        continue
    except ValueError:
      # Error
      print()
      print("Please select number!")
      continue

    break

  empty_project = EmptyProject(project_name, author, language)
  empty_project.create()

if __name__ == "__main__":
  main()
