
    url = graphene.List(Url)

    def resolve_url(parent, info):
        recorte={'width':None,'height':None,'format':None,'regenerate':None}
        for argument in info.operation.selection_set.selections[0].arguments:
            if argument.name.value in recorte:
                recorte[argument.name.value]=argument.value.value

        return [Url(parent,recorte)]