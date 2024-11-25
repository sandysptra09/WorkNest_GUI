import bcrypt
from getpass import getpass
from configs.db_connection import create_connection

def login():
    try:
        connection = create_connection()
        with connection.cursor(dictionary=True) as cursor:
            print("\n" + "=" * 60)
            print("🔐 Login to WorkNest")
            print("=" * 60)
            
            email = input("📧  Email: ").strip()
            password = getpass(" Password: ").strip()
            
            # query to search for users by email
            query = "SELECT * FROM employees WHERE email = %s"
            cursor.execute(query, (email,))
            user = cursor.fetchone()
            
            if user:
                # validation password
                hashed_password = user['password']  
                
                # hash password in database
                if bcrypt.checkpw(password.encode(), hashed_password.encode()):
                    return user  
                else:
                    print("\n❌ Invalid password. Please try again.")
            else:
                print("\n❌ User not found. Please check your email.")
            
            if user:
                # validating password
                hashed_password = user
    
    except Exception as e:
        print(f'\n⚠️ Error during login: {e}')
    finally:
        connection.close()
        
    # failed to login
    return None