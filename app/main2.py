import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages) # la grafica de pastel
  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  

  data = read_csv.read_csv('data.csv')
  Country = input('Type country => ')
  print(Country)

  result = utils.population_by_country(data, Country)

  if len(result) > 0:
    Country = result[0]
    print(Country)
    labels, values = utils.get_population(Country)
    charts.generate_bar_chart(Country['Country'], labels, values) #Country sirve para generar el name de la imagenes puedes ver en charts
  
  print(result)

if __name__ == '__main__':
  run()