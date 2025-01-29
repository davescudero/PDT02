
290120251:13

**El análisis que se realizó fue el siguiente**:
El dataset proporciona datos históricos de ventas diarias. La tarea es predecir la cantidad total de productos vendidos en cada tienda para el conjunto de prueba. Tenga en cuenta que la lista de tiendas y productos cambia ligeramente cada mes. Crear un modelo robusto que pueda manejar tales situaciones es parte del desafío.

En lo que llevamos del EDA se pude observar que el dataset cuenta con 2935849 registros y 6 columnas. Las columnas son las siguientes:
- date 
- date_block_num
- shop_id
- item_id
- item_price
- item_cnt_day

1. Comparamos los datos de las columnas con el tipo de dato que deberian tener y se observo que la columna date es de tipo object y deberia ser de tipo datetime. Se procedio a cambiar el tipo de dato de la columna date a datetime. Se cambió el tipo de dato de la columna item_id a category al igual que la columna shop_id

2. Se comparo shop_id y date para ver cuales tenian flujo de ventas por tienda constante y cuando vendian mas. Es decir que tienda tenia mas flujo de clientes por mes y cuales tenian menos.

3. Se comparo item_id y date para ver cuales tenian flujo de ventas por producto constante y cuando vendian mas. Es decir que producto tenia mas flujo de ventas por mes y cuales tenian menos.

Tener esos puntos en cuenta David <3

