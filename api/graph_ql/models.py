from .database import Base
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    func,
    Text,
    Boolean,
    JSON,
)
from sqlalchemy.orm import backref, relationship


# __MODELS__
    
class administrador_model(Base):
    __tablename__ = "seo_administrador"
    idadministrador = Column(Integer, primary_key=True, nullable=False)
    tipo=Column(Integer, nullable=False)
    email=Column(String(255), nullable=False)
    password=Column(String(255), nullable=False)
    nombre=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    estado=Column(Boolean, nullable=False)
    cookie=Column(String(255), nullable=False)
    
class banner_model(Base):
    __tablename__ = "seo_banner"
    idbanner = Column(Integer, primary_key=True, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    texto1=Column(String(255), nullable=False)
    texto2=Column(String(255), nullable=False)
    texto3=Column(String(255), nullable=False)
    texto=Column(Text, nullable=False)
    link=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class comuna_model(Base):
    __tablename__ = "seo_comuna"
    idcomuna = Column(Integer, primary_key=True, nullable=False)
    idregion=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    precio=Column(Integer, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class configuracion_model(Base):
    __tablename__ = "seo_configuracion"
    idconfiguracion = Column(Integer, primary_key=True, nullable=False)
    variable=Column(String(255), nullable=False)
    valor=Column(Text, nullable=False)
    
class direccion_model(Base):
    __tablename__ = "seo_direccion"
    iddireccion = Column(Integer, primary_key=True, nullable=False)
    idusuario=Column(Integer, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    nombre=Column(String(255), nullable=False)
    direccion=Column(String(255), nullable=False)
    idcomuna=Column(Integer, nullable=False)
    telefono=Column(String(255), nullable=False)
    villa=Column(String(255), nullable=False)
    edificio=Column(String(255), nullable=False)
    departamento=Column(String(255), nullable=False)
    condominio=Column(String(255), nullable=False)
    casa=Column(String(255), nullable=False)
    empresa=Column(String(255), nullable=False)
    referencias=Column(Text, nullable=False)
    
class galeria_model(Base):
    __tablename__ = "seo_galeria"
    idgaleria = Column(Integer, primary_key=True, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    url=Column(String(255), nullable=False)
    subtitulo=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    resumen=Column(Text, nullable=False)
    keywords=Column(String(255), nullable=False)
    metadescripcion=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class igaccounts_model(Base):
    __tablename__ = "seo_igaccounts"
    idigaccounts = Column(Integer, primary_key=True, nullable=False)
    pk=Column(String(255), nullable=False)
    username=Column(String(255), nullable=False)
    full_name=Column(String(255), nullable=False)
    profile_pic_url=Column(String(255), nullable=False)
    biography=Column(Text, nullable=False)
    follower_count=Column(Integer, nullable=False)
    following_count=Column(Integer, nullable=False)
    has_anonymous_profile_picture=Column(Boolean, nullable=False)
    is_private=Column(Boolean, nullable=False)
    is_business=Column(Boolean, nullable=False)
    is_verified=Column(Boolean, nullable=False)
    media_count=Column(Integer, nullable=False)
    fecha=Column(DateTime, nullable=False)
    following=Column(Boolean, nullable=False)
    follower=Column(Boolean, nullable=False)
    favorito=Column(Boolean, nullable=False)
    hashtag=Column(String(255), nullable=False)
    
class ighashtag_model(Base):
    __tablename__ = "seo_ighashtag"
    idighashtag = Column(Integer, primary_key=True, nullable=False)
    hashtag=Column(String(255), nullable=False)
    following=Column(Integer, nullable=False)
    follower=Column(Integer, nullable=False)
    removed=Column(Integer, nullable=False)
    eficiencia=Column(Integer, nullable=False)
    eficiencia2=Column(Integer, nullable=False)
    total=Column(Integer, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class igtotal_model(Base):
    __tablename__ = "seo_igtotal"
    idigtotal = Column(Integer, primary_key=True, nullable=False)
    tag=Column(String(255), nullable=False)
    fecha=Column(DateTime, nullable=False)
    cantidad=Column(Integer, nullable=False)
    
class igusuario_model(Base):
    __tablename__ = "seo_igusuario"
    idigusuario = Column(Integer, primary_key=True, nullable=False)
    usuario=Column(String(255), nullable=False)
    password=Column(String(255), nullable=False)
    estado=Column(Boolean, nullable=False)
    
class log_model(Base):
    __tablename__ = "seo_log"
    idlog = Column(Integer, primary_key=True, nullable=False)
    administrador=Column(String(255), nullable=False)
    tabla=Column(String(255), nullable=False)
    accion=Column(String(255), nullable=False)
    fecha=Column(DateTime, nullable=False)
    
class logo_model(Base):
    __tablename__ = "seo_logo"
    idlogo = Column(Integer, primary_key=True, nullable=False)
    titulo=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    orden=Column(Integer, nullable=False)
    
class mediopago_model(Base):
    __tablename__ = "seo_mediopago"
    idmediopago = Column(Integer, primary_key=True, nullable=False)
    titulo=Column(String(255), nullable=False)
    resumen=Column(Text, nullable=False)
    descripcion=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class modulo_model(Base):
    __tablename__ = "seo_modulo"
    idmodulo = Column(Integer, primary_key=True, nullable=False)
    idmoduloconfiguracion=Column(Integer, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    menu=Column(Text, nullable=False)
    mostrar=Column(Text, nullable=False)
    detalle=Column(Text, nullable=False)
    recortes=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Text, nullable=False)
    aside=Column(Boolean, nullable=False)
    hijos=Column(Boolean, nullable=False)
    
class moduloconfiguracion_model(Base):
    __tablename__ = "seo_moduloconfiguracion"
    idmoduloconfiguracion = Column(Integer, primary_key=True, nullable=False)
    icono=Column(String(255), nullable=False)
    module=Column(String(255), nullable=False)
    titulo=Column(String(255), nullable=False)
    sub=Column(String(255), nullable=False)
    padre=Column(String(255), nullable=False)
    mostrar=Column(Text, nullable=False)
    detalle=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    aside=Column(Boolean, nullable=False)
    tipos=Column(Boolean, nullable=False)
    
class pedido_model(Base):
    __tablename__ = "seo_pedido"
    idpedido = Column(Integer, primary_key=True, nullable=False)
    tipo=Column(Integer, nullable=False)
    cookie_pedido=Column(String(255), nullable=False)
    fecha_creacion=Column(DateTime, nullable=False)
    fecha_pago=Column(DateTime, nullable=False)
    idusuario=Column(Integer, nullable=False)
    idpedidoestado=Column(Integer, nullable=False)
    idmediopago=Column(Integer, nullable=False)
    nombre=Column(String(255), nullable=False)
    email=Column(String(255), nullable=False)
    telefono=Column(String(255), nullable=False)
    total_original=Column(Integer, nullable=False)
    total=Column(Integer, nullable=False)
    comentarios=Column(Text, nullable=False)
    pedido_manual=Column(Boolean, nullable=False)
    
class pedidodireccion_model(Base):
    __tablename__ = "seo_pedidodireccion"
    idpedidodireccion = Column(Integer, primary_key=True, nullable=False)
    idpedido=Column(Integer, nullable=False)
    idusuariodireccion=Column(Integer, nullable=False)
    idpedidoestado=Column(Integer, nullable=False)
    precio=Column(Integer, nullable=False)
    cookie_direccion=Column(String(255), nullable=False)
    nombre=Column(String(255), nullable=False)
    telefono=Column(String(255), nullable=False)
    direccion_completa=Column(Text, nullable=False)
    referencias=Column(Text, nullable=False)
    fecha_entrega=Column(DateTime, nullable=False)
    
class pedidoestado_model(Base):
    __tablename__ = "seo_pedidoestado"
    idpedidoestado = Column(Integer, primary_key=True, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    resumen=Column(Text, nullable=False)
    color=Column(String(255), nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class pedidoproducto_model(Base):
    __tablename__ = "seo_pedidoproducto"
    idpedidoproducto = Column(Integer, primary_key=True, nullable=False)
    idpedido=Column(Integer, nullable=False)
    idpedidodireccion=Column(Integer, nullable=False)
    idproducto=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    mensaje=Column(Text, nullable=False)
    idproductoatributo=Column(Integer, nullable=False)
    titulo_atributo=Column(String(255), nullable=False)
    precio=Column(Integer, nullable=False)
    cantidad=Column(Integer, nullable=False)
    total=Column(Integer, nullable=False)
    
class producto_model(Base):
    __tablename__ = "seo_producto"
    idproducto = Column(Integer, primary_key=True, nullable=False)
    idproductocategoria=Column(Text, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    url=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    archivo=Column(JSON, nullable=False)
    codigo=Column(String(255), nullable=False)
    precio=Column(Integer, nullable=False)
    descuento=Column(Integer, nullable=False)
    descuento_fecha=Column(Text, nullable=False)
    stock=Column(Integer, nullable=False)
    ventas=Column(Integer, nullable=False)
    resumen=Column(Text, nullable=False)
    descripcion=Column(Text, nullable=False)
    keywords=Column(String(255), nullable=False)
    metadescripcion=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    destacado=Column(Boolean, nullable=False)
    
class productocategoria_model(Base):
    __tablename__ = "seo_productocategoria"
    idproductocategoria = Column(Integer, primary_key=True, nullable=False)
    idpadre=Column(Text, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    url=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    descuento=Column(Integer, nullable=False)
    descuento_fecha=Column(Text, nullable=False)
    resumen=Column(Text, nullable=False)
    descripcion=Column(Text, nullable=False)
    keywords=Column(String(255), nullable=False)
    metadescripcion=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    destacado=Column(Boolean, nullable=False)
    
class profile_model(Base):
    __tablename__ = "seo_profile"
    idprofile = Column(Integer, primary_key=True, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class region_model(Base):
    __tablename__ = "seo_region"
    idregion = Column(Integer, primary_key=True, nullable=False)
    titulo=Column(String(255), nullable=False)
    precio=Column(Integer, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class seccion_model(Base):
    __tablename__ = "seo_seccion"
    idseccion = Column(Integer, primary_key=True, nullable=False)
    idseccioncategoria=Column(Text, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    subtitulo=Column(String(255), nullable=False)
    url=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    archivo=Column(JSON, nullable=False)
    resumen=Column(Text, nullable=False)
    descripcion=Column(Text, nullable=False)
    keywords=Column(String(255), nullable=False)
    metadescripcion=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    destacado=Column(Boolean, nullable=False)
    
class seccioncategoria_model(Base):
    __tablename__ = "seo_seccioncategoria"
    idseccioncategoria = Column(Integer, primary_key=True, nullable=False)
    idpadre=Column(Text, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    url=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    resumen=Column(Text, nullable=False)
    descripcion=Column(Text, nullable=False)
    keywords=Column(String(255), nullable=False)
    metadescripcion=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    destacado=Column(Boolean, nullable=False)
    
class seo_model(Base):
    __tablename__ = "seo_seo"
    idseo = Column(Integer, primary_key=True, nullable=False)
    titulo=Column(String(255), nullable=False)
    url=Column(String(255), nullable=False)
    subtitulo=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    banner=Column(JSON, nullable=False)
    modulo_front=Column(String(255), nullable=False)
    modulo_back=Column(String(255), nullable=False)
    tipo_modulo=Column(Integer, nullable=False)
    link_menu=Column(String(255), nullable=False)
    keywords=Column(String(255), nullable=False)
    metadescripcion=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    menu=Column(Boolean, nullable=False)
    submenu=Column(Boolean, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class sitemap_model(Base):
    __tablename__ = "seo_sitemap"
    idsitemap = Column(Integer, primary_key=True, nullable=False)
    idpadre=Column(Integer, nullable=False)
    url=Column(String(255), nullable=False)
    depth=Column(Integer, nullable=False)
    valid=Column(String(255), nullable=False)
    ready=Column(Boolean, nullable=False)
    
class table_model(Base):
    __tablename__ = "seo_table"
    idtable = Column(Integer, primary_key=True, nullable=False)
    tablename=Column(String(255), nullable=False)
    idname=Column(String(255), nullable=False)
    fields=Column(Text, nullable=False)
    truncate=Column(Boolean, nullable=False)
    
class texto_model(Base):
    __tablename__ = "seo_texto"
    idtexto = Column(Integer, primary_key=True, nullable=False)
    tipo=Column(String(255), nullable=False)
    titulo=Column(String(255), nullable=False)
    url=Column(String(255), nullable=False)
    descripcion=Column(Text, nullable=False)
    texto=Column(String(255), nullable=False)
    mapa=Column(Text, nullable=False)
    orden=Column(Integer, nullable=False)
    estado=Column(Boolean, nullable=False)
    
class usuario_model(Base):
    __tablename__ = "seo_usuario"
    idusuario = Column(Integer, primary_key=True, nullable=False)
    tipo=Column(Integer, nullable=False)
    nombre=Column(String(255), nullable=False)
    telefono=Column(String(255), nullable=False)
    email=Column(String(255), nullable=False)
    password=Column(String(255), nullable=False)
    foto=Column(JSON, nullable=False)
    estado=Column(Boolean, nullable=False)
    cookie=Column(String(255), nullable=False)
    
class usuariodireccion_model(Base):
    __tablename__ = "seo_usuariodireccion"
    idusuariodireccion = Column(Integer, primary_key=True, nullable=False)
    idusuario=Column(Integer, nullable=False)
    tipo=Column(Integer, nullable=False)
    titulo=Column(String(255), nullable=False)
    nombre=Column(String(255), nullable=False)
    direccion=Column(String(255), nullable=False)
    idcomuna=Column(Integer, nullable=False)
    telefono=Column(String(255), nullable=False)
    villa=Column(String(255), nullable=False)
    edificio=Column(String(255), nullable=False)
    departamento=Column(String(255), nullable=False)
    condominio=Column(String(255), nullable=False)
    casa=Column(String(255), nullable=False)
    empresa=Column(String(255), nullable=False)
    referencias=Column(Text, nullable=False)
    

# __MODELS__
    
    
    
    

