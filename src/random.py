'''
  random number generator
'''
import os
import binascii
import argparse

parser = argparse.ArgumentParser(description='generate random string')
parser.add_argument('size', metavar='size', type=int, help='length of the random string')

args = parser.parse_args()


string = binascii.b2a_base64(os.urandom(args.size))
string = string[:args.size]
string = str(string, encoding='utf-8')
print(string)
