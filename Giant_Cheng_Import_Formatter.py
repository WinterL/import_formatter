import os
import codecs
import re

# Create a txtlist to store all txt filename in current directory.
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
    section = "none"
    contentlist = []
    for line in inlist:
        linekw = re.compile(u'\d\-?\d?\.?\u3000(.+)')
        if section == "none":
            if re.match(linekw, line):
                section = "content"
                templine = re.match(linekw, line)
                vocabulary = templine.group(1)
        elif section == "content":
            if re.match("\r\n", line):
                section = "none"
                outfile.write(vocabulary + " " +
                              '<br/>'.join(contentlist) + "\r\n")
                contentlist = []
            else:
                line = line.rstrip()
                contentlist.append(line)
    else:
        print "Format completed!"
        outfile.close()

#        os.rename(outfilename, infilename)
#        os.chdir("../")
#        os.remove(infilename)
