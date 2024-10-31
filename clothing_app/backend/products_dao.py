import mysql.connector

cnx = mysql.connector.connect(user='root',password='root',
                              host='127.0.0.1',
                              database='cs')

cursor = cnx.cursor()

query = "SELECT * FROM cs.products"

cursor.execute(query)

for (product_id, product_name, uom_id, product_size_id, product_color_id, price_per_item) in cursor :
    print(product_id, product_name, uom_id, product_size_id, product_color_id, price_per_item)
    
cnx.close()