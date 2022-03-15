def get_results(kilograms, gravity, feet):
  if kilograms:
    kilograms = float(kilograms)
  else:
    return 0.0
  if gravity:
    gravity = float(gravity)
  else:
    return 0.0
  if feet:
    feet = float(feet)
  else:
    return 0.0
  potential_energy = kilograms * gravity * feet
  results = "{} j".format(potential_energy)
  return results