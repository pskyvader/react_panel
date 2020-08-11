
    FIELD=all_image
    def resolve_FIELD(self,info, **kwargs):
        return resolve_all_image(self,info,table_name='TABLENAME',idparent=self.idTABLENAME,field_name='FIELD',**kwargs)
