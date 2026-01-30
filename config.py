class Config:
    guest_num = 1000

    unique_attractions_num = 25     #unique because automatically for every real attraction there is generated also one more vr attraction 
    min_attraction_built_year = 2000
    max_attraction_built_year = 2020
    adjectives_for_attractions_names = [
    "Wild", "Extreme", "Mighty", "Dark", "Golden", "Frozen", "Hidden", "Lost",
    "Epic", "Silent", "Rapid", "Furious", "Electric", "Infinite", "Savage",
    "Ancient", "Mystic", "Secret", "Burning", "Stormy", "Twisted", "Flying",
    "Raging", "Phantom", "Shadowy", "Crimson", "Icy", "Blazing", "Roaring",
    "Iron", "Steel", "Cosmic", "Brave", "Legendary", "Massive", "Rapid",
    "Glorious", "Savage", "Broken", "Cursed", "Haunted", "Thunderous",
    "Shattered", "Celestial", "Solar", "Lunar", "Obsidian", "Vicious",
    "Feral", "Grim", "Fearless", "Endless", "Savage", "Frozen", "Infernal",
    "Vortex", "Turbo", "Steep", "Colossal", "Whispering", "Shining",
    "Ruthless", "Chaotic", "Hidden", "Final", "Eternal", "Reckless",
    "Electric", "Stormborn", "Gravity", "Dangerous", "Unholy", "Sacred",
    "Swift", "Midnight", "Neon", "Blinding", "Titanic", "Merciless",
    "Savage", "Radiant", "Volcanic", "Astral", "Darkened", "Savage"
]
    nouns_for_attractions_names = [
    "Ride", "Coaster", "Drop", "Fall", "Storm", "Fury", "Twister", "Loop",
    "Tunnel", "Track", "Cliff", "Spiral", "Rush", "Edge", "Peak", "Plunge",
    "Vortex", "Flight", "Rocket", "Tower", "Canyon", "Wave", "Inferno",
    "Maze", "Labyrinth", "Cyclone", "Whirl", "Beast", "Dragon", "Phantom",
    "Shadow", "Blade", "Machine", "Engine", "Pulse", "Strike", "Force",
    "Velocity", "Gravity", "Orbit", "Galaxy", "Void", "Abyss", "Rift",
    "Crash", "Surge", "Breaker", "Thunder", "Rampage", "Fallout", "Zone",
    "Core", "Sector", "Gate", "Portal", "Chasm", "Reactor", "Spike",
    "Dash", "Rush", "Claw", "Fang", "Howl", "Roar", "Skull", "Ember",
    "Ash", "Flame", "Spark", "Volt", "Stormfront", "Dropzone", "Summit",
    "Drift", "Vault", "Pit", "Track", "Crossing", "Run", "Strike"
]

    max_payments_per_guest = 6
    weights_for_payments = [0.2, 0.3, 0.2, 0.2, 0.1]
    open_hour = 9
    closure_hour = 18

    names_for_incident_types = [
        "Mechanical failure",
        "Electrical malfunction",
        "Software system error",
        "Operator mistake",
        "Safety system failure",
        "Fire hazard",
        "Power outage",
        "Minor equipment damage",
        "Structural instability",
        "Emergency evacuation"
        ]
    risks_of_incident_types = [5, 4, 3, 3, 5, 5, 2, 1, 4, 5]

    incidents_num = 50

    insurance_names = ["full insurance", "full children insurance", "partial insurance", "partial children insurance", "senior insurance"]
    insurance_amounts = [100000, 150000, 50000, 75000, 150000]
    children_id_list = [2,4]
    adult_id_list = [1,3]
    senior_id_list = [5]

    min_salary = 5000
    max_salary = 7000
    number_of_months = 6
    workers_num_per_attraction = 1

    min_month_costs = 20000
    max_month_costs = 30000

    possible_malfunctions_per_attraction = 3
    min_fix_cost = 2000
    max_fix_cost = 20000
    max_days_to_fix = 30

    inspections_num = 200
    possible_inspection_results = ["No problems found", "There is possible malfunction"]

config = Config()