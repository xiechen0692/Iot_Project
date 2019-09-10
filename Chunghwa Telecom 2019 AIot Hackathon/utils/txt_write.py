import os
def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    (filename,extension) = os.path.splitext(name)
                    file.write(filename + " " + "depth/" + name + "\n")
                    break

def write_all(dir, file):
    files = os.listdir(dir)
    files.sort()
    for name in files:
        file.write(dir + "/" + name + "\n")

def Test():
  dir="/home/xiec/Research/PyTorch-YOLOv3-master/lumen_data/images/valid_img"
  outfile="/home/xiec/Research/PyTorch-YOLOv3-master/lumen_data/" + "/" + "valid.txt"
  wildcard = ".jpg"

  file = open(outfile,"w")
  if not file:
    print ("cannot open the file %s for writing" % outfile)
  # ListFilesToTxt(dir,file,wildcard, 1)
  write_all(dir, file)

  file.close()

Test()
