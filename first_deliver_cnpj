import pandas as pd
import glob

path = r'/Users/diegofrade/Documents/GitHub/CNPJ-full/first_deliver_dataplor'  # path
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
    i += 1
    print('Document:' + str(i))
    d["df_".format(i)] = pd.read_csv(filename, index_col=None, header=0, error_bad_lines=False,low_memory=False)
    d["df_".format(i)] = d["df_".format(i)].iloc[:,0:38]
    print(cities[i])
    d["df_".format(i)]['city'] = cities[i]
    df_total = (d["df_".format(i)])
    print(len(df_total))

    df_total.columns = [ 'cnpj','matriz_filial','razao_social','nome_fantasia','situacao','data_situacao','motivo_situacao',
                        'nm_cidade_exterior','cod_pais','nome_pais','cod_nat_juridica','data_inicio_ativ','cnae_fiscal',
                          'tipo_logradouro','logradouro','numero','complemento','bairro','cep','uf','cod_municipio',
                            'municipio','ddd_1','telefone_1','ddd_2','telefone_2','ddd_fax','num_fax','email',
                              'qualif_resp','capital_social','porte','opc_simples','data_opc_simples','data_exc_simples',
                                'opc_mei','sit_especial','data_sit_especial','city']
    df_total.to_csv(str(cities[i]) + '.csv')
