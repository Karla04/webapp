CREATE DATABASE d3ngn1fnbhxtvtl4;

USE d3ngn1fnbhxtvtl4;

CREATE TABLE  productos (
  id_producto int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  producto varchar(400) NOT NULL,
  descripcion varchar(100) NOT NULL,
  existencias varchar(100) NOT NULL,
  precio_compra varchar(100) NOT NULL,
  precio_venta varchar(100) NOT NULL,
  imagen_producto varchar(100) NOT NULL
);

INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Samsung Galaxy Grand Prime","Celular","500","$3,500","$3,600","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Laptop Dell","Laptop","200","$5,000","$5,000","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Audifonos Sony","Audifonos Via Bluetooth","400","$1,200","$1,280","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Nokia Lumia 790","Celular","1000","$2,200","$2,400","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Laptop HP","Laptop","300","$8,300","$8,400","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Mouse","Rojo","500","$500","$600","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Cable USB","1.8 mts","200","$50","$100","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Audifonos Steren","Negro/Blanco","900","$170","$280","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("TV LG","49''","450","$13,000","$13,800","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("Calculadora CASIO","Cientifica Marron","900","$370","$490","");
INSERT INTO productos (producto, descripcion, existencias, precio_compra, precio_venta, imagen_producto) VALUES ("DVD","Blu-ray","50","$670","$890","");