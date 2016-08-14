import re
import sys
import getopt

def filter(in_file,out_file):
    p01=re.compile(r"<br>")
    p02=re.compile(r"&nbsp;");
    p2=re.compile(r"<img [^>]*>")
    p3=re.compile(r"<noscript>([^<]*)</noscript>")
    p4=re.compile(r"<a [^>]*>([^<]*)</a>")
    p5=re.compile(r"<strong>([^<]*)</strong>")
    p6=re.compile(r"<em>([^<]*)</em>")
    p7=re.compile(r"<sup>([^<]*)</sup>")
    p8=re.compile(r"<b>([^<]*)</b>",re.X|re.M)
    p9=re.compile(r"<p>([^<]*)</p>",re.X|re.M)

    in_file=open(in_file)
    xx=in_file.read()
    in_file.close()
    #sprint(xx)

    y=p01.sub("\n",xx)
    y=p02.sub("\n",y)
    y=p2.sub("",y)
    y=p3.sub(r"\1",y)
    y=p4.sub(r"\1",y)
    y=p5.sub(r"\1",y)
    y=p6.sub(r"\1",y)
    y=p7.sub(r"\1",y)
    y=p8.sub(r"\1",y)
    y=p9.sub(r"\1",y)
    #print(y)

    out=open(out_file,"w")
    out.write(y)
    out.close()

def PrintUsage():
    print("Usage:")
    print("filter -i [input_file] -o [output_file]")

opts,args=getopt.getopt(sys.argv[1:],"hi:o:")
input_file=r"in.txt"
output_file=r"out.txt"
for op,value in opts:
    if op=="-i":
        input_file=value
    elif op=="-o":
        output_file=value
    elif op=="-h":
        PrintUsage()
        exit(0)
    
filter(input_file,output_file)
