import os
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin import storage
from tkinter import messagebox
from utils import generic as gen
from services import global_vars as gv
from dotenv import load_dotenv

load_dotenv()

# Initialize Firestore with your credentials
cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred, {'storageBucket': os.getenv("STORAGEBUCKET")})
db = firestore.client()
storage_bucket = storage.bucket()

class FirebaseService:
    def __init__(self):
        pass

    '''
        Summary: Verify if a user exists and sign in
        Parameters: username: string, password: string
        Returns: boolean
    '''
    def sign_in(self, username, password):
        try:
            #Reference to the collection
            collection_ref = db.collection("users")

            # Get all documents from the collection
            docs = collection_ref.stream()

            # Iterating over all documents
            for doc in docs:

                # Get doc data
                doc_data = doc.to_dict()

                # Verify if the username exists
                if doc_data["username"] == username:

                    # Decrypt the password and verify if it is valid
                    valid_password = gen.decrypt_password(password, doc_data["password"])

                    # If the password is valid, save the user data and return True
                    if valid_password:
                        # Save user data
                        gv.user_data = doc_data

                        # Add the user id to the user data
                        gv.user_data["id"] = doc.id

                        return True
                    
                    # If the password is invalid, return False
                    else:
                        return False

            # If the username does not exist, return False
            return False

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    '''
        Summary: Get all documents from a collection
        Parameters: collection_name: string
        Returns: list of documents
    '''
    def get_collection(self, collection_name):
        # Get all docs from collection
        try:
            # Collection Reference
            collection_ref = db.collection(collection_name)
            # Get all docs from collection
            docs = collection_ref.stream()

            # List to store all docs
            data = []
            # Iterate over all docs
            for doc in docs:
                # Get doc data
                doc_data = doc.to_dict()
                # Add doc data to list
                data.append(doc_data)

            return data

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    '''
        Summary: Get documents with status "active" from a collection
        Parameters: collection_name: string
        Returns: list of documents
    '''
    def get_active_collection(self, collection_name):
        # Get all docs from collection with status "active"
        try:
            # Collection Reference
            collection_ref = db.collection(collection_name)
            # Get all docs from collection
            docs = collection_ref.where("status", "==", "active").stream()

            # List to store all docs
            data = []
            # Iterate over all docs
            for doc in docs:
                # Get doc data and doc id
                doc_data = doc.to_dict()
                doc_data["id"] = doc.id
                # Add doc data to list
                data.append(doc_data)

            return data

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    '''
        Summary: Insert a new document in a collection
        Parameters: collection_name: string, data: dict
        Returns: None
    '''
    def insert_collection(self, collection_name, data):
        # Add a new doc in collection
        try:
            # Collection Reference
            collection_ref = db.collection(collection_name)
            # Add data to collection
            collection_ref.add(data)

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    '''
        Summary: verify if username or email already exists in users collection
        Parameters: username: string, email: string
        Returns: boolean
    '''
    def verify_user(self, username, email):
        # Verify if username or email already exists
        try:
            # Collection Reference
            collection_ref = db.collection("users")
            # Get all docs from collection
            docs = collection_ref.stream()

            # Iterate over all docs
            for doc in docs:
                # Get doc data
                doc_data = doc.to_dict()
                # Check if username or email already exists
                if doc_data["username"] == username or doc_data["email"] == email:
                    return True

            return False

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    '''
        Summary: Verify if username or email already exists in users collection, except for the current user
        Parameters: username: string, email: string
        Returns: boolean
    '''
    def verify_others_users(self, username, email):
        # Verify if username or email already exists, except for the current user
        try:
            # Collection Reference
            collection_ref = db.collection("users")
            # Get all docs from collection
            docs = collection_ref.stream()

            # Iterate over all docs
            for doc in docs:
                # Get doc data
                doc_data = doc.to_dict()
                # Check if username or email already exists, except for the current user
                if (doc_data["username"] == username or doc_data["email"] == email) and doc.id != gv.user_data["id"]:
                    return True

            return False

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    
    '''
        Summary: Update a document in a collection
        Parameters: collection_name: string, doc_id: string, data: dict
        Returns: None
    '''
    def update_collection(self, collection_name, doc_id, data):
        # Update a doc in collection
        try:
            # Collection Reference
            collection_ref = db.collection(collection_name)
            # Doc Reference
            doc_ref = collection_ref.document(doc_id)
            # Update doc data
            doc_ref.update(data)

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

    '''
        Summary: Upload an image to Firebase Storage
        Parameters: file_path: string, file_name: string
        Returns: string
    '''
    def upload_image(self, file_path, file_name, folder_name):
        try:
            blob = storage_bucket.blob(f"{folder_name}/{file_name}")
            blob.upload_from_filename(file_path)
            # Expiration date in 7 days
            image_url = blob.generate_signed_url(version="v4", expiration=604800)
            return image_url

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    