from flask import Flask, jsonify
import psycopg2
from api.models.animals import Animal
from api.models.plants import Plant

def create_app(database, dbuser, dbpassword):
    app = Flask(__name__)

    app.config.from_mapping(DATABASE=database,
                            DBUSER=dbuser,
                            DBPASSWORD=dbpassword)
    
    @app.route('/')
    def homepage():
        return """This is the homepage for occurences in Ecuador for:
        Plants
        Animals"""


    @app.route('/plants')
    def plants_index():
        conn = psycopg2.connect(database = app.config['DATABASE'],
                                user = app.config['DBUSER'],
                                password = app.config['DBPASSWORD'])
        cursor = conn.cursor()
        cursor.execute('SELECT local_id, associatedTaxa FROM plants')
        plant_names = cursor.fetchall()
        return jsonify(plant_names)
    
    @app.route('/plants/<id>')
    def show_plant(id):
        conn = psycopg2.connect(database = app.config['DATABASE'],
                                user = app.config['DBUSER'],
                                password = app.config['DBPASSWORD'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM plants WHERE local_id = %s', (id,))
        plant_response = cursor.fetchall()
        return Plant(plant_response).__dict__

    @app.route('/animals')
    def animals_index():
        column_keys = ['local_id', 'kingdom', 'phylum', 'class_', 'order_', 'family', 'scientificName']
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['DBUSER'], password = app.config['DBPASSWORD'])
        cursor = conn.cursor()
        # cursor.execute("SELECT local_id, kingdom, phylum, class_, order_, family, scientificName FROM animals")
        cursor.execute('SELECT local_id, kingdom, phylum, class_, order_, family, scientificName FROM animals')
        animal_names = cursor.fetchall()
        animal_objs = [Animal(animal_name, columns=column_keys) for animal_name in animal_names]
        animal_dicts = [animal_obj.__dict__ for animal_obj in animal_objs]
        # animal_dicts_with_correct_keys = [animal_dict for animal_dict in animal_dicts if animal_dict.keys() in column_keys]
        return jsonify(animal_dicts)
        
    
    @app.route('/animals/<id>')
    def show_animal(id):
        conn = psycopg2.connect(database = app.config['DATABASE'], user = app.config['DBUSER'], password = app.config['DBPASSWORD'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM animals WHERE local_id = %s', (id,))
        animal_response = cursor.fetchall()
        return Animal(animal_response).__dict__


    return app


