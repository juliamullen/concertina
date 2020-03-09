from concertina import identify_matches, Note

song = [
    # Measure 1
    (
      (Note('E', 2), Note('G#', 2)),
      'Measure 1: EM'
      ),
    (
      (Note('F', 2), Note('A', 2)),
      'F M3'
      ),
    (
      (Note('A', 2), Note('C', 3)),
      'A M3'
      ),
    (
      (Note('A', 2), Note('D', 3)),
      'D inverted'
      ),

    # Measure 2
    (
      (Note('C', 3), Note('F', 3)),
      'Measure 2: F inverted'
      ),
    (
      (Note('C', 3), Note('A', 3)),
      'Am inverted'
      ),

    # Measure 3
    (
      (Note('F#', 3), Note('Bb', 3)),
      'Measure 3: F# M3?'
      ),
    (
      (Note('D', 3), Note('A', 3)),
      'D5'
      ),
    (
      (Note('C', 3), Note('F#', 3)),
      'Csus4?? F is still sharp I think?'
      ),
    (
      (Note('A', 2), Note('D', 3)),
      'D5 inv?'
      ),


    # Measure 4
    (
      (Note('F#', 2), Note('C', 3)),
      'Measure 4: F#5'
      ),
    (
      (Note('E', 3), Note('A', 3)),
      'Am5 inv?'
      ),

    # Measure 5
    (
      (Note('D', 3), Note('A', 3)),
      'Measure 5: D5'
      ),
    (
      (Note('D', 3), Note('G', 3)),
      'G inv'
      ),
    (
      (Note('D', 3), Note('A', 3)),
      'D5'
      ),
    (
      (Note('D', 3), Note('G', 3)),
      'G inv'
      ),

    # Measure 6
    (
      (Note('D', 3), Note('A', 3)),
      'Measure 6: D5'
      ),
    (
      (Note('D', 3), Note('G', 3)),
      'G inv'
      ),

    # Measure 7
    (
      (Note('A', 3), Note('C', 4)),
      'Measure 7: Am'
      ),
    (
      (Note('E', 3), Note('A', 3)),
      'A inv'
      ),
    (
      (Note('D', 3), Note('G', 3)),
      'G5 inv'
      ),
    (
      (Note('C', 3), Note('E', 3)),
      'CM'
      ),

    # Measure 8
    (
      (Note('Bb', 2), Note('D', 3)),
      'Measure 8: Bb'
      ),


]

for i in song:
  identify_matches(*i)
