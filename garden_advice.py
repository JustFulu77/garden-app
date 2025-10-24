def get_advice(season, plant_type):
    """
    Return gardening advice based on the given season and plant type.
    
    :param season: str - current season (e.g. 'summer', 'winter')
    :param plant_type: str - type of plant (e.g. 'flower', 'vegetable')
    :return: str - gardening advice
    """
    advice = ""

    # Advice based on season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"

    # Advice based on plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."

    return advice


def main():
    """Main function to get user input and display gardening advice."""
    season = input("Enter the current season (summer/winter/etc): ").strip().lower()
    plant_type = input("Enter the plant type (flower/vegetable/etc): ").strip().lower()
    advice = get_advice(season, plant_type)
    print("\nGardening Advice:\n" + advice)


# Entry point of the script
if __name__ == "__main__":
    main()
