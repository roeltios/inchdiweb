from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

usos = ["PLASTIC BAGS", "PLASTIC CUPS", "PAPER PLATES", "POPSICKLE STICKS", "LIGAS", "CARDBOARD"]
objetos = ["MUSICAL INSTRUMENT", "BOAT", "SHELTER", "MOUSTRAP", "CARNIVAL RIDE", "TOWER"]
propósitos = ["MAKE NOISE", "FLYE", "DANCE", "MAKE EVERYONE LAUG", "HOLD A TENNIS BALL", "BREAK INTO 4 PIECES"]
locations = [
    "Hogwarts", "Tokyo", "Grand Canyon", "Atlantis", "Narnia", 
    "Eiffel Tower", "Amazon Rainforest", "Venice", "Gotham City", "Blue Lagoon"
]

seekers = [
    "Captain Zeta", "The Glitter Wizard", "Detective Noodle", "Professor Peanut", 
    "Zara the Robot Queen", "Billy Banana", "Echo the Time Jumper", "The Dancing Witch", 
    "Agent Pickle", "Nimbus the Dreamer"
]

transport_modes = [
    "Bicycle", "Submarine", "Hot Air Balloon", "Spaceship", "Horse", 
    "The Flying Carpet from 1,001 Arabian Nights", "Pegasus", "Magic School Bus", 
    "Roller Skates", "Floating Bubble"
]

detours = [
    "a haunted talent show", "an alien karaoke challenge", 
    "a backwards-talking forest", "a riddle battle with a swamp troll", 
    "a surprise dance-off", "a sudden sleep spell", 
    "a thunderstorm made of glitter", "a time loop", 
    "a giant pancake avalanche", "a talking map with attitude"
]



@app.route('/api/reto', methods=['GET'])
def generar_reto():
    uso = random.choice(usos)
    objeto = random.choice(objetos)
    proposito = random.choice(propósitos)
    reto = f"Use {uso} to make a {objeto} that will {proposito}."
    return jsonify(reto=reto)

@app.route('/api/performance', methods=['GET'])
def generate_performance_challenge():
    start = random.choice(locations)
    end = random.choice([loc for loc in locations if loc != start])
    seeker = random.choice(seekers)
    transport = random.choice(transport_modes)
    detour = random.choice(detours)

    challenge = (
        f"Your seeker, '{seeker}', must travel from {start} to {end} using {transport} — "
        f"but beware: there’s {detour} in the middle of the journey!"
    )
    return jsonify(challenge=challenge)

if __name__ == '__main__':
    app.run(debug=True)
