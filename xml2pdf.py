import lxml.etree as ET
import argparse
import pdfkit

def xml2dom(xml_file, xslt_file):
    dom = ET.parse(xml_file)
    xslt = ET.parse(xslt_file)
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    return(newdom)

def html2pdf(dom, file_name):
    output = file_name + '.pdf'
    html = ET.tostring(dom, pretty_print=True).decode('utf-8')
    pdfkit.from_string(html, output)

def xml2pdf(xml_file, xslt_file, output):
    dom = xml2dom(xml_file, xslt_file)
    html2pdf(dom,output)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-xml', '--xml_infile', help='XML infile to be transformed.')
    parser.add_argument('-xslt','--xslt_file', help='XSLT for transforming')
    parser.add_argument('-o', '--output', help='Name of PDF output')
    args = parser.parse_args()

    if args:
        if args.xml_infile:
            xml = args.xml_infile

        if args.xslt_file:
            xslt = args.xslt_file

        if args.output:
            output = args.output
            
        else:
            output = 'output'

        xml2pdf(xml,xslt,output)

if __name__ == '__main__':
    main()
