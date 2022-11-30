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
    "bahrain": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Bahrain_Circuit.png.transform/7col-retina/image.png"
    "adelaide": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Australia_Circuit.png.transform/7col-retina/image.png"
    "indianapolis": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Miami_Circuit.png.transform/7col-retina/image.png"
    "catalunya": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Spain_Circuit.png.transform/7col-retina/image.png"
    "monaco": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Monoco_Circuit.png.transform/7col-retina/image.png"
    "jeddah": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Saudi_Arabia_Circuit.png.transform/7col-retina/image.png"
    "baku": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Baku_Circuit.png.transform/7col-retina/image.png"
    "mosport": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Canada_Circuit.png.transform/7col-retina/image.png"
    "silverstone": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Great_Britain_Circuit.png.transform/7col-retina/image.png"
    "red_bull_ring": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Austria_Circuit.png.transform/7col-retina/image.png"
    "reims": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/France_Circuit.png.transform/7col-retina/image.png"
    "hungaroring": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Hungary_Circuit.png.transform/7col-retina/image.png"
    "nivelles": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Belgium_Circuit.png.transform/7col-retina/image.png"
    "zandvoort": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Netherlands_Circuit.png.transform/7col-retina/image.png"
    "monza": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Italy_Circuit.png.transform/7col-retina/image.png"
    "marina_bay": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Singapore_Circuit.png.transform/7col-retina/image.png"
    "okayama": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Japan_Circuit.png.transform/7col-retina/image.png"
    "americas": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/USA_Circuit.png.transform/7col-retina/image.png"
    "miami": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Miami_Circuit.png.transform/7col-retina/image.png"
    "rodriguez": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Mexico_Circuit.png.transform/7col-retina/image.png"
    "interlagos": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Brazil_Circuit.png.transform/7col-retina/image.png"
    "yas_marina": "https://www.formula1.com/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Abu_Dhabi_Circuit.png.transform/7col-retina/image.png"
}

LAPS = {
    "imola": 63,
    "bahrain": 57,
    "adelaide": 58,
    "indianapolis": 57,
    "catalunya": 66,
    "monaco": 78,
    "jeddah": 50,
    "baku": 51,
    "mosport": 70,
    "silverstone": 52,
    "red_bull_ring": 71,
    "reims": 53,
    "hungaroring": 70,
    "nivelles": 44,
    "zandvoort": 72,
    "monza": 53,
    "marina_bay": 61,
    "okayama": 53,
    "americas": 56,
    "miami": 57,
    "rodriguez": 71,
    "interlagos": 71,
    "yas_marina": 58
}

CIRCUIT_LENGTH = {
    "imola": "4.909 km"
    "bahrain": "5.412km"
    "adelaide": "5.278km"
    "indianapolis": "5.412km"
    "catalunya": "4.675km"
    "monaco": "3.337km"
    "jeddah": "6.174km"
    "baku": "6.003km"
    "mosport": "4.361km"
    "silverstone": "5.891km"
    "red_bull_ring": "4.318km"
    "reims": "5.842km"
    "hungaroring": "4.381km"
    "nivelles": "7.004km"
    "zandvoort": "4.259km"
    "monza": "5.793km"
    "marina_bay": "5.063km"
    "okayama": "5.807km"
    "americas": "5.513km"
    "miami": "5.412km"
    "rodriguez": "4.304km"
    "interlagos": "4.309km"
    "yas_marina": "5.281km"
}
