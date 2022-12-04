from base_buisness import BaseTable

_DB_SHEMA__ = "tv_activities"

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
        return f"""INSERT INTO {_DB_SHEMA__}.{self.__tablename__}\n({self.columns})\nVALUES ({self.values});"""


