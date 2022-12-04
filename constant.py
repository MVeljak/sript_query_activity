import uuid
from datetime import datetime, timedelta

FILE_NAME = "fileSql.txt"

ACTIVITY_NUMBER = 3

NULL_VALUE = 'null'
FALSE_VALUE = 'false'
TRUE_VALUE = 'true'


DATE_NOW = datetime.now()

RESULT_CLOSE = ('result_9', 'result_10', 'result_11', 'result_12', 'result_13', 'result_22', 'result_23', 'result_6',
                'result_7', 'result_8', 'result_14', 'result_15', 'result_16', 'result_17', 'result_18')

RESULT_OPEN = ('result_1', 'result_2', 'result_3', 'result_4', 'result_5', 'result_19', 'result_20', 'result_21')

RESULT_NEW = 'nuovo'

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
                   'ASUFC - MOGGIO C/O CENTRO ANZIANI', 'ASUFC - PALMANOVA OSPEDALE REPARTO GINECOLOGIA',
                   'ASUFC - PONTEBBA POLIAMBULATORIO', 'ASUFC - S.GIORGIO DI NOGARO CONSULTORIO'
                   'ASUFC - TARCENTO DISTRETTO SANITARIO', 'ASUFC - TOLMEZZO OSPEDALE',
                   'ASUFC - TRICESIMO AMBULATORIO', 'ASUFC - UDINE DISTRETTO SANITARIO - POLIAMBULATORI',
                   'ASUFC OSP.S.DANIELE AMB.PAP-TEST-VICINO PEDIATRIA',
                   'ASUFC-GEMONA OSPEDALE-AMB.GINECOLOGICO 3 P,SCALA D',
                   'ASUGI - DIST.SANIT.2 VIA PIETA\' - 2 PIANO ST.225',
                   'ASUGI - DISTRETTO N.3 MUGGIA  1 PIANO, ST.104',
                   'ASUGI - GORIZIA -EX OSPEDALE-CONSULTORIO FAMILIARE', 'ASUGI - MONFALCONE - CONSULTORIO FAMILIARE',
                   'ASUGI - SANATORIO TRIESTINO - 1 PIANO, ST. 129')

# DATE_IMPORT = (DATE_NOW - timedelta(hours=25))
# UUID_IMPORT_CERV = '83fa20be-3e95-4f2a-a982-fcf7176c2869'  # uuid.uuid4()
# UUID_IMPORT_MAMM = 'f261dbfe-0e45-4cf0-b6c3-7a5d22dfb022'  # uuid.uuid4()
# UUID_IMPORT_SPOSTAMENTO = '5a9741dc-47d6-44e5-ab2b-e30b87f08d89'  # uuid.uuid4()
# USER_UUID = uuid.uuid4()
# EXECUTER = '5e311e0f-b72d-4796-a03a-74f930adf890'  # uuid.uuid4()
# CERVICE_CAMPAIGN_UUID = 'e3d5eb7d-e176-4932-8142-dac69351c78f'  # uuid.uuid4() -> preso dai test
# MAMMO_CAMPAIGN_UUID = '65244678-190a-4713-9af0-a3ae6e2eee71'  # uuid.uuid4() -> preso dai test
# SPOSTAMENTO_CAMPAIGN_UUID = '03e4b15e-ef23-4be0-abc8-68ac54661378'  # uuid.uuid4() -> preso dai test
# DATE_INSERT = (DATE_NOW - timedelta(hours=26))
# _TYPE_ACTIVITY = 'CERVMAMM'