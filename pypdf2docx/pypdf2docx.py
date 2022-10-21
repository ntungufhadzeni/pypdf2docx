#! python
import os
from pdf2docx import Converter
import sys


def convert(arg_input, arg_output):
    cv = Converter(arg_input)
    cv.convert(arg_output)
    cv.close()


def main():
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        if len(sys.argv) > 2:
            output_file = sys.argv[2]
            if not os.path.isdir(output_file):
                output_path = os.path.join(os.path.dirname(input_file), output_file)
                convert(input_file, output_path)
            else:
                if os.path.isdir(output_file):
                    filename_l = os.path.basename(input_file).split('.')
                    filename = filename_l[0] + '.docx'
                    output_path = os.path.join(os.path.dirname(input_file), filename)
                    convert(input_file, output_path)
                else:
                    output_path = output_file
                    convert(input_file, output_path)
        else:
            filename_l = os.path.basename(input_file).split('.')
            filename = filename_l[0] + '.docx'
            output_path = os.path.join(os.path.dirname(input_file), filename)
            convert(input_file, output_path)

    else:
        print('Usage: pypdf2docx [path to pdf] [output name | path]')
