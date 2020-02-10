
    FIELD=all_image

    def resolve_FIELD(parent,info, **kwargs):
        return resolve_all_image(parent,info,table_name='TABLENAME',idparent=parent.idTABLENAME,field_name='FIELD',**kwargs)