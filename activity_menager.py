import random
import string

from activity_buisness import Activity
from cervice_buisness import Cervice
from constant import FALSE_VALUE, RESULT_NEW, cervice_result_close, \
    cervice_result_open, LIST_AMBULATORI, mammografia_result_close, spostamento_result_close, mammografia_result_open, \
    spostamento_result_open, CERVICE_CAMPAIGN_UUID, MAMMO_CAMPAIGN_UUID, SPOSTAMENTO_CAMPAIGN_UUID, UUID_IMPORT_CERV, \
    UUID_IMPORT_MAMM, UUID_IMPORT_SPOSTAMENTO, GROUP_1_UUID, EXECUTER, TRUE_VALUE
from mammografia_buisness import Mammografia
from spostamento_buisness import SpostamentoVaccino
from utils import getUUID, getDate, randomChoice, get_azienda_sanitaria



def mapping_result(activityType, close=False):
    if close:
        result = {"cervice": cervice_result_close, "mammografia": mammografia_result_close,
                  "spostamento": spostamento_result_close}
    else:
        result = {"cervice": cervice_result_open, "mammografia": mammografia_result_open,
                  "spostamento": spostamento_result_open}

    return result.get(activityType)


def result_manager(avtivityType, i, size, close=True, result=None, prev_result=None):
    closeR = list(mapping_result(avtivityType).keys())
    openR = list(mapping_result(avtivityType, True).keys())
    activity_executer = None
    if i == 0:
        prev_result = RESULT_NEW
        result = None if not close else randomChoice(closeR) if i != size else randomChoice(openR)
    else:
        prev_result = result
        result = randomChoice(closeR) if i == size else randomChoice(openR)

        activity_executer = EXECUTER if result else None

    return {"result": result, "previous_result": prev_result, "executer": activity_executer}


def parent_activity_manager(i, activity_uuid=None, parent_uuid=None):
    if i == 0:
        activity_uuid = getUUID()
    else:
        parent_uuid = activity_uuid
        activity_uuid = getUUID()

    return {"activity_uuid": activity_uuid, "parent_uuid": parent_uuid}


def campaign_mapper(avtivityType):
    campaign_uuid=None
    uuid_import=None
    type=None
    if avtivityType == 'cervice':
        campaign_uuid=CERVICE_CAMPAIGN_UUID
        type="CERVMAMM"
        uuid_import=UUID_IMPORT_CERV
    elif avtivityType == 'mammografia':
        campaign_uuid=MAMMO_CAMPAIGN_UUID
        type = "MAMMOGRAPHY"
        uuid_import = UUID_IMPORT_MAMM
    elif avtivityType == 'spostamento':
        campaign_uuid=SPOSTAMENTO_CAMPAIGN_UUID
        type = "SPOSTAMENTO_VACCINO"
        uuid_import = UUID_IMPORT_SPOSTAMENTO

    return {"campaign_uuid": campaign_uuid, "type": type, "uuid_import": uuid_import}

def random_string(letter_count=3, digit_count=3):
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))
    sam_list = list(str1)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string


def create_cervice(uuidAct, ambulatorio, seqNum):
    return Cervice(uuid=uuidAct,
                   date_list=getDate(-27),
                   event_type="appuntamento",
                   ambulatorio=ambulatorio,
                   responded=FALSE_VALUE,
                   alert_recall=FALSE_VALUE,
                   azienda_sanitaria=get_azienda_sanitaria(ambulatorio),
                   sequential_number=seqNum,
                   recapito_telefonico_casa="040235689 041256489",
                   recapito_telefonico_cellulare="3294658784")


def create_mammografia(uuidAct, ambulatorio, seqNum):
    return Mammografia(uuid=uuidAct,
                       ambulatorio=ambulatorio,
                       sequential_number=seqNum,
                       recapito_telefonico_cellulare="438256598",
                       recapito_telefonico_casa="3485678945",
                       azienda_sanitaria=get_azienda_sanitaria(ambulatorio),
                       date_list=getDate(-27),
                       responded=FALSE_VALUE,
                       alert_recall=FALSE_VALUE,
                       event_type="Appuntamento")


def create_spostamento(uuidAct, ambulatorio, seqNum=None):
    return SpostamentoVaccino(uuid=uuidAct,
                              vaccino_prima_dose="pfizer",
                              data_prima_dose=getDate(-20, True),
                              created=getDate(-26),
                              id_esterno=random.randint(10000, 50000),
                              azienda_prima_dose=get_azienda_sanitaria(ambulatorio),
                              sede_seconda_dose_programmata=ambulatorio,
                              data_seconda_dose_programmata=getDate(15, True),
                              dettaglio_richiesta="P",
                              archived="No",
                              download_zip="Scarica",
                              codice_univoco_completamento=random_string(),
                              recapito_telefonico="041526598",
                              )


def activity_type_menager(activityType):
    result = {"cervice": create_cervice,
              "mammografia": create_mammografia,
              "spostamento": create_spostamento
              }
    return result.get(activityType)


def create_activity_sequence(num, activityType='cervice', close=True,  numAmbulatori=1, is_pemding=True, inbound=False):
    list_activity = list()
    for amb in range(numAmbulatori):
        ambulatorio = LIST_AMBULATORI[amb]
        prev_result = None
        result = None
        activity_uuid = None
        parent_uuid = None
        for seq_num in range(num):
            dictResult = result_manager(activityType, seq_num, num, close=close, result=result, prev_result=prev_result)
            dictActivityUuid = parent_activity_manager(seq_num, activity_uuid, parent_uuid)
            campaign_data = campaign_mapper(activityType)
            a = Activity(uuid=dictActivityUuid["activity_uuid"],
                         user_uuid=getUUID(),
                         insert_date=getDate(-26),
                         type=campaign_data["type"],
                         uuid_import=campaign_data["uuid_import"],
                         deleted=FALSE_VALUE,
                         inbound=TRUE_VALUE if inbound else FALSE_VALUE,
                         activity_executer=dictResult["executer"],
                         campaign_uuid=campaign_data["campaign_uuid"],
                         parent_uuid=dictActivityUuid["parent_uuid"],
                         previous_result=dictResult["previous_result"],
                         result=dictResult["result"],
                         operator_group_uuid=None if is_pemding else GROUP_1_UUID)

            activitySpecific = activity_type_menager(activityType)
            specific = activitySpecific(dictActivityUuid["activity_uuid"], ambulatorio, seq_num)
            list_activity.append(a)
            list_activity.append(specific)

    return list_activity

# lista = create_activity_sequence(1, close=True, activityType='cervice', numAmbulatori=1)
