
    url = graphene.List(Url)

    def resolve_url(parent, info):
        from graph_ql.utils import image
        width=None
        heigth=None
        extension=None
        for argument in info.operation.selection_set.selections[0].arguments:
            if argument.name.value=='width':
                width=argument.value.value
            elif argument.name.value=='height':
                heigth=argument.value.value
            elif argument.name.value=='extension':
                extension=argument.value.value
                
        recorte={'width':width,'height':heigth,'extension':extension}
        return [Url(parent,recorte)]