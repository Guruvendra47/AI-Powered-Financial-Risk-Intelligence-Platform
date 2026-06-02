from src.cloud.snowflake.snowflake_connection import get_connection

def main():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT CURRENT_VERSION()"
    )

    result = cursor.fetchone()

    print(
        f"Snowflake Version: {result[0]}"
    )

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
