import subprocess

def print_pdf(file_path):
    try:
        subprocess.run(["lp", file_path])
        print("PDF sent to printer")
    except Exception as e:
        print(f"Error: {e}")
