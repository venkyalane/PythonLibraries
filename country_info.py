from countryinfo import CountryInfo

country = CountryInfo(input("Enter country name: "))

print("Country name: ",country.name())
print("Country capital: ",country.capital())
print("Country population: ",country.population())
print("Country area: ",country.area())
print("Country region: ",country.region())
print("Country subregion: ",country.subregion())
print("Country demonym: ",country.demonym())
print("Country currencies: ",country.currencies())
print("Country languages: ",country.languages())
print("Country borders: ",country.borders())
print(country.info())
print(country.timezones())
print(country.wiki())