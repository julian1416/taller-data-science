SELECT 
    cliente.ID AS Codigo_Cliente,
    cliente.NOMBRE,
    cliente.APELLIDO,
    ventas.ID_VENTAS AS Numero_Factura,
    ventas.VALOR,
    ventas.FECHA
FROM ventas
INNER JOIN cliente ON ventas.ID_CLIENTE = cliente.ID;