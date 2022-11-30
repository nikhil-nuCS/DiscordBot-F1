import json
import os
from path import DATA_DIR, OUT_DIR
from discord import File


def load_drivers():
    """Load drivers JSON from file and return as dict."""
    with open(f'{DATA_DIR}/drivers.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        driver_data = data['MRData']['DriverTable']['Drivers']
        return driver_data


def save_figure(fig, path=OUT_DIR, name='plot.png'):
    """Save the figure as a file."""
    fig.savefig(os.path.join(path, name), bbox_inches='tight')


def load_figure(file_name):
    plot_file = File(f"{OUT_DIR}/{file_name}", filename=file_name)
    return plot_file


def load_track_layout(track):
    return CIRCUIT_LAYOUT[track]


def get_circuit_lap_number(track):
    return LAPS[track]


def get_circuit_length(track):
    return CIRCUIT_LENGTH[track]


DRIVERS = load_drivers()

CIRCUIT_LAYOUT = {
    "imola": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Emilia_Romagna_Circuit.png.transform/7col/image.png"
}

LAPS = {
    "imola": 63
}

CIRCUIT_LENGTH = {
    "imola": "4.909 km"
}