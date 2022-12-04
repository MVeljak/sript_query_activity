from activity_buisness import Activity
import random
import uuid
from datetime import datetime, timedelta

from constant import DATE_NOW, FALSE_VALUE

DATE_IMPORT = (DATE_NOW - timedelta(hours=25))
UUID_IMPORT_CERV = '83fa20be-3e95-4f2a-a982-fcf7176c2869'  # uuid.uuid4()
USER_UUID = uuid.uuid4()
EXECUTER = '5e311e0f-b72d-4796-a03a-74f930adf890'  # uuid.uuid4()
CERVICE_CAMPAIGN_UUID = 'e3d5eb7d-e176-4932-8142-dac69351c78f'  # uuid.uuid4() -> preso dai test
DATE_INSERT = (DATE_NOW - timedelta(hours=26))
_TYPE_ACTIVITY = 'CERVMAMM'

# _TYPE_ACTIVITY = 'CERVMAMM'
# for SEQUENTIAL_NUMBER in range(num):
#     # setto l'uuid activity
#     if SEQUENTIAL_NUMBER == 0:
#         # Il primo non ha parent
#         ACTIVITY_UUID = uuid.uuid4()
#         ACTIVITY_UUID_PARENT = 'null'
#         RESULT = LIST_RESULT[16]  # result_6 - tentativo_1
#         PREVIOUS_RESULT = 'nuovo'
#     else:
#         ACTIVITY_UUID_PARENT = ACTIVITY_UUID
#         ACTIVITY_UUID = uuid.uuid4()
#         PREVIOUS_RESULT = RESULT
#         RESULT = random.choice(LIST_RESULT)


def result_manager(i, size, close=True):
    if i == 0:
        pass
    elif i == size:
        pass
    else:
        pass




def create_activity__new(num):
    list_activity = list()
    for seq_num in range(num):
        activity_uuid = uuid.uuid4()
        list_activity.append(Activity(uuid=activity_uuid, user_uuid=USER_UUID, insert_date=DATE_INSERT,
                                      type=_TYPE_ACTIVITY, uuid_import=UUID_IMPORT_CERV,deleted=FALSE_VALUE,
                                      activity_executer=EXECUTER, campaign_uuid=CERVICE_CAMPAIGN_UUID,
                                      previous_result='nuovo'))

    for act in list_activity:
        print(act.insert())

