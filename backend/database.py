from supabase import create_client

SUPABASE_URL = "https://luukbkxdqlyatfcragse.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx1dWtia3hkcWx5YXRmY3JhZ3NlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzg3NjI4MjEsImV4cCI6MjA1NDMzODgyMX0.recYT2Lf0QF-ppmKgixk4YJJ9UIYn03u3A_q-xi4UtY"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_price_data(prices):
    for item, details in prices.items():
        data = {
            "item": item,
            "store": details["store"],
            "price": details["price"],
        }
        supabase.table("price_history").insert(data).execute()

def get_price_history():
    return supabase.table("price_history").select("*").execute()
