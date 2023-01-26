import pandas as pd
from flask import Flask, make_response, jsonify, request
import json

app = Flask(__name__)


# Classe Triângulo
class Triangulo:

  def toJson(self):
    return json.dumps(self,
                      default=lambda o: o.__dict__,
                      sort_keys=True,
                      indent=4)


# contruir as funcionalidades
@app.route('/')
def homepage():
  return 'A API está no ar'


@app.route('/calculo', methods=['POST'])
def calculoLadoTriangulo():
  triangulo = request.json

  triangulo_obj = Triangulo()
  triangulo_obj.cateto1 = triangulo['cateto1']
  triangulo_obj.cateto2 = triangulo['cateto2']
  triangulo_obj.hipotenusa = triangulo['hipotenusa']

  if (triangulo_obj.cateto1 == None):
    triangulo_obj.cateto1 = pow(
      ((triangulo_obj.hipotenusa * triangulo_obj.hipotenusa) -
       (triangulo_obj.cateto2 * triangulo_obj.cateto2)), 1/2)

  if (triangulo_obj.cateto2 == None):
    triangulo_obj.cateto2 = pow(
      ((triangulo_obj.hipotenusa * triangulo_obj.hipotenusa) -
       (triangulo_obj.cateto1 * triangulo_obj.cateto1)), 1/2)

  if (triangulo_obj.hipotenusa == None):
    triangulo_obj.hipotenusa = pow(
      ((triangulo_obj.cateto2 * triangulo_obj.cateto2) +
       (triangulo_obj.cateto1 * triangulo_obj.cateto1)), 1/2)

  triangulo = triangulo_obj.toJson()
  return triangulo


# Rodar API
app.run()
