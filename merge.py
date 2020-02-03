import pandas as pd
import glob

path = r'/Users/diegofrade/PycharmProjects/cities_data'  # path
all_files = glob.glob(path + "/*.csv")
df_1 = pd.DataFrame()

cnaes = pd.read_csv('/Users/diegofrade/Documents/GitHub/CNPJ-full/PASTA_DE_SAIDA/cnaes_secundarios.csv', index_col=None, error_bad_lines=False)
cnaes = cnaes.iloc[:,[0,2]]
print(cnaes.columns)
cities = [
    'CARAPICUIBA',
    'OSASCO',
    'SANTANA DE PARNAIBA',
    'CAETE',
    'ALVORADA',
    'NOVO HAMBURGO',
    'SAO JOSE DE RIBAMAR',
    'ITAUNA',
    'CANOAS',
    'VESPASIANO',
    'ITABIRITO',
    'RIBEIRAO DAS NEVES',
    'SANTA RITA',
    'TABOAO DA SERRA',
    'VIAMAO',
    'SANTO ANDRE',
    'PACO DO LUMIAR',
    'IBIRITE',
    'SAO LUIS',
    'LAGOA SANTA',
    'SABARA',
    'CONTAGEM',
    'SANTA LUZIA',
    'BRASILIA',
    'BACABEIRA',
    'BRUMADINHO',
    'PARA DE MINAS',
    'ICATU',
    'CACHOEIRINHA',
    'EMBU DAS ARTES',
    'GUARULHOS',
    'SAO LEOPOLDO',
    'DIADEMA',
    'NOVA LIMA',
    'SETE LAGOAS',
    'MONTENEGRO',
    'BELO HORIZONTE',
    'PEDRO LEOPOLDO',
    'SAO CAETANO DO SUL',
    'ROSARIO',
    'GRAVATAI',
    'SAO BERNARDO DO CAMPO',
    'ALCANTARA',
    'BARUERI',
    'RAPOSA',
    'SAO PAULO',
    'BARAO DE COCAIS',
    'JANDIRA',
    'PORTO ALEGRE']



d = {}
i = -1
df_total = pd.DataFrame()
for filename in all_files:
    print(filename)
    i += 1
    print('Document:' + str(i))
    d["df_".format(i)] = pd.read_csv(filename, index_col=None, header=0, error_bad_lines=False,low_memory=False)
    print(cities[i])
    df_total = (d["df_".format(i)])
    print(len(df_total))
    df_total = pd.merge(df_total , cnaes , how='left', on=['cnpj', 'cnpj'])
    df_total.to_csv(str(cities[i]) + '.csv')
