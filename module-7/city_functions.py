# Joshua Xiong / 11/26/2026 / Module 7.2 Assignment

def city_country(city, country, population=None, language=None):
    """Return 'City, Country', optionally with population and language."""
    formatted = f"{city.title()}, {country.title()}"
    if population:
        formatted += f" - population {population}"
    if language:
        formatted += f", {language.title()}"
    return formatted


if __name__ == "__main__":
    # City, Country
    print(city_country("santiago", "chile"))

    # City, Country, Population
    print(city_country("tokyo", "japan", 14000000))

    # City, Country, Population, Language
    print(city_country("nairobi", "kenya", 4400000, "swahili"))
