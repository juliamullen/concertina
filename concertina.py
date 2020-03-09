import itertools

class Note:
  def __init__(self, name, octave):
    self.name = name
    self.octave = octave

  def __repr__(self):
    return "<Note {}{}>".format(self.name, self.octave)

class Button:
  def __init__(self, draw, drawOctave, push, pushOctave):
    self.draw = draw
    self.push = push
    self.d8 = drawOctave
    self.p8 = pushOctave

  def set_button_info(self, row_index, button_index):
    self.row_index = row_index
    self.button_index = button_index
    #print((row_index, button_index))

  def play(self, note):
    if note.name == self.draw:
      if note.octave == self.d8:
        return "draw"
    if note.name == self.push:
      if note.octave == self.p8:
        return "push"
    return False

  def __str__(self):
    button_info = "{} Button #{}".format(Layout.LAYOUT_NAMES[self.row_index].title(), self.button_index + 1)
    note_info = "{}{} out / {}{} in".format(
        self.draw, self.d8,
        self.push, self.p8
    )
    return "{} ({})".format(button_info, note_info)

  def __repr__(self):
    return self.__str__()

class Layout:
  LEFT_ACCIDENTAL = [
    ('F', 1, 'E', 1),
    ('Bb', 1, 'A', 1),
    ('Eb', 2, 'C#', 2),
    ('G', 2, 'A', 2),
    ('Bb', 2, 'G#', 2)
  ]

  LEFT_C = [
    ('G', 1, 'C', 1),
    ('B', 1, 'G', 1),
    ('D', 2, 'C', 2),
    ('F', 2, 'E', 2),
    ('A', 2, 'G', 2)
  ]

  LEFT_G = [
    ('A', 1, 'B', 1),
    ('F#', 2, 'D', 2),
    ('A', 2, 'G', 2),
    ('C', 3, 'B', 2),
    ('E', 3, 'D', 3)
  ]

  RIGHT_ACCIDENTAL = [
    ('Eb', 3, 'C#', 3),
    ('G', 3,  'A', 3),
    ('Bb', 3, 'G#', 3),
    ('Eb', 4, 'C#', 4),
    ('F', 4,  'A', 4)
  ]

  RIGHT_C = [
    ('B', 2, 'C', 3),
    ('D', 3, 'E', 3),
    ('F', 3, 'G', 3),
    ('A', 3, 'C', 4),
    ('B', 3, 'E', 4)
  ]

  RIGHT_G = [
    ('F#', 3, 'G', 3),
    ('A', 3, 'B', 3),
    ('C', 4, 'D', 4),
    ('E', 4, 'G', 4),
    ('F#', 4, 'B', 4)
  ]

  LAYOUT_NAMES = ["left accidental", "left c", "left g", "right accidental", "right c", "right g"]

  def __init__(self):
    self.notes = [self.LEFT_ACCIDENTAL, self.LEFT_C, self.LEFT_G, self.RIGHT_ACCIDENTAL, self.RIGHT_C, self.RIGHT_G]
    self.reset()

  def reset(self):
    self.pressed_buttons = []

  def press_button(self, button, action):
    self.pressed_buttons.append((button, action))

  def __str__(self):
    mode = False
    representation = [['-' for i in range(5)] for i in range(6)]
    for button, action in self.pressed_buttons:
      action_char = 'o' if action == 'draw' else 'x'
      try:
        representation[button.row_index][button.button_index] = action_char
      except IndexError:
        print("Couldn't find row {} button {}".format(button.row_index, button.button_index))
    depiction = []
    for r in representation:
      depiction.append("".join(r))

    return "{} {}\n{} {}\n{} {}\n\n".format(
        depiction[0], depiction[3],
        depiction[1], depiction[4],
        depiction[2], depiction[5]
      )


buttons = []

layout = Layout()
for i, row in enumerate(layout.notes):
  for j, button_info in enumerate(row):
    new_button = Button(*button_info)
    new_button.set_button_info(i, j)
    buttons.append(new_button)

def identify_matches(note_list, chord_name):
  #print("notes -- {}".format(note_list))
  print("chord {}".format(chord_name))
  matched_lists = []
  for note in note_list:
    matched_notes = []
    for button in buttons:
      action = button.play(note)
      if action:
        matched_notes.append((button, action))
    if len(matched_notes) == 0:
      print("Couldn't find {}{}".format(note.name, note.octave))
      return
    matched_lists.append(matched_notes)

  # try drawing:
  def get_layouts(matched_lists, action):
    #print('matches list', matched_lists)
    actions = []
    for note in matched_lists:
      # Each "note" here corresponds to a list of buttons
      notes_for_action = [b for b in note if b[1] == action]
      if not notes_for_action:
        actions.append([])
      actions.append(notes_for_action)
    #print("\n", action, "\n\nactions", *actions, "\nproduct", list(itertools.product(*actions)), '\n')
    if all(actions):
      for combo in itertools.product(*actions):
        #print('comb', combo)
        layout.reset()
        for button in combo:
          layout.press_button(*button)
        print(layout)
        return True

  if not(get_layouts(matched_lists, 'push')):
    get_layouts(matched_lists, 'draw')

"""
  pushs = [b for match in matched_lists for b in match if b[1] == 'push']
  if all(pushs):
    for combo in itertools.product(pushs):
      layout.reset()
      print('c2', combo)
      for button, action in combo:
        layout.press_button(button, 'push')
      print(layout)

"""
"""
Example output:
(push)
----- -----
--x-- -----
x---- -----

(push)
----- -----
--ooo -----
----- ----
"""
