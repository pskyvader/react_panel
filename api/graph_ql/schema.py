from .schemas import *
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField


import sys, inspect
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
print(clsmembers)

print(sys.modules)

class Query(graphene.ObjectType):
    node = relay.Node.Field()
# __QUERY__
    
    all_administrador = administrador_schema.all_administrador
    resolve_all_administrador = administrador_schema.resolve_all_administrador
    administrador = administrador_schema.administrador
    resolve_administrador = administrador_schema.resolve_administrador
    
    all_banner = banner_schema.all_banner
    resolve_all_banner = banner_schema.resolve_all_banner
    banner = banner_schema.banner
    resolve_banner = banner_schema.resolve_banner
    
    all_comuna = comuna_schema.all_comuna
    resolve_all_comuna = comuna_schema.resolve_all_comuna
    comuna = comuna_schema.comuna
    resolve_comuna = comuna_schema.resolve_comuna
    
    all_configuracion = configuracion_schema.all_configuracion
    resolve_all_configuracion = configuracion_schema.resolve_all_configuracion
    configuracion = configuracion_schema.configuracion
    resolve_configuracion = configuracion_schema.resolve_configuracion
    
    all_direccion = direccion_schema.all_direccion
    resolve_all_direccion = direccion_schema.resolve_all_direccion
    direccion = direccion_schema.direccion
    resolve_direccion = direccion_schema.resolve_direccion
    
    all_galeria = galeria_schema.all_galeria
    resolve_all_galeria = galeria_schema.resolve_all_galeria
    galeria = galeria_schema.galeria
    resolve_galeria = galeria_schema.resolve_galeria
    
    all_igaccounts = igaccounts_schema.all_igaccounts
    resolve_all_igaccounts = igaccounts_schema.resolve_all_igaccounts
    igaccounts = igaccounts_schema.igaccounts
    resolve_igaccounts = igaccounts_schema.resolve_igaccounts
    
    all_ighashtag = ighashtag_schema.all_ighashtag
    resolve_all_ighashtag = ighashtag_schema.resolve_all_ighashtag
    ighashtag = ighashtag_schema.ighashtag
    resolve_ighashtag = ighashtag_schema.resolve_ighashtag
    
    all_igtotal = igtotal_schema.all_igtotal
    resolve_all_igtotal = igtotal_schema.resolve_all_igtotal
    igtotal = igtotal_schema.igtotal
    resolve_igtotal = igtotal_schema.resolve_igtotal
    
    all_igusuario = igusuario_schema.all_igusuario
    resolve_all_igusuario = igusuario_schema.resolve_all_igusuario
    igusuario = igusuario_schema.igusuario
    resolve_igusuario = igusuario_schema.resolve_igusuario
    
    all_log = log_schema.all_log
    resolve_all_log = log_schema.resolve_all_log
    log = log_schema.log
    resolve_log = log_schema.resolve_log
    
    all_logo = logo_schema.all_logo
    resolve_all_logo = logo_schema.resolve_all_logo
    logo = logo_schema.logo
    resolve_logo = logo_schema.resolve_logo
    
    all_mediopago = mediopago_schema.all_mediopago
    resolve_all_mediopago = mediopago_schema.resolve_all_mediopago
    mediopago = mediopago_schema.mediopago
    resolve_mediopago = mediopago_schema.resolve_mediopago
    
    all_modulo = modulo_schema.all_modulo
    resolve_all_modulo = modulo_schema.resolve_all_modulo
    modulo = modulo_schema.modulo
    resolve_modulo = modulo_schema.resolve_modulo
    
    all_moduloconfiguracion = moduloconfiguracion_schema.all_moduloconfiguracion
    resolve_all_moduloconfiguracion = moduloconfiguracion_schema.resolve_all_moduloconfiguracion
    moduloconfiguracion = moduloconfiguracion_schema.moduloconfiguracion
    resolve_moduloconfiguracion = moduloconfiguracion_schema.resolve_moduloconfiguracion
    
    all_pedido = pedido_schema.all_pedido
    resolve_all_pedido = pedido_schema.resolve_all_pedido
    pedido = pedido_schema.pedido
    resolve_pedido = pedido_schema.resolve_pedido
    
    all_pedidodireccion = pedidodireccion_schema.all_pedidodireccion
    resolve_all_pedidodireccion = pedidodireccion_schema.resolve_all_pedidodireccion
    pedidodireccion = pedidodireccion_schema.pedidodireccion
    resolve_pedidodireccion = pedidodireccion_schema.resolve_pedidodireccion
    
    all_pedidoestado = pedidoestado_schema.all_pedidoestado
    resolve_all_pedidoestado = pedidoestado_schema.resolve_all_pedidoestado
    pedidoestado = pedidoestado_schema.pedidoestado
    resolve_pedidoestado = pedidoestado_schema.resolve_pedidoestado
    
    all_pedidoproducto = pedidoproducto_schema.all_pedidoproducto
    resolve_all_pedidoproducto = pedidoproducto_schema.resolve_all_pedidoproducto
    pedidoproducto = pedidoproducto_schema.pedidoproducto
    resolve_pedidoproducto = pedidoproducto_schema.resolve_pedidoproducto
    
    all_producto = producto_schema.all_producto
    resolve_all_producto = producto_schema.resolve_all_producto
    producto = producto_schema.producto
    resolve_producto = producto_schema.resolve_producto
    
    all_productocategoria = productocategoria_schema.all_productocategoria
    resolve_all_productocategoria = productocategoria_schema.resolve_all_productocategoria
    productocategoria = productocategoria_schema.productocategoria
    resolve_productocategoria = productocategoria_schema.resolve_productocategoria
    
    all_profile = profile_schema.all_profile
    resolve_all_profile = profile_schema.resolve_all_profile
    profile = profile_schema.profile
    resolve_profile = profile_schema.resolve_profile
    
    all_region = region_schema.all_region
    resolve_all_region = region_schema.resolve_all_region
    region = region_schema.region
    resolve_region = region_schema.resolve_region
    
    all_seccion = seccion_schema.all_seccion
    resolve_all_seccion = seccion_schema.resolve_all_seccion
    seccion = seccion_schema.seccion
    resolve_seccion = seccion_schema.resolve_seccion
    
    all_seccioncategoria = seccioncategoria_schema.all_seccioncategoria
    resolve_all_seccioncategoria = seccioncategoria_schema.resolve_all_seccioncategoria
    seccioncategoria = seccioncategoria_schema.seccioncategoria
    resolve_seccioncategoria = seccioncategoria_schema.resolve_seccioncategoria
    
    all_seo = seo_schema.all_seo
    resolve_all_seo = seo_schema.resolve_all_seo
    seo = seo_schema.seo
    resolve_seo = seo_schema.resolve_seo
    
    all_sitemap = sitemap_schema.all_sitemap
    resolve_all_sitemap = sitemap_schema.resolve_all_sitemap
    sitemap = sitemap_schema.sitemap
    resolve_sitemap = sitemap_schema.resolve_sitemap
    
    all_table = table_schema.all_table
    resolve_all_table = table_schema.resolve_all_table
    table = table_schema.table
    resolve_table = table_schema.resolve_table
    
    all_texto = texto_schema.all_texto
    resolve_all_texto = texto_schema.resolve_all_texto
    texto = texto_schema.texto
    resolve_texto = texto_schema.resolve_texto
    
    all_usuario = usuario_schema.all_usuario
    resolve_all_usuario = usuario_schema.resolve_all_usuario
    usuario = usuario_schema.usuario
    resolve_usuario = usuario_schema.resolve_usuario
    
    all_usuariodireccion = usuariodireccion_schema.all_usuariodireccion
    resolve_all_usuariodireccion = usuariodireccion_schema.resolve_all_usuariodireccion
    usuariodireccion = usuariodireccion_schema.usuariodireccion
    resolve_usuariodireccion = usuariodireccion_schema.resolve_usuariodireccion
    
# __QUERY__
    
    
    
    
    
    
    
    
    
    
    
    
    
class Mutation(graphene.ObjectType):

# __MUTATION__
    
    create_administrador = administrador_schema.create_administrador.Field()
    update_administrador = administrador_schema.update_administrador.Field()
    delete_administrador = administrador_schema.delete_administrador.Field()
    
    create_banner = banner_schema.create_banner.Field()
    update_banner = banner_schema.update_banner.Field()
    delete_banner = banner_schema.delete_banner.Field()
    
    create_comuna = comuna_schema.create_comuna.Field()
    update_comuna = comuna_schema.update_comuna.Field()
    delete_comuna = comuna_schema.delete_comuna.Field()
    
    create_configuracion = configuracion_schema.create_configuracion.Field()
    update_configuracion = configuracion_schema.update_configuracion.Field()
    delete_configuracion = configuracion_schema.delete_configuracion.Field()
    
    create_direccion = direccion_schema.create_direccion.Field()
    update_direccion = direccion_schema.update_direccion.Field()
    delete_direccion = direccion_schema.delete_direccion.Field()
    
    create_galeria = galeria_schema.create_galeria.Field()
    update_galeria = galeria_schema.update_galeria.Field()
    delete_galeria = galeria_schema.delete_galeria.Field()
    
    create_igaccounts = igaccounts_schema.create_igaccounts.Field()
    update_igaccounts = igaccounts_schema.update_igaccounts.Field()
    delete_igaccounts = igaccounts_schema.delete_igaccounts.Field()
    
    create_ighashtag = ighashtag_schema.create_ighashtag.Field()
    update_ighashtag = ighashtag_schema.update_ighashtag.Field()
    delete_ighashtag = ighashtag_schema.delete_ighashtag.Field()
    
    create_igtotal = igtotal_schema.create_igtotal.Field()
    update_igtotal = igtotal_schema.update_igtotal.Field()
    delete_igtotal = igtotal_schema.delete_igtotal.Field()
    
    create_igusuario = igusuario_schema.create_igusuario.Field()
    update_igusuario = igusuario_schema.update_igusuario.Field()
    delete_igusuario = igusuario_schema.delete_igusuario.Field()
    
    create_log = log_schema.create_log.Field()
    update_log = log_schema.update_log.Field()
    delete_log = log_schema.delete_log.Field()
    
    create_logo = logo_schema.create_logo.Field()
    update_logo = logo_schema.update_logo.Field()
    delete_logo = logo_schema.delete_logo.Field()
    
    create_mediopago = mediopago_schema.create_mediopago.Field()
    update_mediopago = mediopago_schema.update_mediopago.Field()
    delete_mediopago = mediopago_schema.delete_mediopago.Field()
    
    create_modulo = modulo_schema.create_modulo.Field()
    update_modulo = modulo_schema.update_modulo.Field()
    delete_modulo = modulo_schema.delete_modulo.Field()
    
    create_moduloconfiguracion = moduloconfiguracion_schema.create_moduloconfiguracion.Field()
    update_moduloconfiguracion = moduloconfiguracion_schema.update_moduloconfiguracion.Field()
    delete_moduloconfiguracion = moduloconfiguracion_schema.delete_moduloconfiguracion.Field()
    
    create_pedido = pedido_schema.create_pedido.Field()
    update_pedido = pedido_schema.update_pedido.Field()
    delete_pedido = pedido_schema.delete_pedido.Field()
    
    create_pedidodireccion = pedidodireccion_schema.create_pedidodireccion.Field()
    update_pedidodireccion = pedidodireccion_schema.update_pedidodireccion.Field()
    delete_pedidodireccion = pedidodireccion_schema.delete_pedidodireccion.Field()
    
    create_pedidoestado = pedidoestado_schema.create_pedidoestado.Field()
    update_pedidoestado = pedidoestado_schema.update_pedidoestado.Field()
    delete_pedidoestado = pedidoestado_schema.delete_pedidoestado.Field()
    
    create_pedidoproducto = pedidoproducto_schema.create_pedidoproducto.Field()
    update_pedidoproducto = pedidoproducto_schema.update_pedidoproducto.Field()
    delete_pedidoproducto = pedidoproducto_schema.delete_pedidoproducto.Field()
    
    create_producto = producto_schema.create_producto.Field()
    update_producto = producto_schema.update_producto.Field()
    delete_producto = producto_schema.delete_producto.Field()
    
    create_productocategoria = productocategoria_schema.create_productocategoria.Field()
    update_productocategoria = productocategoria_schema.update_productocategoria.Field()
    delete_productocategoria = productocategoria_schema.delete_productocategoria.Field()
    
    create_profile = profile_schema.create_profile.Field()
    update_profile = profile_schema.update_profile.Field()
    delete_profile = profile_schema.delete_profile.Field()
    
    create_region = region_schema.create_region.Field()
    update_region = region_schema.update_region.Field()
    delete_region = region_schema.delete_region.Field()
    
    create_seccion = seccion_schema.create_seccion.Field()
    update_seccion = seccion_schema.update_seccion.Field()
    delete_seccion = seccion_schema.delete_seccion.Field()
    
    create_seccioncategoria = seccioncategoria_schema.create_seccioncategoria.Field()
    update_seccioncategoria = seccioncategoria_schema.update_seccioncategoria.Field()
    delete_seccioncategoria = seccioncategoria_schema.delete_seccioncategoria.Field()
    
    create_seo = seo_schema.create_seo.Field()
    update_seo = seo_schema.update_seo.Field()
    delete_seo = seo_schema.delete_seo.Field()
    
    create_sitemap = sitemap_schema.create_sitemap.Field()
    update_sitemap = sitemap_schema.update_sitemap.Field()
    delete_sitemap = sitemap_schema.delete_sitemap.Field()
    
    create_table = table_schema.create_table.Field()
    update_table = table_schema.update_table.Field()
    delete_table = table_schema.delete_table.Field()
    
    create_texto = texto_schema.create_texto.Field()
    update_texto = texto_schema.update_texto.Field()
    delete_texto = texto_schema.delete_texto.Field()
    
    create_usuario = usuario_schema.create_usuario.Field()
    update_usuario = usuario_schema.update_usuario.Field()
    delete_usuario = usuario_schema.delete_usuario.Field()
    
    create_usuariodireccion = usuariodireccion_schema.create_usuariodireccion.Field()
    update_usuariodireccion = usuariodireccion_schema.update_usuariodireccion.Field()
    delete_usuariodireccion = usuariodireccion_schema.delete_usuariodireccion.Field()
    
# __MUTATION__
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    

# __TYPES__
    
schema = graphene.Schema(query=Query,mutation=Mutation)
# __TYPES__
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    