from datetime import datetime

from base_buisness import BaseTable
from constant import DB_SCHEMA


class Activity(BaseTable):
    __tablename__ = "t_activity"
    _FORMAT_KEY_ = ['type', 'result']

    def __init__(self, uuid=None, user_uuid=None, type=None, activity_date=None, deleted=None, activity_executer=None,
                 completed_timestamp=None, parent_uuid=None,
                 uuid_import=None, data_presa_in_carico=None, operator_group_uuid=None, assign_date=None, inbound=None,
                 result=None, insert_date=None, previous_result=None, description=None, campaign_uuid=None,
                 did_create_followup=None):
        super().__init__()

        self.uuid = uuid
        self.user_uuid = user_uuid
        self.type = type
        self.activity_date = activity_date
        self.deleted = deleted
        self.activity_executer = activity_executer
        self.completed_timestamp = completed_timestamp
        self.parent_uuid = parent_uuid
        self.uuid_import = uuid_import
        self.data_presa_in_carico = data_presa_in_carico
        self.operator_group_uuid = operator_group_uuid
        self.assign_date = assign_date
        self.inbound = inbound
        self.result = result
        self.insert_date = insert_date
        self.previous_result = previous_result
        self.description = description
        self.campaign_uuid = campaign_uuid
        self.did_create_followup = did_create_followup

    def insert(self):
        self.creteField(self._FORMAT_KEY_)
        return f"""INSERT INTO {DB_SCHEMA}.{self.__tablename__}\n({self.columns})\nVALUES ({self.values});"""


# class Cervice(BaseTable):
#     __tablename__ = "t_cerv_mamm"
#     _FORMAT_KEY_ = ['type', 'result']
#
#     def __init__(self, uuid=None, date_list=None, date_end=None, ambulatorio=None, event_type=None,
#                  previous_invite=None, responded=None, send_via_sms=None, azienda_sanitaria=None,
#                  sequential_number=None, data_pendenza=None, alert_recall=None, contact_date=None,
#                  contact_to=None, contact_from=None, recapito_telefonico_casa=None, recapito_telefonico_cellulare=None):
#         super().__init__()
#
#         self.uuid = uuid
#         self.date_list = date_list
#         self.date_end = date_end
#         self.ambulatorio = ambulatorio
#         self.event_type = event_type
#         self.previous_invite = previous_invite
#         self.responded = responded
#         self.send_via_sms = send_via_sms
#         self.azienda_sanitaria = azienda_sanitaria
#         self.sequential_number = sequential_number
#         self.data_pendenza = data_pendenza
#         self.alert_recall = alert_recall
#         self.contact_date = contact_date
#         self.contact_to = contact_to
#         self.contact_from = contact_from
#         self.recapito_telefonico_casa = recapito_telefonico_casa
#         self.recapito_telefonico_cellulare = recapito_telefonico_cellulare
#
#     def insert(self):
#         self.creteField(self._FORMAT_KEY_)
#         return f"""INSERT INTO {DB_SCHEMA}.{self.__tablename__}\n({self.columns})\nVALUES ({self.values});"""

