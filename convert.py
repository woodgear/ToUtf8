import chardet
import os
import os.path
import codecs
def detect_encode(path):
    rawdata = open(path, "rb").read()
    result = chardet.detect(rawdata)
    return result


def list_all_codefile(dir):
    for root, dirs, files in os.walk(dir):
        list=[]
        for name in files:
            path=os.path.join(root, name)
            if path.endswith("h") or path.endswith("cpp"):
                list.append(path)
        return list


def convert(source,sourceEncode,target,targetEncode):
    BLOCKSIZE = 1024*1024
    with codecs.open(source, "r",sourceEncode) as sourceFile:
        with codecs.open(target, "w", targetEncode) as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)

def convert_file_to_utf8(path):
    encode=detect_encode(path)
    if encode["confidence"]<0.9:
        print(path+"=>"+str(encode))
        if(input("ha ~ ,are sure? (yes/no)")!="yes"):
            return False
    if(encode["encoding"]=="utf_8"):
        return True
    print("to utf_8 -> %s %s"%(path,str(encode)))
    convert(path,encode["encoding"],path+"_utf8","utf_8")
    os.remove(path)
    os.rename(path+"_utf8",path)

def convert_dir(dir):
    if os.path.isdir(dir):
        for path in list_all_codefile(dir):
            convert_file_to_utf8(path)


convert_dir("SetupFrame")
