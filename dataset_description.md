# Dataset Description

## Predict Future Sales

Se le proporciona datos históricos de ventas diarias. La tarea es predecir la cantidad total de productos vendidos en cada tienda para el conjunto de prueba. Tenga en cuenta que la lista de tiendas y productos cambia ligeramente cada mes. Crear un modelo robusto que pueda manejar tales situaciones es parte del desafío.

## File descriptions

`sales_train.csv` - el conjunto de entrenamiento. Datos históricos diarios desde enero de 2013 hasta octubre de 2015.

`test.csv` - el conjunto de prueba. Necesita predecir las ventas para estas tiendas y productos para noviembre de 2015.

`sample_submission.csv` - a sample submission file in the correct format.

`items.csv` - información suplementaria sobre los artículos/productos.

`item_categories.csv` - información suplementaria sobre las categorías de artículos.

`shops.csv`- informacion suplemetaria sobre las tiendas.

## Data fields

`ID` - un Id que representa una tupla (Tienda, Artículo) dentro del conjunto de prueba  
`shop_id` - identificador único de una tienda  
`item_id` - identificador único de un producto  
`item_category_id` - identificador único de la categoría de artículo  
`item_cnt_day` - número de productos vendidos. Usted está prediciendo una cantidad mensual de esta medida  
`item_price` - precio actual de un artículo  
`date` - fecha en formato dd/mm/yyyy  
`date_block_num` - un número de mes consecutivo, usado para conveniencia. Enero 2013 es 0, Febrero 2013 es 1,..., Octubre 2015 es 33  
`item_name` - nombre del artículo  
`shop_name` - nombre de la tienda  
`item_category_name` - nombre de la categoría de artículo  
