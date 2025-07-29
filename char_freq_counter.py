def char_freq(ss):
  ss = (ss.lower().replace(" ", ""))
  my_dict = {x: ss.count(x) for x in ss}
  my_dict = dict(sorted(my_dict.items()))
  for k, v in my_dict.items():
    print(f"{k} = {v}")

  return my_dict


if __name__ == "__main__":
  enter = input("Enter a string:")
  char_freq(enter)
