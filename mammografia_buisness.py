from base_buisness import BaseTable
from constant import DB_SCHEMA


class Mammografia(BaseTable):
    __tablename__ = "t_mammography"
    _FORMAT_KEY_ = ['type', 'result']

    def __init__(self, uuid=None, date_list=None, date_end=None, ambulatorio=None, azienda_sanitaria=None,
                 event_type=None, previous_invite=None, responded=None, send_via_sms=None, missed_appointment_date=None,
                 last_appointment_date=None, missed_appointment_info=None, sequential_number=None, data_pendenza=None,
                 alert_recall=None, contact_date=None, recapito_telefonico_casa=None,
                 recapito_telefonico_cellulare=None,contact_to=None, contact_from=None):
        super().__init__()

        self.uuid = uuid
        self.date_list = date_list
        self.date_end = date_end
        self.ambulatorio = ambulatorio
        self.event_type = event_type
        self.previous_invite = previous_invite
        self.responded = responded
        self.send_via_sms = send_via_sms
        self.azienda_sanitaria = azienda_sanitaria
        self.sequential_number = sequential_number
        self.data_pendenza = data_pendenza
        self.alert_recall = alert_recall
        self.contact_date = contact_date
        self.contact_to = contact_to
        self.contact_from = contact_from
        self.recapito_telefonico_casa = recapito_telefonico_casa
        self.recapito_telefonico_cellulare = recapito_telefonico_cellulare
        self.missed_appointment_date = missed_appointment_date
        self.last_appointment_date = last_appointment_date
        self.missed_appointment_info = missed_appointment_info

    def insert(self):
        self.creteField([])
        return f"""INSERT INTO {DB_SCHEMA}.{self.__tablename__}\n({self.columns})\nVALUES ({self.values});"""
