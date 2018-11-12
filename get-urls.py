import argparse
import pandas as pd
import parser
import sqlite3
import sys

parser = argparse.ArgumentParser()
parser.add_argument("input",
                    help="chictopia.sqlite3")
parser.add_argument("output")
args = parser.parse_args()

db = sqlite3.connect(args.input)
photos = pd.read_sql("SELECT *, 'http://images2.chictopia.com' || path AS url FROM photos WHERE photos.post_id IS NOT NULL AND file_file_size IS NOT NULL", con=db)
photos['id'] = photos['id'].map(lambda d: '%07d.jpg' % d)
photos.to_csv(args.output, header=False, columns=['id', 'url'], index=False, encoding='utf-8')
