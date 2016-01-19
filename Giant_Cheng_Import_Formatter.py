import os
import codecs
import re

txtkw = re.compile('txt\Z')
txtlist = filter(txtkw.search, os.listdir(u'.'))

# Mistake-proofing
if len(txtlist) == 0:
    print "There is no text file in current directory, " \
        + "please move some text files to current directory."
elif "importfile.txt" in txtlist:
    print "importfile.txt Dectected, please remove this file."
# Main
else:
    infilename = txtlist[0]
    outfilename = u"importfile.txt"
    infile = codecs.open(infilename, 'r', encoding='utf-16')
    inlist = infile.readlines()
    infile.close()

    outfile = codecs.open(outfilename, 'w', encoding='utf-8')
    state = "none"
    contentlist = []
    for line in inlist:
        linekw = re.compile(u'\d\-?\d?\.?\u3000(.+)\r\n')
        if re.match(linekw, line):
            if state == "ready"
                # Check follow and mean
                for item in contenlist:
                    fwkw = re.compile(u'\+')
                    if re.search(fwkw, item):
                        print "follow"
                        fwflag = TRUE
                    if
                # TODO Replace \n to \r\n when release windows version
                outfile.write(vocabulary + " " +
                              '<br/>'.join(contentlist) + "\n")
                contentlist = []
                state = "prepare"
            templine = re.match(linekw, line)
            vocabulary = templine.group(1)
        else:
            state = "ready"
            line = line.rstrip()
            contentlist.append(line)
    else:
        print vocabulary
        print "Format completed!"
        outfile.close()

