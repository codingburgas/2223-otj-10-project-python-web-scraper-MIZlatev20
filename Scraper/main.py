from pages import covid, weather, economy
import csv

file_path = "data/data.csv"
columns = ["Area", "Active cases", "Total vaccines", "Temperature", "Humidity", "Air Quality", "Unemployed"]

def create_new_file(file):
    with open(file, 'w') as f:
        f.write("")
    
def write_to_file(data):
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([column for column in columns])

        for j in range(len(data[0])):
            current = [data[i][j] for i in range(len(columns))]
            writer.writerow(current)

def main():
    create_new_file(file_path)

    data = [covid.areas]
    data.append(covid.get_new_cases())
    data.append(covid.get_vaccines())
    data.append(weather.get_temperatures())
    data.append(weather.get_humidities())
    data.append(weather.get_aq())
    data.append(economy.get_areas_unemployement())

    write_to_file(data)

if __name__ == "__main__":
    main()