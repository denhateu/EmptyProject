def show_message(message: str = "") -> None:
  print()

  print("=" * (len(message) + 2))
  print(f" {message}")
  print("=" * (len(message) + 2))

def get_lang(language):
  try:
    if language == "python" or int(language) == 0:
      result = "python"
    else:
      return False
  except ValueError:
    return False

  return result
