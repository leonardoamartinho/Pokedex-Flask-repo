from flask import Flask, render_template
from flask import request
import requests, json


app = Flask(__name__)

@app.route('/')
def main():

    return render_template("main.html")

@app.route('/pokedex/<generation>')
def pokedex(generation):


    #url = "https://pokeapi.co/api/v2/pokemon/?limit=-1"

    #response = requests.get(url)

    #pokemons = response.json()

    pokemonList = []

    if generation == 'one':
        for i in range (1,152,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'two':
        for i in range (152,252,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'three':
        for i in range (252,387,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'four':
        for i in range (387,494,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'five':
        for i in range (494,650,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'six':
        for i in range (650,722,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'seven':
        for i in range (722,810,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'eight':
        for i in range (811,906,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'nine':
        for i in range (906,1009,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    elif generation == 'national':
        for i in range (0,1009,1): 
            pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
    
    #for i in range (1,20,1): 
    #    pokemonList.append(requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}').json())
        

    return render_template("pokedex.html", pokemonList=pokemonList)

if __name__ =="__main__":
    app.run(debug=True)