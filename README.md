# midi2vp

Very simple and easy *.mid files to Virtualpiano sheets converter. It converts (one) midi track to ASCII characters, for playing on the [VirtualPiano site](https://https://virtualpiano.net).
### Main usage
Written in Python, the script requires a mido library to read MIDI files. Easily install this: `sudo pip install mido`. Then download this script,and the MIDI file of the song you want to convert. In this example, MIDI called `Beethoven - Moonlight Sonata.mid`.

Convert it:

`python midi2vp "Beethoven - Moonlight Sonata.mid"`

 After a moment, in the same folder will appear the file called `Beethoven - Moonlight Sonata.txt`. It will contain "sheets" (just characters you need to type for play). Chords, such as they are will be converted in this way,you will understand how to play the chord.

If you have more than one track in MIDI file,you should check next option:
`python midi2vp "Beethoven - Moonlight Sonata.mid" -t 1`

Where `-t` -- is argument for setting the track number.

Please notice that piano on virtualpiano.net supports 5 octaves - from C2 to C7. At the process of conversion you can see message like `Note 60 can't be converted`. It means that this note is not in range between 2 and 6 octave, you can't just play it :)

Also, if you play chords, you can't make chord containing sharp / flat and non-sharp / non-flat notes: you just can't press key with and without Shift at the same time. 


### Transpose
This script also supports transpose. To transpose any song, add `-r` argument.

`python midi2vp "Beethoven - Moonlight Sonata.mid" -r 1`

This command will convert the file and transpose 1 octave up. Just as simple you can transpose 2 (or 3 or 7,depends on what do you want to get):

`python midi2vp "Beethoven - Moonlight Sonata.mid" -r -2`

Also be careful, sometimes you can cath up the message like `Note 40 can't be transposed`.

Read the previous paragraph, if you you want to know, indeed why.
