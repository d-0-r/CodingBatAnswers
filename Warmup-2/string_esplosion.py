#Instructions
#Given a non-empty string like "Code" return a string like "CCoCodCode". 


def string_splosion(str):
  string = ""
  for i in range(len(str)):
    string = string + str[:i+1]
  return string
