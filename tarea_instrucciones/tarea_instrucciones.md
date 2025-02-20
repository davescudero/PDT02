# Tarea 02

En las primeras clases del curso estaremos trabajando en desarrollar buenas
prácticas para construir productos de datos. La parte conceptual como la
parte de programación son igualmente importantes. Para poder bajar las ideas
a la práctica necesitamos una muestra de código.

## Contexto:

* Supon que estamos trabajando en una start up de bienes raices y necesitamos
construir un producto de datos que ayude a soportar una aplicación para 
que nuestros clientes (compradores/vendedores) puedan consultar una estimación
del valor de una propiedad de bienes raíces.

* Aún el CEO no tiene claro como debe de diseñarse esta aplicación. Nostros
como data scientists debemos proponer una Prueba de Concepto, que permita
experimentar rápido, dar un *look an feel* de la experiencia y nos permita
fallar rápido para probar una siguiente iteración.

## Objetivo:

* Prototipa un modelo en Python que permita estimar el precio de una casa
dadas algunas características que el usuario deberá proporcionar a través de
un front al momento de la inferencia.

## Datos:

* En vista de que el CEO no tiene mucha claridad, podemos construir un dataset
  con dato sintéticos o tomar alguno otro como referencia, para poder 
  desarrollar nuestra idea.

* Para lo cual usaremos el [conjunto de precios de compra-venta de casas de la
  ciudad Ames, Iowa en Estados Unidos](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques).

* Si sientes que este conjunto de datos está por debajo de tu nivel, o como dirían en inglés **you are feeling dangerous**, puedes trabajar con el conjunto de datos [predicción de ventas de la empresa 1C](https://www.kaggle.com/competitions/competitive-data-science-predict-future-sales).

## Entregable

* Un notebook o notebooks que puedas presentar, desarrollando todos los 
pasos que seguiste para construir tu modelo.

* Recuerda incluir la ingeniería de características, la selección de variabales,
el entrenamiento del modelo, la evaluación del ajuste y un ejemplo de como se
ejecutaran las inferencias. Muy importante no olvides el EDA.

* Un diagrama que muestre el flujo de trabajo, y como está interactuando tu código. Usa [diagrams.net](https://app.diagrams.net/).

## Out of scope

* Desarrollar una herramienta, API, etc.
