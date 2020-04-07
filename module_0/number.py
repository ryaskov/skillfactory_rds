def guess_num(some_number):
  counter = 1
  number_to_guess = 50
  adder = 50
  while number_to_guess != some_number:
    counter += 1
    if adder != 1:
      adder = round(adder/2)
    if some_number > number_to_guess:
      number_to_guess += adder
    else:
      number_to_guess -= adder
  return(counter)