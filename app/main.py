import utils
import read_csv
import charts


def run():
  data = read_csv.read_csv('./app/data.csv')
  
  Country = input('Type country => ')
  result = utils.population_by_country(data, Country)

  if len(result) > 0:
    Country = result[0]
    labels, values = utils.get_population(Country)
    charts.generate_pie_chart(labels, values)
  
  print(result)

if __name__ == '__main__':
  run()

  '''Este if dice que si es ejecutado desde la terminal, entre al run y si es ejecutado desde otro archivo, no se ejecuta.'''
  