
import os
import codecs
import re



#
# amenamefile = codecs.open("Gamename.txt", 'r', encoding='utf-16')
# amename = gamenamefile.readline().rstrip()
# amenamefile.close()


# xtkw = re.compile('txt\Z')
# xtlist = filter(txtkw.search, os.listdir(u'.'))
# xtlist.remove("Gamename.txt")

# f len(txtlist) == 0:
#    print "There is no text file in current directory, " \
#            + "Please move a text file to current directory."
# lif len(txtlist) > 1:
#    print "There are mutiple text files in current directory " \
#            + "please remove unnecessary txt files."
# lse:
#    #
#    infilename = txtlist[0]
#    outfilename = u"out" + txtlist[0]
#    if "processed" not in os.listdir(u'.'):
#        os.mkdir("processed")

#    infile = codecs.open(infilename, 'r', encoding='utf-16')
#    os.chdir("./processed/")
#    outfile = codecs.open(outfilename, 'w', encoding='utf-16')
#    #
#    donekw = re.compile(u'.+\u3000-.+')
#    for line in infile.readlines():

#        if re.search(donekw, line):
#            print "This file was formatted, please replace a new text file."
#            infile.close()
#            outfile.close()
#            os.remove(outfilename)
#            break
#        else:
#            linekw1 = re.compile(u'(\u300C.+\u300D)+\r\n')
#            linekw2 = re.compile(u'(\u300C.+\u300D)+.+\r\n')
#            linekw3 = re.compile(u'(\u300C.+\u300D)+.+(\u300C.+\u300D)+\r\n')
#            if re.match(linekw3, line):
#                line = line.rstrip()
#                outfile.write(line + u'\u3000' + "-" + gamename + "\r\n")
#            elif re.match(linekw1, line):
#                line = line.rstrip()
#                outfile.write(line + u'\u3000' + "-" + gamename + "\r\n")
#            else:
#                # Unicode 300C 3000 300D
#                line = line.rstrip()
#                outfile.write(u'\u300C' + line + u'\u300D' + u'\u3000' +
#                              "-" + gamename + "\r\n")
#    else:
#        print "Format completed!"
#        infile.close()
#        outfile.close()

#        os.rename(outfilename, infilename)
#        os.chdir("../")
#        os.remove(infilename)
