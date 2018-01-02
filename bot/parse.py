import xml.etree.ElementTree as etree

ns = {'ns2': 'http://idecs.nvg.ru/privateoffice/ws/types/'}


def parse(el):
    return (el.find('ns2:characteristicName', ns).text,
            el.find('ns2:characteristic', ns).text)


def main(f):
    tree = etree.parse(f)

    err = tree.find('.//ns2:error', ns)
    if err is not None:
        return err.text

    l = []
    for x in tree.findall('.//ns2:any', ns):
        l.append(parse(x))
    return l

if __name__ == '__main__':
    print(main('res.xml'))
