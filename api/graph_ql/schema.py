from .schemas import *
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField


class Query(graphene.ObjectType):
    node = relay.Node.Field()
# __QUERY__
    
    all_administrador = administrador_method.all_administrador
    resolve_all_administrador = administrador_method.resolve_all_administrador
    administrador = administrador_method.administrador
    resolve_administrador = administrador_method.resolve_administrador
    
    all_banner = banner_method.all_banner
    resolve_all_banner = banner_method.resolve_all_banner
    banner = banner_method.banner
    resolve_banner = banner_method.resolve_banner
    
    all_comuna = comuna_method.all_comuna
    resolve_all_comuna = comuna_method.resolve_all_comuna
    comuna = comuna_method.comuna
    resolve_comuna = comuna_method.resolve_comuna
    
    all_configuracion = configuracion_method.all_configuracion
    resolve_all_configuracion = configuracion_method.resolve_all_configuracion
    configuracion = configuracion_method.configuracion
    resolve_configuracion = configuracion_method.resolve_configuracion
    
    all_direccion = direccion_method.all_direccion
    resolve_all_direccion = direccion_method.resolve_all_direccion
    direccion = direccion_method.direccion
    resolve_direccion = direccion_method.resolve_direccion
    
    all_galeria = galeria_method.all_galeria
    resolve_all_galeria = galeria_method.resolve_all_galeria
    galeria = galeria_method.galeria
    resolve_galeria = galeria_method.resolve_galeria
    
    all_igaccounts = igaccounts_method.all_igaccounts
    resolve_all_igaccounts = igaccounts_method.resolve_all_igaccounts
    igaccounts = igaccounts_method.igaccounts
    resolve_igaccounts = igaccounts_method.resolve_igaccounts
    
    all_ighashtag = ighashtag_method.all_ighashtag
    resolve_all_ighashtag = ighashtag_method.resolve_all_ighashtag
    ighashtag = ighashtag_method.ighashtag
    resolve_ighashtag = ighashtag_method.resolve_ighashtag
    
    all_igtotal = igtotal_method.all_igtotal
    resolve_all_igtotal = igtotal_method.resolve_all_igtotal
    igtotal = igtotal_method.igtotal
    resolve_igtotal = igtotal_method.resolve_igtotal
    
    all_igusuario = igusuario_method.all_igusuario
    resolve_all_igusuario = igusuario_method.resolve_all_igusuario
    igusuario = igusuario_method.igusuario
    resolve_igusuario = igusuario_method.resolve_igusuario
    
    all_log = log_method.all_log
    resolve_all_log = log_method.resolve_all_log
    log = log_method.log
    resolve_log = log_method.resolve_log
    
    all_logo = logo_method.all_logo
    resolve_all_logo = logo_method.resolve_all_logo
    logo = logo_method.logo
    resolve_logo = logo_method.resolve_logo
    
    all_mediopago = mediopago_method.all_mediopago
    resolve_all_mediopago = mediopago_method.resolve_all_mediopago
    mediopago = mediopago_method.mediopago
    resolve_mediopago = mediopago_method.resolve_mediopago
    
    all_modulo = modulo_method.all_modulo
    resolve_all_modulo = modulo_method.resolve_all_modulo
    modulo = modulo_method.modulo
    resolve_modulo = modulo_method.resolve_modulo
    
    all_moduloconfiguracion = moduloconfiguracion_method.all_moduloconfiguracion
    resolve_all_moduloconfiguracion = moduloconfiguracion_method.resolve_all_moduloconfiguracion
    moduloconfiguracion = moduloconfiguracion_method.moduloconfiguracion
    resolve_moduloconfiguracion = moduloconfiguracion_method.resolve_moduloconfiguracion
    
    all_pedido = pedido_method.all_pedido
    resolve_all_pedido = pedido_method.resolve_all_pedido
    pedido = pedido_method.pedido
    resolve_pedido = pedido_method.resolve_pedido
    
    all_pedidodireccion = pedidodireccion_method.all_pedidodireccion
    resolve_all_pedidodireccion = pedidodireccion_method.resolve_all_pedidodireccion
    pedidodireccion = pedidodireccion_method.pedidodireccion
    resolve_pedidodireccion = pedidodireccion_method.resolve_pedidodireccion
    
    all_pedidoestado = pedidoestado_method.all_pedidoestado
    resolve_all_pedidoestado = pedidoestado_method.resolve_all_pedidoestado
    pedidoestado = pedidoestado_method.pedidoestado
    resolve_pedidoestado = pedidoestado_method.resolve_pedidoestado
    
    all_pedidoproducto = pedidoproducto_method.all_pedidoproducto
    resolve_all_pedidoproducto = pedidoproducto_method.resolve_all_pedidoproducto
    pedidoproducto = pedidoproducto_method.pedidoproducto
    resolve_pedidoproducto = pedidoproducto_method.resolve_pedidoproducto
    
    all_producto = producto_method.all_producto
    resolve_all_producto = producto_method.resolve_all_producto
    producto = producto_method.producto
    resolve_producto = producto_method.resolve_producto
    
    all_productocategoria = productocategoria_method.all_productocategoria
    resolve_all_productocategoria = productocategoria_method.resolve_all_productocategoria
    productocategoria = productocategoria_method.productocategoria
    resolve_productocategoria = productocategoria_method.resolve_productocategoria
    
    all_profile = profile_method.all_profile
    resolve_all_profile = profile_method.resolve_all_profile
    profile = profile_method.profile
    resolve_profile = profile_method.resolve_profile
    
    all_region = region_method.all_region
    resolve_all_region = region_method.resolve_all_region
    region = region_method.region
    resolve_region = region_method.resolve_region
    
    all_seccion = seccion_method.all_seccion
    resolve_all_seccion = seccion_method.resolve_all_seccion
    seccion = seccion_method.seccion
    resolve_seccion = seccion_method.resolve_seccion
    
    all_seccioncategoria = seccioncategoria_method.all_seccioncategoria
    resolve_all_seccioncategoria = seccioncategoria_method.resolve_all_seccioncategoria
    seccioncategoria = seccioncategoria_method.seccioncategoria
    resolve_seccioncategoria = seccioncategoria_method.resolve_seccioncategoria
    
    all_seo = seo_method.all_seo
    resolve_all_seo = seo_method.resolve_all_seo
    seo = seo_method.seo
    resolve_seo = seo_method.resolve_seo
    
    all_sitemap = sitemap_method.all_sitemap
    resolve_all_sitemap = sitemap_method.resolve_all_sitemap
    sitemap = sitemap_method.sitemap
    resolve_sitemap = sitemap_method.resolve_sitemap
    
    all_table = table_method.all_table
    resolve_all_table = table_method.resolve_all_table
    table = table_method.table
    resolve_table = table_method.resolve_table
    
    all_texto = texto_method.all_texto
    resolve_all_texto = texto_method.resolve_all_texto
    texto = texto_method.texto
    resolve_texto = texto_method.resolve_texto
    
    all_usuario = usuario_method.all_usuario
    resolve_all_usuario = usuario_method.resolve_all_usuario
    usuario = usuario_method.usuario
    resolve_usuario = usuario_method.resolve_usuario
    
    all_usuariodireccion = usuariodireccion_method.all_usuariodireccion
    resolve_all_usuariodireccion = usuariodireccion_method.resolve_all_usuariodireccion
    usuariodireccion = usuariodireccion_method.usuariodireccion
    resolve_usuariodireccion = usuariodireccion_method.resolve_usuariodireccion
    
# __QUERY__
    
    
    
class Mutation(graphene.ObjectType):
    pass
# __MUTATION__

    # createPerson = schema_people.CreatePerson.Field()
    # updatePerson = schema_people.UpdatePerson.Field()
    # createPlanet = schema_planet.CreatePlanet.Field()
    # updatePlanet = schema_planet.UpdatePlanet.Field()
    
# __MUTATION__
    
    

    
    
    
    
    
    
    
    
    

# __TYPES__
    
schema = graphene.Schema(query=Query, types=[administrador_method.administrador_schema,banner_method.banner_schema,comuna_method.comuna_schema,configuracion_method.configuracion_schema,direccion_method.direccion_schema,galeria_method.galeria_schema,igaccounts_method.igaccounts_schema,ighashtag_method.ighashtag_schema,igtotal_method.igtotal_schema,igusuario_method.igusuario_schema,log_method.log_schema,logo_method.logo_schema,mediopago_method.mediopago_schema,modulo_method.modulo_schema,moduloconfiguracion_method.moduloconfiguracion_schema,pedido_method.pedido_schema,pedidodireccion_method.pedidodireccion_schema,pedidoestado_method.pedidoestado_schema,pedidoproducto_method.pedidoproducto_schema,producto_method.producto_schema,productocategoria_method.productocategoria_schema,profile_method.profile_schema,region_method.region_schema,seccion_method.seccion_schema,seccioncategoria_method.seccioncategoria_schema,seo_method.seo_schema,sitemap_method.sitemap_schema,table_method.table_schema,texto_method.texto_schema,usuario_method.usuario_schema,usuariodireccion_method.usuariodireccion_schema,])
# __TYPES__
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    