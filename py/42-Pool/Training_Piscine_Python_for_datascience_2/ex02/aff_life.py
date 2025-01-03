from load_csv import load
import matplotlib.pyplot as plt # type: ignore

def main():
    df = load('./../population_total.csv')
    
    countries = ['Belgium', 'France']
    # countries = ['Morocco', 'United States']

    plt.figure(figsize=(10, 6))

    for country in countries:
        if country in df['country'].values:
            country_data = df[df['country'] == country].iloc[0, 1:]
            
            years = country_data.index.astype(int)
            population = country_data.values
            
            plt.plot(years, population, label=country)
        else:
            print(f"Error: Country {country} not found in the dataset.")

    plt.title(f"population Projections")
    plt.xlabel("Year")
    # plt.ylim(min(df.iloc[:, 1:].min().min(), df.iloc[:, 1:].min().min()), max(df.iloc[:, 1:].max().max(), df.iloc[:, 1:].max().max()))
    # y_max, y_min = plt.ylim()
    # y_middle = (y_min + y_max) / 2
    # plt.yticks([y_max, y_middle, y_min])
    plt.yticks([100, 200, 300])
    plt.ylabel("population")
    plt.legend()
    # plt.grid(False)
    plt.show()

if __name__ == '__main__':
    main()