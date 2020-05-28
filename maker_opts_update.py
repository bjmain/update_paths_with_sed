import glob
import os

# Update the fasta file in every maker_opts.ctl file

opts_files = glob.glob("chnk_*/maker_opts.ctl")
for f in opts_files:
    filename = f.split("/")[0]
    new_chnk = "/home/bmain/otherpath/" + filename + "/" + filename + ".fa"
    os.system("sed 's#/home/bmain/path/chnk1/chnk1.fa#%s#g' %s" % (new_chnk, f))
