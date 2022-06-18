from flask import Flask
from flask_restful import Resource, Api, reqparse
from sqlalchemy import true
from sympy import arg
from pyspark import SparkContext
from matchHelper import get_close_matches
from difflib import get_close_matches as get_close_matches1
from heapq import nlargest as _nlargest


app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()

sc = SparkContext(master='local[*]', appName='matcher')

text_rdd = sc.textFile('chem_file.txt').repartition(16)
# print(text_rdd.take(1))


class Test(Resource):
    def post(self):
        parser.add_argument("name")
        args = parser.parse_args()
        
        mapped = text_rdd.map(lambda name:get_close_matches(args["name"],[name]))
        reduced = mapped.reduce(lambda x,y:_nlargest(5,x+y))
        return {"data":reduced}


api.add_resource(Test,'/matcher/')

if __name__ == '__main__':
    app.run(debug=true)

