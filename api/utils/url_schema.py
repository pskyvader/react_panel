
    url = graphene.String()

    def resolve_url(parent, info):
        width=None
        heigth=None
        for argument in info.operation.selection_set.selections[0].arguments:
            if argument.name.value=='width':
                width=argument.value.value
            elif argument.name.value=='height':
                heigth=argument.value.value

        if parent.table_name != None and parent.idparent != None:
            if width!=None or heigth!=None:
                if width==None:
                    width=0
                if heigth==None:
                    heigth=0
                parent.name=f"{width}x{heigth}"
            return f"{parent.table_name}/{parent.idparent}/{parent.idimage}/{parent.name}{parent.extension}"
        else:
            return f"tmp/{parent.idimage}/{parent.name}{parent.extension}"
            