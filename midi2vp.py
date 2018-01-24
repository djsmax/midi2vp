import argparse
import mido
import os


nts = list('1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",type = str,
                        help = "path to MIDI file (.mid)")
    parser.add_argument('-r',"--transpose",type = int,default = 0,
                        help = "transpose song to N octaves (both plus and minus values)")
    parser.add_argument('-t',"--track",type = int,default = 0,
                        help = "number of MIDI-track (if becomes more than one)")
    args = parser.parse_args()
    if not args.transpose in range(-6,7):
        raise ValueError("transpose value must be between range of -6 and 6")
        
    if not os.path.isfile(args.filename):
        raise ValueError("file {} don't exist".format(args.filename))

    s = mido.MidiFile(args.filename, charset = 'utf-8') ##i don't catching any exceptions
    ## about non-MIDI files here, mido do it well by itself
    try:
        track = s.tracks[args.track]
    except IndexError:
        raise ValueError("there's no track #{} in this MIDI file :("
                         .format(args.track))


    notes = []
    tn = []

    for msg in track:
        if not msg.is_meta:
            if msg.type == 'note_on' and msg.velocity != 0:
                if tn:
                    tn.append(msg.note)
                else:
                    tn = [msg.note]
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                if tn:
                    notes.append(tn)
                    tn = []

    print("Total notes: {}".format(len(notes)))

    asc_notes = ''

    for i in notes:
        l = ''
        for ii in sorted(i):
            if ii in range(24,85):
                try:
                    l += nts[ii - 24 + args.transpose * 12]
                except IndexError: ## here comes errors with transposing, i know this is very bad way to do like that,but..
                    print("Note {} can't be transposed".format(ii))
            else:
                print("Note {} can't be converted".format(ii))
        asc_notes += l + ' '

    stf = os.path.split(args.filename)
    tf = os.path.join(stf[0],os.path.splitext(stf[1])[0] + '.txt')

    open(tf,'w').write(asc_notes)
