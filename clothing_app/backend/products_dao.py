import mysql.connector

def get_all_products():
    
    # Creating Database Connection
    cnx = mysql.connector.connect(user='root',password='root',
                                host='127.0.0.1',
                                database='cs')

    #Creating Database Cursor
    cursor = cnx.cursor()

    #Database Query - To Be Amended upon Database Update
    query = ("SELECT products.product_id, products.product_name, products.uom_id, uom.uom_name, products.product_size_id, size.size_name, products.product_color_id, color.color_name,products.price_per_item FROM products INNER JOIN uom ON products.uom_id = uom.uom_id INNER JOIN size ON products.product_size_id = size.size_id INNER JOIN color ON products.product_color_id = color.color_id;")

    #Cursor Execution
    cursor.execute(query)

    #List of Dictionary containing all products info's - We are using Dictionary so we can extract certain informations easier
    response = []

    #Loop that gets all relevant product info from database 
    for (product_id, product_name, uom_id, uom_name, product_size_id, size_name, product_color_id, color_name, price_per_item) in cursor :
        response.append(
            {
                'product_id' : product_id,
                'product_name' : product_name,
                'uom_id' : uom_id,
                'uom_name' : uom_name,
                'product_size_id' : product_size_id,
                'size_name' : size_name,
                'product_color_id' : product_color_id,
                'color_name' : color_name,
                'price_per_item' : price_per_item
            }
        )

        #print(product_id, product_name, uom_id, uom_name, product_size_id, size_name, product_color_id, color_name, price_per_item) - This method was used for testing purposes as it only prints the results.

    #Closing Connection
    cnx.close()

    return response

if __name__ == '__main__':
    print(get_all_products())