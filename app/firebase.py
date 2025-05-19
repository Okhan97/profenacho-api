# app/firebase.py
import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, auth
from google.cloud import firestore

load_dotenv()

cred = credentials.Certificate(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
firebase_admin.initialize_app(cred)
db = firestore.Client()



