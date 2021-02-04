import sys
import psycopg2
database = "olympics"
user = ""
password = ""


search_string = 'Brontë'
query = '''SELECT first_name, last_name
           FROM authors
           WHERE last_name = %s'''
try:
    cursor.execute(query, (search_string,))
except Exception as e:
    print(e)
    exit()

print('===== Authors with last name {0} ====='.format(search_string))
for row in cursor:
    print(row[0], row[1])
print()

'''
Prints a list of all NOCs and the gold medals they have won, sorted in decreasing order.
'''
def listGolds():
    # Connect to the database
    try:
        connection = psycopg2.connect(database=database, user=user, password=password)
    except Exception as e:
        print(e)
        exit()

    try:
        cursor = connection.cursor()
        query = 'SELECT NOCs.noc_abbre, COUNT(NOCs_Medals.noc_id) FROM NOCs, NOCs_Medals, Medals WHERE NOCs.id = NOCs_Medals.noc_id AND NOCs_Medals.medal_id = Medals.id AND Medals.medal_type = "Gold" GROUP BY NOCs.noc_abbre ORDER BY COUNT(NOCs_Medals.noc_id) DESC;'
        cursor.execute(query)
    except Exception as e:
        print(e)
        exit()

    print('===== List of Gold medals sorted by NOC =====')
    for row in cursor:
        print(row[0], row[1])
    print()

def main():
    if len(sys.argv) < 2:
        print("You didn't give any arguments.")

    command = str(sys.argv[1])

    if command == "--help" or command == "-h":
        print("something")
    
    if command == "--listNOCAthletes" or command == "-lna":
        NOC = str(sys.argv[2])
    
    if command == "--listGolds" or command == "-lg":
        listGolds()

