from base_buisness import BaseTable
from constant import DB_SCHEMA


class SpostamentoVaccino(BaseTable):
    __tablename__ = "t_spostamento_vaccino"
    _FORMAT_KEY_ = ['type', 'result']

    def __init__(self, uuid=None,id_esterno=None, modified=None,created=None,vaccino_prima_dose=None,
                 data_prima_dose=None,azienda_prima_dose=None,data_seconda_dose_programmata=None,
                 sede_seconda_dose_programmata=None, domanda=None, dettaglio_richiesta=None,
                 codice_univoco_completamento=None,datamin=None,datamax=None,motivo_trasferimento=None,
                 status=None,archived=None,user_exel=None,real_survey_responder=None,data_exel=None,
                 download_zip=None, motivo_spostamento_seconda_dose=None,recapito_telefonico=None):
        super().__init__()
        self.uuid = uuid
        self.id_esterno = id_esterno
        self.modified = modified
        self.created = created
        self.vaccino_prima_dose = vaccino_prima_dose
        self.data_prima_dose = data_prima_dose
        self.azienda_prima_dose = azienda_prima_dose
        self.data_seconda_dose_programmata = data_seconda_dose_programmata
        self.sede_seconda_dose_programmata = sede_seconda_dose_programmata
        self.domanda = domanda
        self.dettaglio_richiesta = dettaglio_richiesta
        self.codice_univoco_completamento = codice_univoco_completamento
        self.datamin = datamin
        self.datamax = datamax
        self.motivo_trasferimento = motivo_trasferimento
        self.status = status
        self.archived = archived
        self.user_exel = user_exel
        self.real_survey_responder = real_survey_responder
        self.data_exel = data_exel
        self.download_zip = download_zip
        self.motivo_spostamento_seconda_dose = motivo_spostamento_seconda_dose
        self.recapito_telefonico = recapito_telefonico

    def insert(self):
        self.creteField([])
        return f"""INSERT INTO {DB_SCHEMA}.{self.__tablename__}\n({self.columns})\nVALUES ({self.values});"""
