"""first

Revision ID: 685232bad991
Revises: 17dae11cd9da
Create Date: 2020-01-09 19:09:26.140691

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '685232bad991'
down_revision = '17dae11cd9da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('seo_administrador', 'cookie',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_administrador', 'email',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_administrador', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_administrador', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_administrador', 'nombre',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_administrador', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    
    op.alter_column('seo_banner', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_banner', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_banner', 'link',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_banner', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_banner', 'texto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_banner', 'texto1',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_banner', 'texto2',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_banner', 'texto3',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_banner', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_banner', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_comuna', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_comuna', 'idregion',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_comuna', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_comuna', 'precio',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_comuna', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_configuracion', 'valor',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_configuracion', 'variable',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'casa',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'condominio',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'departamento',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'direccion',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'edificio',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'empresa',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'idcomuna',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_direccion', 'idusuario',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_direccion', 'nombre',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'referencias',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_direccion', 'telefono',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_direccion', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_direccion', 'villa',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_galeria', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_galeria', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_galeria', 'keywords',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_galeria', 'metadescripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_galeria', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_galeria', 'resumen',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_galeria', 'subtitulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_galeria', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_galeria', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_galeria', 'url',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_igaccounts', 'biography',
               existing_type=mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_bin'),
               nullable=True)
    op.alter_column('seo_igaccounts', 'favorito',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_igaccounts', 'fecha',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('seo_igaccounts', 'follower',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_igaccounts', 'follower_count',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_igaccounts', 'following',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_igaccounts', 'following_count',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_igaccounts', 'full_name',
               existing_type=mysql.CHAR(charset='utf8mb4', collation='utf8mb4_bin', length=255),
               nullable=True)
    op.alter_column('seo_igaccounts', 'has_anonymous_profile_picture',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_igaccounts', 'hashtag',
               existing_type=mysql.CHAR(charset='utf8mb4', collation='utf8mb4_bin', length=255),
               nullable=True)
    op.alter_column('seo_igaccounts', 'is_business',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_igaccounts', 'is_private',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_igaccounts', 'is_verified',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_igaccounts', 'media_count',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_igaccounts', 'pk',
               existing_type=mysql.CHAR(charset='utf8mb4', collation='utf8mb4_bin', length=255),
               nullable=True)
    op.alter_column('seo_igaccounts', 'profile_pic_url',
               existing_type=mysql.CHAR(charset='utf8mb4', collation='utf8mb4_bin', length=255),
               nullable=True)
    op.alter_column('seo_igaccounts', 'username',
               existing_type=mysql.CHAR(charset='utf8mb4', collation='utf8mb4_bin', length=255),
               nullable=True)
    op.alter_column('seo_ighashtag', 'eficiencia',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_ighashtag', 'eficiencia2',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_ighashtag', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_ighashtag', 'follower',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_ighashtag', 'following',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_ighashtag', 'hashtag',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_ighashtag', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_ighashtag', 'removed',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_ighashtag', 'total',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_igtotal', 'cantidad',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_igtotal', 'fecha',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('seo_igtotal', 'tag',
               existing_type=mysql.CHAR(charset='utf8mb4', collation='utf8mb4_bin', length=255),
               nullable=True)
    op.alter_column('seo_igusuario', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_igusuario', 'password',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_igusuario', 'usuario',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_log', 'accion',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_log', 'administrador',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_log', 'fecha',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('seo_log', 'tabla',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_logo', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_logo', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_logo', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_mediopago', 'descripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_mediopago', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_mediopago', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_mediopago', 'resumen',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_mediopago', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_modulo', 'aside',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_modulo', 'detalle',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_modulo', 'estado',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_modulo', 'hijos',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_modulo', 'idmoduloconfiguracion',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_modulo', 'menu',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_modulo', 'mostrar',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_modulo', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_modulo', 'recortes',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_modulo', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_modulo', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_moduloconfiguracion', 'aside',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_moduloconfiguracion', 'detalle',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_moduloconfiguracion', 'icono',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_moduloconfiguracion', 'module',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_moduloconfiguracion', 'mostrar',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_moduloconfiguracion', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_moduloconfiguracion', 'padre',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_moduloconfiguracion', 'sub',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_moduloconfiguracion', 'tipos',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_moduloconfiguracion', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedido', 'comentarios',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_pedido', 'cookie_pedido',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedido', 'email',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedido', 'fecha_creacion',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('seo_pedido', 'fecha_pago',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('seo_pedido', 'idmediopago',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedido', 'idpedidoestado',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedido', 'idusuario',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedido', 'nombre',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedido', 'pedido_manual',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_pedido', 'telefono',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedido', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedido', 'total',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedido', 'total_original',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'cookie_direccion',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'direccion_completa',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'fecha_entrega',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'idpedido',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'idpedidoestado',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'idusuariodireccion',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'nombre',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'precio',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'referencias',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_pedidodireccion', 'telefono',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedidoestado', 'color',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedidoestado', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_pedidoestado', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidoestado', 'resumen',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_pedidoestado', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidoestado', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'cantidad',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'foto',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'idpedido',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'idpedidodireccion',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'idproducto',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'idproductoatributo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'mensaje',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'precio',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'titulo_atributo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_pedidoproducto', 'total',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_producto', 'archivo',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_producto', 'codigo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_producto', 'descripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_producto', 'descuento',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_producto', 'descuento_fecha',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_producto', 'destacado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_producto', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_producto', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_producto', 'idproductocategoria',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_producto', 'keywords',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_producto', 'metadescripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_producto', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_producto', 'precio',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_producto', 'resumen',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_producto', 'stock',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_producto', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_producto', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_producto', 'url',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_producto', 'ventas',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_productocategoria', 'descripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_productocategoria', 'descuento',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_productocategoria', 'descuento_fecha',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_productocategoria', 'destacado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_productocategoria', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_productocategoria', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_productocategoria', 'idpadre',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_productocategoria', 'keywords',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_productocategoria', 'metadescripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_productocategoria', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_productocategoria', 'resumen',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_productocategoria', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_productocategoria', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_productocategoria', 'url',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_profile', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_profile', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_profile', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_profile', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_region', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_region', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_region', 'precio',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_region', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seccion', 'archivo',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccion', 'descripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccion', 'destacado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_seccion', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_seccion', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccion', 'idseccioncategoria',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccion', 'keywords',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seccion', 'metadescripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccion', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_seccion', 'resumen',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccion', 'subtitulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seccion', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_seccion', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seccion', 'url',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'descripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'destacado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_seccioncategoria', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_seccioncategoria', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'idpadre',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'keywords',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'metadescripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'resumen',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seccioncategoria', 'url',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seo', 'banner',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seo', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_seo', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seo', 'keywords',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seo', 'link_menu',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seo', 'menu',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_seo', 'metadescripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_seo', 'modulo_back',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seo', 'modulo_front',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seo', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_seo', 'submenu',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_seo', 'subtitulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seo', 'tipo_modulo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_seo', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_seo', 'url',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_sitemap', 'depth',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_sitemap', 'idpadre',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_sitemap', 'ready',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_sitemap', 'url',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_sitemap', 'valid',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_table', 'fields',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_table', 'idname',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_table', 'tablename',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_table', 'truncate',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_texto', 'descripcion',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_texto', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_texto', 'mapa',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_texto', 'orden',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_texto', 'texto',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_texto', 'tipo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_texto', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_texto', 'url',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuario', 'cookie',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuario', 'email',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuario', 'estado',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    op.alter_column('seo_usuario', 'foto',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_usuario', 'nombre',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuario', 'telefono',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuario', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'casa',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'condominio',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'departamento',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'direccion',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'edificio',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'empresa',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'idcomuna',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'idusuario',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'nombre',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'referencias',
               existing_type=mysql.LONGTEXT(),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'telefono',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'tipo',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'titulo',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    op.alter_column('seo_usuariodireccion', 'villa',
               existing_type=mysql.CHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    pass