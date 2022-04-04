import sys
import xml.dom.minidom as md


def main(args):
    if len(args)>1:
        filename = args[1]
    else:
        exit
    if len(args)>2: 
        split_string = args[2]
    else:
        split_string = ''

    print(f'Splitting {filename} at {split_string} level')
    with open(args[1],'r') as f:
        split_no = 0
        for linecount, line in enumerate(f):
            print(line,end='')
            try:
                doc = md.parseString(line)
                for c in doc.childNodes:
                    print(c.Name,eol=',')
            except:
                print('ok')
    

if __name__ == "__main__":
    doc = md.Document()
    doc = md.parseString('<Style><LineStyle><color>ff0000ff</color></LineStyle><PolyStyle><fill>0</fill></PolyStyle></Style>')
    print(type(doc))
    print(type(doc.childNodes[0]))
    print(doc.__dict__)
    input('press [Enter]')
    main(sys.argv)