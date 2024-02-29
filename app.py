from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import psycopg2

import requests

app = Flask(__name__, template_folder='static/templates')
CORS(app)

habits = []

@app.route('/', methods=['GET'])
def home():
    conn = create_db_connection()
    cursor = conn.cursor()

    sql = """SELECT * FROM HABITS"""

    # Execute the SQL statement with the corresponding values
    cursor.execute(sql)
    habits_data = cursor.fetchall()

    cursor.close()
    conn.close()
    print(habits_data)
    return render_template('habitTracker.html', habits = habits_data)

@app.route('/habit-tracker', methods=['POST'])
def habitTracker():
    try:
        if request.method == 'POST':
            data = request.get_json()
            print('inside post')
            print(data)
            transactionType = data['transactionType']
            if transactionType == 'add':
                print(data)
                habitName = data['habitName']
                habitDescription = data['habitDescription']
                habitFrequency = data['habitFrequency']
                habitReps = data['habitReps']


                conn = create_db_connection()
                cursor = conn.cursor()

                sql = "SELECT * FROM HABITS WHERE HABITNAME = %s"
                cursor.execute(sql, [habitName])
                temp = cursor.fetchall()

                if(len(temp) > 0):
                    cursor.close()
                    conn.close()
                    return jsonify({'message': 'DUPE'})
                

                sql = """
                  INSERT INTO habits (habitName, habitDescription, habitFrequency, habitReps)
                  VALUES (%s, %s, %s, %s)
              """

                # Execute the SQL statement with the corresponding values
                cursor.execute(sql, (habitName, habitDescription, habitFrequency, habitReps))
                conn.commit()

                cursor.close()
                conn.close()

                # create db inserts for journal entries here

                return jsonify({'message': 'Habit added successfully!'})

            if transactionType == 'delete':
                print('here')
                print(data)

                conn = create_db_connection()
                cursor = conn.cursor()

                sql = """DELETE FROM HABITS WHERE HABITNAME = %s"""

                # Execute the SQL statement with the corresponding values
                cursor.execute(sql, [data['habitName']])
                conn.commit()

                sql = """SELECT * FROM HABITS"""
                cursor.execute(sql)
                res = cursor.fetchall()
                cursor.close()
                conn.close()

                # create db inserts for journal entries here

                return jsonify({'message': 'Habit deleted successfully!', 'data': res})
            if transactionType == 'edit':

                conn = create_db_connection()
                cursor = conn.cursor()

                sql = "SELECT * FROM HABITS WHERE HABITNAME = %s"
                cursor.execute(sql, [data['oldHabitName']])
                temp = cursor.fetchall()

                if(len(temp) > 0):
                    cursor.close()
                    conn.close()
                    return jsonify({'message': 'DUPE'})
                

                sql = """UPDATE HABITS SET HABITNAME = %s, HABITDESCRIPTION = %s, HABITREPS = %s, HABITFREQUENCY = %s WHERE HABITNAME = %s"""

                # Execute the SQL statement with the corresponding values
                cursor.execute(sql, [data['habitName'], data['habitDescription'], data['habitReps'], data['habitFrequency'], data['oldHabitName'] ])
                conn.commit()

                sql = """SELECT * FROM HABITS"""
                cursor.execute(sql)
                res = cursor.fetchall()
                cursor.close()
                conn.close()

                # create db inserts for journal entries here

                return jsonify({'message': 'Habit editted successfully!', 'data': res})

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 400





# ---------------------------------- DB INFO SECTION START ---------------------------------- #
def create_db_connection():
  con = psycopg2.connect(
    host='localhost',
    port='5432',
    dbname='habitTrackerDB',
    user='postgres',
    password='password'
  )
  return con

# ----------------------------------- DB INFO SECTION END ----------------------------------- #






if __name__ == '__main__':
  app.run()


def update_table(connection, table_name, update_columns, update_values, condition_column, condition_value):
    # Create a cursor object to execute SQL statements
    conn = create_db_connection()
    cursor = conn.cursor()

    # Construct the UPDATE SQL statement dynamically
    update_query = f"UPDATE {table_name} SET {', '.join([f'{column} = %s' for column in update_columns])} WHERE {condition_column} = %s"

    # Combine the update values and condition value into a single tuple
    update_values_tuple = tuple(update_values + [condition_value])

    # Execute the UPDATE statement
    cursor.execute(update_query, update_values_tuple)

    # Commit the changes
    connection.commit()

    # Close the cursor
    cursor.close()


# CREATE TABLE habits (
#     habitID SERIAL PRIMARY KEY,
#     habitName VARCHAR(50) NOT NULL,
#     habitDescription VARCHAR(250),
# 	habitFrequency INT,
# 	habitReps INT,
#     dateAdded TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );