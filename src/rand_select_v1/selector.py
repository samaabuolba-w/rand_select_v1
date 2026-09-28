import random

def random_selection(n_list, q_list, rng=random, used_names=()):
  available_names = [n for n in n_list if n not in used_names]

  chosen_name = rng.choice(available_names)
  chosen_question = rng.choice(q_list)

  return (chosen_name, chosen_question)