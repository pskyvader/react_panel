
    url = graphene.List(Url,width=graphene.String(), height=graphene.String(), format=graphene.String(), regenerate=graphene.Boolean())
    resolve_url=resolve_url_field