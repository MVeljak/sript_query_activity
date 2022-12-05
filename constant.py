import uuid
from datetime import datetime, timedelta

FILE_NAME = "fileSql.txt"

ACTIVITY_NUMBER = 3

NULL_VALUE = 'null'
FALSE_VALUE = 'false'
TRUE_VALUE = 'true'

DATE_NOW = datetime.now()

RESULT_NEW = 'nuovo'

DB_SCHEMA = "tv_activities"

LIST_AMBULATORI = ('ASFO - AZZANO DECIMO CONSULTORIO FAMILIARE',
                   'ASFO - MANIAGO CONSULTORIO FAM. C/O OSPEDALE',
                   'ASFO - PORDENONE CONSULTORIO FAMILIARE',
                   'ASFO - S.VITO AL T. CONSULTORIO F.AMB.A',
                   'ASFO - SACILE CONSULTORIO FAM  PAD. RUFFO 1 PIANO',
                   'ASFO - SPILIMBERGO CONSULTORIO FAM. C/O OSPEDALE',
                   'ASUFC - CERVIGNANO POLIAMBULATORIO I PIANO',
                   'ASUFC - CIVIDALE DEL FR. DISTRETTO SANITARIO',
                   'ASUFC - CODROIPO  DISTRETTO SANITARIO',
                   'ASUFC - FELETTO UMBERTO AMBULATORIO',
                   'ASUFC - LATISANA CONSULTORIO FAMILIARE - 2 PIANO',
                   'ASUFC - MANZANO AMBULATORIO',
                   'ASUFC - MOGGIO C/O CENTRO ANZIANI',
                   'ASUFC - PALMANOVA OSPEDALE REPARTO GINECOLOGIA',
                   'ASUFC - PONTEBBA POLIAMBULATORIO',
                   'ASUFC - S.GIORGIO DI NOGARO CONSULTORIO',
                    'ASUFC - TARCENTO DISTRETTO SANITARIO',
                   'ASUFC - TOLMEZZO OSPEDALE',
                   'ASUFC - TRICESIMO AMBULATORIO',
                   'ASUFC - UDINE DISTRETTO SANITARIO - POLIAMBULATORI',
                   'ASUFC OSP.S.DANIELE AMB.PAP-TEST-VICINO PEDIATRIA',
                   'ASUFC-GEMONA OSPEDALE-AMB.GINECOLOGICO 3 P,SCALA D',
                   'ASUGI - DIST.SANIT.2 VIA PIETA\' - 2 PIANO ST.225',
                   'ASUGI - DISTRETTO N.3 MUGGIA  1 PIANO, ST.104',
                   'ASUGI - GORIZIA -EX OSPEDALE-CONSULTORIO FAMILIARE',
                   'ASUGI - MONFALCONE - CONSULTORIO FAMILIARE',
                   'ASUGI - SANATORIO TRIESTINO - 1 PIANO, ST. 129')

# DATE_IMPORT = (DATE_NOW - timedelta(hours=25))
UUID_IMPORT_CERV = '83fa20be-3e95-4f2a-a982-fcf7176c2869'  # uuid.uuid4()
UUID_IMPORT_MAMM = 'f261dbfe-0e45-4cf0-b6c3-7a5d22dfb022'  # uuid.uuid4()
UUID_IMPORT_SPOSTAMENTO = '5a9741dc-47d6-44e5-ab2b-e30b87f08d89'  # uuid.uuid4()
# USER_UUID = uuid.uuid4()
EXECUTER = '5e311e0f-b72d-4796-a03a-74f930adf890'  # uuid.uuid4()
CERVICE_CAMPAIGN_UUID = 'e3d5eb7d-e176-4932-8142-dac69351c78f'  # uuid.uuid4() -> preso dai test
MAMMO_CAMPAIGN_UUID = '65244678-190a-4713-9af0-a3ae6e2eee71'  # uuid.uuid4() -> preso dai test
SPOSTAMENTO_CAMPAIGN_UUID = '03e4b15e-ef23-4be0-abc8-68ac54661378'  # uuid.uuid4() -> preso dai test

GROUP_1_UUID = "dc507ab4-7077-4537-b61a-bd8df2ac82e6"
GROUP_2_UUID = "b6ba4d0b-974e-43f8-a389-2c25eba6c206"


cervice_result_close = {"result_1": "Aderente",
                        "result_2": "Autonomo Percorso",
                        "result_3": "Effettuata MMX a meno di 1 anno",
                        "result_4": "Non aderente",
                        "result_9": "Tentativo 4",
                        "result_10": "Tentativo 5",
                        "result_11": "Tentativo 6",
                        "result_12": "Nessun numero INSIEL né CUPWEB",
                        "result_13": "La donna non deambula/non sta in piedi",
                        "result_21": "Numero inesistente 3",
                        "result_22": "Persona estranea",
                        "result_23": "Non acconsente a trattamento dati",
                        "nuovo": "Nuovo",
                        "scheda_duplicata": "Scheda duplicata"}

cervice_result_open = {"result_5": "Da ricontattare CR",
                       "result_6": "Tentativo 1",
                       "result_7": "Tentativo 2",
                       "result_8": "Tentativo 3",
                       "result_14": "Chiede altro periodo (agenda ancora chiusa)",
                       "result_15": "Chiede altra sede (agenda ancora chiusa)",
                       "result_16": "Presenta sintomi COVID",
                       "result_17": "In quarantena per COVID",
                       "result_18": "Positiva Covid",
                       "result_19": "Numero inesistente 1",
                       "result_20": "Numero inesistente 2"}

mammografia_result_close = {"result_1": "Aderente",
                            "result_2": "Autonomo Percorso",
                            "result_3": "Effettuata MMX a meno di 1 anno",
                            "result_4": "Non aderente",
                            "result_9": "Tentativo 4",
                            "result_10": "Tentativo 5",
                            "result_11": "Tentativo 6",
                            "result_12": "Nessun numero INSIEL né CUPWEB",
                            "result_13": "La donna non deambula/non sta in piedi",
                            "result_21": "Numero inesistente 3",
                            "result_22": "Persona estranea",
                            "result_23": "Non acconsente a trattamento dati",
                            "nuovo": "Nuovo",
                            "scheda_duplicata": "Scheda duplicata"}

mammografia_result_open = {"result_5": "Da ricontattare CR",
                           "result_6": "Tentativo 1",
                           "result_7": "Tentativo 2",
                           "result_8": "Tentativo 3",
                           "result_14": "Chiede altro periodo (agenda ancora chiusa)",
                           "result_15": "Chiede altra sede (agenda ancora chiusa)",
                           "result_16": "Presenta sintomi COVID",
                           "result_17": "In quarantena per COVID",
                           "result_18": "Positiva Covid",
                           "result_19": "Numero inesistente 1",
                           "result_20": "Numero inesistente 2"}

spostamento_result_open = {"move_try_1": "Non risponde tentativo 1",
                           "move_try_2": "Non risponde tentativo 2"}

spostamento_result_close = {"move_1": "Effettuato spostamento anticipo",
                            "move_2": "Effettuato spostamento posticipo",
                            "move_3": "Effettuato spostamento sede",
                            "move_4": "Non più interessato allo spostamento",
                            "move_done_1": "Già effettuato spostamento Azienda sanitaria",
                            "move_done_2": "Già effettuato spostamento call center",
                            "move_wrong_num": "Numero errato/inesistente",
                            "move_try_3": "Non risponde tentativo 3",
                            "move_trasf": "Trasferito al Dip. di Prevenzione",
                            "duplicate": "Utente doppiato",
                            "imp_move_try_1": "Import primo tentativo",
                            "imp_move_try_2": "Import secondo tentativo",
                            "nuovo": "Nuovo"}
