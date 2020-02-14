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
    tipo = Column(Integer)
    email = Column(String(255))
    password = Column(String(255))
    nombre = Column(String(255))
    estado = Column(Boolean, nullable=False, default=False)
    cookie = Column(String(255))
    
    

class banner_model(Base):
    __tablename__ = "seo_banner"
    idbanner = Column(Integer, primary_key=True, nullable=False)
    tipo = Column(Integer)
    titulo = Column(String(255))
    texto1 = Column(String(255))
    texto2 = Column(String(255))
    texto3 = Column(String(255))
    texto = Column(Text)
    link = Column(String(255))
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class comuna_model(Base):
    __tablename__ = "seo_comuna"
    idcomuna = Column(Integer, primary_key=True, nullable=False)
    idregion = Column(Integer)
    titulo = Column(String(255))
    precio = Column(Integer)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class configuracion_model(Base):
    __tablename__ = "seo_configuracion"
    idconfiguracion = Column(Integer, primary_key=True, nullable=False)
    variable = Column(String(255))
    valor = Column(Text)
    
    

class direccion_model(Base):
    __tablename__ = "seo_direccion"
    iddireccion = Column(Integer, primary_key=True, nullable=False)
    idusuario = Column(Integer)
    tipo = Column(Integer)
    titulo = Column(String(255))
    nombre = Column(String(255))
    direccion = Column(String(255))
    idcomuna = Column(Integer)
    telefono = Column(String(255))
    villa = Column(String(255))
    edificio = Column(String(255))
    departamento = Column(String(255))
    condominio = Column(String(255))
    casa = Column(String(255))
    empresa = Column(String(255))
    referencias = Column(Text)
    
    

class galeria_model(Base):
    __tablename__ = "seo_galeria"
    idgaleria = Column(Integer, primary_key=True, nullable=False)
    tipo = Column(Integer)
    titulo = Column(String(255))
    url = Column(String(255))
    subtitulo = Column(String(255))
    resumen = Column(Text)
    keywords = Column(String(255))
    metadescripcion = Column(Text)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class igaccounts_model(Base):
    __tablename__ = "seo_igaccounts"
    idigaccounts = Column(Integer, primary_key=True, nullable=False)
    pk = Column(String(255))
    username = Column(String(255))
    full_name = Column(String(255))
    profile_pic_url = Column(String(255))
    biography = Column(Text)
    follower_count = Column(Integer)
    following_count = Column(Integer)
    has_anonymous_profile_picture = Column(Boolean, nullable=False, default=False)
    is_private = Column(Boolean, nullable=False, default=False)
    is_business = Column(Boolean, nullable=False, default=False)
    is_verified = Column(Boolean, nullable=False, default=False)
    media_count = Column(Integer)
    fecha = Column(DateTime)
    following = Column(Boolean, nullable=False, default=False)
    follower = Column(Boolean, nullable=False, default=False)
    favorito = Column(Boolean, nullable=False, default=False)
    hashtag = Column(String(255))
    
    

class ighashtag_model(Base):
    __tablename__ = "seo_ighashtag"
    idighashtag = Column(Integer, primary_key=True, nullable=False)
    hashtag = Column(String(255))
    following = Column(Integer)
    follower = Column(Integer)
    removed = Column(Integer)
    eficiencia = Column(Integer)
    eficiencia2 = Column(Integer)
    total = Column(Integer)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class igtotal_model(Base):
    __tablename__ = "seo_igtotal"
    idigtotal = Column(Integer, primary_key=True, nullable=False)
    tag = Column(String(255))
    fecha = Column(DateTime)
    cantidad = Column(Integer)
    
    

class igusuario_model(Base):
    __tablename__ = "seo_igusuario"
    idigusuario = Column(Integer, primary_key=True, nullable=False)
    usuario = Column(String(255))
    password = Column(String(255))
    estado = Column(Boolean, nullable=False, default=False)
    
    

class image_model(Base):
    __tablename__ = "seo_image"
    idimage = Column(Integer, primary_key=True, nullable=False)
    table_name = Column(String(255))
    field_name = Column(String(255))
    idparent = Column(Integer)
    name = Column(String(255))
    extension = Column(String(255))
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    portada = Column(Boolean, nullable=False, default=False)
    
    

class log_model(Base):
    __tablename__ = "seo_log"
    idlog = Column(Integer, primary_key=True, nullable=False)
    administrador = Column(String(255))
    tabla = Column(String(255))
    accion = Column(String(255))
    fecha = Column(DateTime)
    
    

class logo_model(Base):
    __tablename__ = "seo_logo"
    idlogo = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(255))
    orden = Column(Integer)
    
    

class mediopago_model(Base):
    __tablename__ = "seo_mediopago"
    idmediopago = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(255))
    resumen = Column(Text)
    descripcion = Column(Text)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class modulo_model(Base):
    __tablename__ = "seo_modulo"
    idmodulo = Column(Integer, primary_key=True, nullable=False)
    idmoduloconfiguracion = Column(Integer)
    tipo = Column(Integer)
    titulo = Column(String(255))
    menu = Column(Text)
    mostrar = Column(Text)
    detalle = Column(Text)
    recortes = Column(Text)
    orden = Column(Integer)
    estado = Column(Text)
    aside = Column(Boolean, nullable=False, default=False)
    hijos = Column(Boolean, nullable=False, default=False)
    
    

class moduloconfiguracion_model(Base):
    __tablename__ = "seo_moduloconfiguracion"
    idmoduloconfiguracion = Column(Integer, primary_key=True, nullable=False)
    icono = Column(String(255))
    module = Column(String(255))
    titulo = Column(String(255))
    sub = Column(String(255))
    padre = Column(String(255))
    mostrar = Column(Text)
    detalle = Column(Text)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    aside = Column(Boolean, nullable=False, default=False)
    tipos = Column(Boolean, nullable=False, default=False)
    
    

class pedido_model(Base):
    __tablename__ = "seo_pedido"
    idpedido = Column(Integer, primary_key=True, nullable=False)
    tipo = Column(Integer)
    cookie_pedido = Column(String(255))
    fecha_creacion = Column(DateTime)
    fecha_pago = Column(DateTime)
    idusuario = Column(Integer)
    idpedidoestado = Column(Integer)
    idmediopago = Column(Integer)
    nombre = Column(String(255))
    email = Column(String(255))
    telefono = Column(String(255))
    total_original = Column(Integer)
    total = Column(Integer)
    comentarios = Column(Text)
    pedido_manual = Column(Boolean, nullable=False, default=False)
    
    

class pedidodireccion_model(Base):
    __tablename__ = "seo_pedidodireccion"
    idpedidodireccion = Column(Integer, primary_key=True, nullable=False)
    idpedido = Column(Integer)
    idusuariodireccion = Column(Integer)
    idpedidoestado = Column(Integer)
    precio = Column(Integer)
    cookie_direccion = Column(String(255))
    nombre = Column(String(255))
    telefono = Column(String(255))
    direccion_completa = Column(Text)
    referencias = Column(Text)
    fecha_entrega = Column(DateTime)
    
    

class pedidoestado_model(Base):
    __tablename__ = "seo_pedidoestado"
    idpedidoestado = Column(Integer, primary_key=True, nullable=False)
    tipo = Column(Integer)
    titulo = Column(String(255))
    resumen = Column(Text)
    color = Column(String(255))
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class pedidoproducto_model(Base):
    __tablename__ = "seo_pedidoproducto"
    idpedidoproducto = Column(Integer, primary_key=True, nullable=False)
    idpedido = Column(Integer)
    idpedidodireccion = Column(Integer)
    idproducto = Column(Integer)
    titulo = Column(String(255))
    mensaje = Column(Text)
    idproductoatributo = Column(Integer)
    titulo_atributo = Column(String(255))
    precio = Column(Integer)
    cantidad = Column(Integer)
    total = Column(Integer)
    
    

class producto_model(Base):
    __tablename__ = "seo_producto"
    idproducto = Column(Integer, primary_key=True, nullable=False)
    idproductocategoria = Column(Text)
    tipo = Column(Integer)
    titulo = Column(String(255))
    url = Column(String(255))
    archivo = Column(JSON)
    codigo = Column(String(255))
    precio = Column(Integer)
    descuento = Column(Integer)
    descuento_fecha = Column(Text)
    stock = Column(Integer)
    ventas = Column(Integer)
    resumen = Column(Text)
    descripcion = Column(Text)
    keywords = Column(String(255))
    metadescripcion = Column(Text)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    destacado = Column(Boolean, nullable=False, default=False)
    
    

class productocategoria_model(Base):
    __tablename__ = "seo_productocategoria"
    idproductocategoria = Column(Integer, primary_key=True, nullable=False)
    idpadre = Column(Text)
    tipo = Column(Integer)
    titulo = Column(String(255))
    url = Column(String(255))
    descuento = Column(Integer)
    descuento_fecha = Column(Text)
    resumen = Column(Text)
    descripcion = Column(Text)
    keywords = Column(String(255))
    metadescripcion = Column(Text)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    destacado = Column(Boolean, nullable=False, default=False)
    
    

class profile_model(Base):
    __tablename__ = "seo_profile"
    idprofile = Column(Integer, primary_key=True, nullable=False)
    tipo = Column(Integer)
    titulo = Column(String(255))
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class region_model(Base):
    __tablename__ = "seo_region"
    idregion = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(255))
    precio = Column(Integer)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class seccion_model(Base):
    __tablename__ = "seo_seccion"
    idseccion = Column(Integer, primary_key=True, nullable=False)
    idseccioncategoria = Column(Text)
    tipo = Column(Integer)
    titulo = Column(String(255))
    subtitulo = Column(String(255))
    url = Column(String(255))
    archivo = Column(JSON)
    resumen = Column(Text)
    descripcion = Column(Text)
    keywords = Column(String(255))
    metadescripcion = Column(Text)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    destacado = Column(Boolean, nullable=False, default=False)
    
    

class seccioncategoria_model(Base):
    __tablename__ = "seo_seccioncategoria"
    idseccioncategoria = Column(Integer, primary_key=True, nullable=False)
    idpadre = Column(Text)
    tipo = Column(Integer)
    titulo = Column(String(255))
    url = Column(String(255))
    resumen = Column(Text)
    descripcion = Column(Text)
    keywords = Column(String(255))
    metadescripcion = Column(Text)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    destacado = Column(Boolean, nullable=False, default=False)
    
    

class seo_model(Base):
    __tablename__ = "seo_seo"
    idseo = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String(255))
    url = Column(String(255))
    subtitulo = Column(String(255))
    modulo_front = Column(String(255))
    modulo_back = Column(String(255))
    tipo_modulo = Column(Integer)
    link_menu = Column(String(255))
    keywords = Column(String(255))
    metadescripcion = Column(Text)
    orden = Column(Integer)
    menu = Column(Boolean, nullable=False, default=False)
    submenu = Column(Boolean, nullable=False, default=False)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class sitemap_model(Base):
    __tablename__ = "seo_sitemap"
    idsitemap = Column(Integer, primary_key=True, nullable=False)
    idpadre = Column(Integer)
    url = Column(String(255))
    depth = Column(Integer)
    valid = Column(String(255))
    ready = Column(Boolean, nullable=False, default=False)
    
    

class table_model(Base):
    __tablename__ = "seo_table"
    idtable = Column(Integer, primary_key=True, nullable=False)
    tablename = Column(String(255))
    idname = Column(String(255))
    fields = Column(Text)
    truncate = Column(Boolean, nullable=False, default=False)
    
    

class texto_model(Base):
    __tablename__ = "seo_texto"
    idtexto = Column(Integer, primary_key=True, nullable=False)
    tipo = Column(String(255))
    titulo = Column(String(255))
    url = Column(String(255))
    descripcion = Column(Text)
    texto = Column(String(255))
    mapa = Column(Text)
    orden = Column(Integer)
    estado = Column(Boolean, nullable=False, default=False)
    
    

class usuario_model(Base):
    __tablename__ = "seo_usuario"
    idusuario = Column(Integer, primary_key=True, nullable=False)
    tipo = Column(Integer)
    nombre = Column(String(255))
    telefono = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    estado = Column(Boolean, nullable=False, default=False)
    cookie = Column(String(255))
    
    

class usuariodireccion_model(Base):
    __tablename__ = "seo_usuariodireccion"
    idusuariodireccion = Column(Integer, primary_key=True, nullable=False)
    idusuario = Column(Integer)
    tipo = Column(Integer)
    titulo = Column(String(255))
    nombre = Column(String(255))
    direccion = Column(String(255))
    idcomuna = Column(Integer)
    telefono = Column(String(255))
    villa = Column(String(255))
    edificio = Column(String(255))
    departamento = Column(String(255))
    condominio = Column(String(255))
    casa = Column(String(255))
    empresa = Column(String(255))
    referencias = Column(Text)
    
    

# __MODELS__
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

