import pandas as pd
import glob

path = r'/Users/diegofrade/PycharmProjects/cities_nnpj'  # path
all_files = glob.glob(path + "/*.csv")
df_1 = pd.DataFrame()

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
    print('Document:  ' + str(i))
    d["df_".format(i)] = pd.read_csv(filename, index_col=None, header=0, error_bad_lines=False,low_memory=False)
    df_total = (d["df_".format(i)])
    print('First length: ' + str(len(df_total)))
    df_total = df_total.loc[df_total['opc_mei'] == 'S']
    print('Processing............')
    print('Second length: ' + str(len(df_total)))
    print('Distinct values for opc imei: ' + str(df_total.opc_mei.unique()))
    print(df_total.head())
    df_total.to_csv(str(all_files[i][:-4]) + '_imei.csv',index=False)













