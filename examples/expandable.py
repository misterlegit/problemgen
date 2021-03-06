from problemgen.container import Worksheet 
import random
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("wn_number", help='Number of the worksheet')
args = parser.parse_args()

wn_number = args.wn_number
todaydate = time.strftime("%m-%d-%Y")

w = Worksheet('%s-%s.tex' % (todaydate, wn_number))
w.set_title('Worksheet %s for the week of %s' % (wn_number, todaydate))
w.set_message('Outline, step by step, how you use the FOIL method to multiply binomials. Then multiply each binominal. Show your work.')
for _ in range(25):
    w.add_expandable_expression(order=2, factor_order=1, leading_coeff=True)
# w.shuffle()
w.make(num_cols=2)
